# Jack B
# Make sure to download the adafruit_ads1x15 .git
#tutorial >> https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/ads1015-slash-ads1115
#the .git >> https://github.com/adafruit/Adafruit_Python_ADS1x15



import Adafruit_ADS1x15
import sqlite3
import time
import random
from datetime import datetime
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

#def get_random(a,b):
    #return random.uniform(a,b)
def get_windspeed():
    return  adc.read_adc(3, gain=GAIN)
def get_temp():
    return  adc.read_adc(2, gain=GAIN)
def get_pressure():
    return  adc.read_adc(1, gain=GAIN)
    




conn = sqlite3.connect('WeatherStation.db')
tempv= (get_temp()*4.096/32767)

windspeed = (get_windspeed()*4.096/32767)
tempc = (tempv - 0.5) / 0.01
tempf = (tempc * 1.8) + 32
pressure = (get_pressure()*4.096/32767)
date = datetime.now()



print("Windspeed: {} | Pressure: {} | Temp Celsius: {}  | Temp Fahrenheit: {} Date: {}".format(windspeed, pressure, tempc, tempf, date))
conn.execute("INSERT INTO WEATHER (WINDSPEED,PRESSURE,TEMP,DATE) VALUES (?,?,?,?)", (windspeed,pressure,temp,date))



conn.commit()
print("Record created successfully")
conn.close()





