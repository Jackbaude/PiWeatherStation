#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('WeatherStation.db')
#change the name of test.db to whatever you would like to call your database
conn.execute('''CREATE TABLE WEATHER
         (WINDSPEED  FLOAT NOT NULL,
         PRESSURE FLOAT NOT NULL,
         TEMP FLOAT,
         DATE DATETIME PRIMARY KEY NOT NULL);''')

conn.close()
