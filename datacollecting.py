import Adafruit_ADS1x15
import sqlite3
import time
import random
from datetime import datetime
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

def get_random(a,b):
    return random.uniform(a,b)

def get_voltage():
    return  adc.read_adc(3, gain=GAIN)





conn = sqlite3.connect('test.db')

windspeed = (get_voltage()*4.096/32767)
pressure = get_random(0,39)
temp = get_random(32, 99)
date = datetime.now()



print("Wind: {} Pressure: {} Temp: {} Date: {}".format(windspeed, pressure, temp, date))
conn.execute("INSERT INTO WEATHER (WINDSPEED,PRESSURE,TEMP,DATE) VALUES (?,?,?,?)", (windspeed,pressure,temp,date))



conn.commit()
print("Record created successfully")
conn.close()




