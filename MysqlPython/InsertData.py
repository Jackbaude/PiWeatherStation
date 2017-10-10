#!/usr/bin/python

import sqlite3, random
from datetime import datetime

conn = sqlite3.connect('test.db')

def get_random(a,b):
    return random.uniform(a,b)

windspeed = get_random(0, 51)
pressure = get_random(0,39)
temp = get_random(32, 99)
date = datetime.now()
print("Wind: {} Pressure: {} Temp: {} Date: {}".format(windspeed, pressure, temp, date))
conn.execute("INSERT INTO WEATHER (WINDSPEED,PRESSURE,TEMP,DATE) VALUES (?,?,?,?)", (windspeed,pressure,temp,date))

#conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
#
#conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")
#
#conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

conn.commit()
print("Record created successfully")
conn.close()
