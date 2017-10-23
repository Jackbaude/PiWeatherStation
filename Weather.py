# Jack B
# Weather uploader 

from flask import Flask, render_template, session, request
import datetime
app = Flask(__name__)
import Adafruit_ADS1x15
import time
#40494D is gun black in html
DEBUG = True

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
date = datetime.date.today()
localtime = time.localtime(time.time())

def _get_temp_voltage():
    return  adc.read_adc(2, gain=GAIN)*4.096/32767

def get_tempcel():
    tempc = (_get_temp_voltage() - 0.5) / 0.01
    return str(float(round(tempc, 2)))

def get_tempfar():
    tempc = (_get_temp_voltage() - 0.5) / 0.01
    tempf = (tempc * 1.8) + 32
    return str(float(round(tempf, 2)))



# Tests
@app.route('/hello')
def hello_flask():
    return 'Hello from flask\n'


# Live data

@app.route('/Weatherpage')
def weatherprint():
    return render_template('Weather1.html',date = date, TEMF = get_tempfar(), TEMC = get_tempcel())
            

    


