app = Flask(__name__)
import Adafruit_ADS1x15
import time



adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
date = datetime.date.today()
localtime = time.localtime(time.time())


def get_temp():
    return  adc.read_adc(2, gain=GAIN)

def get_windspeed():
    return  adc.read_adc(3, gain=GAIN)

def get_pressure():
    return  adc.read_adc(1, gain=GAIN)

tempv= (get_temp()*4.096/32767)
tempc = (tempv - 0.5) / 0.01
tempf = (tempc * 1.8) + 32
TEMC = str(float(round(tempc, 2)))
TEMF = str(float(round(tempf, 2)))

# use for flask test
@app.route('/hello')
def hello_flask():
    return 'Hello from flask\n'




# -----------------------------------------------------------------
@app.route('/Weatherpage')
def weatherprint():
    return render_template('Weather1.html',date = date, TEMF = TEMF, TEMC = TEMC)
            
    
    
























if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0")
