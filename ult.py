# Jack B
#I have implemeted both FlaskWPI and Weather into one script, this way i can check the database and the current weather on one server.
 
import sqlite3
from flask import Flask, render_template, session, request
import datetime
app = Flask(__name__)
import Adafruit_ADS1x15
import time

conn = sqlite3.connect('WeatherStation.db')
cursor = conn.execute("SELECT windspeed, pressure, temp, date from WEATHER")
results = cursor.fetchall()


def classify_results(db_results):
    results = []
    for row in db_results:
        windspeed, pressure, temp, date = row
        results.append(Row(windspeed, pressure, temp, date))
    return results

class Row(object):
    def __init__(self, windspeed, pressure, temp, date):
        self.windspeed = round(windspeed,2)
        self.pressure = pressure
        self.temp = round(temp,1)
        self.date = date



DEBUG = True
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
date = datetime.date.today()
localtime = time.localtime(time.time())

# Data Collecting Functions -
def _get_temp_voltage():
    return  adc.read_adc(2, gain=GAIN)*4.096/32767

def _get_wind_voltage():
    return  adc.read_adc(3, gain=GAIN)*4.096/32767

def _get_pressure():
    return  adc.read_adc(1, gain=GAIN)*4.096/32767

def get_tempcel():
    tempc = (_get_temp_voltage() - 0.5) / 0.01
    return str(float(round(tempc, 2)))

def get_tempfar():
    tempc = (_get_temp_voltage() - 0.5) / 0.01
    tempf = (tempc * 1.8) + 32
    return str(float(round(tempf, 2)))

def give_wind_speed():
    MPS = _get_wind_voltage()*(1.6/32.4) + 0.4
    MPH = (MPS*2.23694)
    if MPH <= 0.94 :
        return ("(No Current windpseed)")
    else:
        return str(float(round(MPH,3)))
   
# Test to see if flask works
@app.route('/hello')
def hello_flask():
    return 'Hello from flask\n'


# Live data
@app.route('/Weatherpage')
def weatherprint():
    return render_template('Weather1.html',date = date, TEMF = get_tempfar(), TEMC = get_tempcel(), windspeed = give_wind_speed())
            
# database
@app.route('/sqlone')
def sqlone():        # Make the connection to the DB
    conn = sqlite3.connect('WeatherStation.db')
    
    cursor = conn.execute("SELECT * from WEATHER")
    
    # Fetch all the results
    results = classify_results(cursor.fetchall())
    
    print("The DB has {} records".format(len(results)))
    
    
    # Now when we iterate the results, we can refer to the DB fields
    # which seems easier than positional numbers in the list (array)
    
    html = "<html><body><table border=1><tr><th>Windspeed</th><th>Pressure</th><th>Temperature</th><th>Date</th></tr>"# or its tuple
    for row in results:
        #print(row.windspeed, row.pressure, row.temp, row.date)
        html += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(row.windspeed, row.pressure, row.temp, row.date)
    
    conn.close()   

    html+= "</table> </body> </html>"
    return html
    


if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0")
