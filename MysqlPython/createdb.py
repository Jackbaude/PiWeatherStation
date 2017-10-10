#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')

conn.execute('''CREATE TABLE WEATHER
         (WINDSPEED  FLOAT NOT NULL,
         PRESSURE FLOAT NOT NULL,
         TEMP FLOAT,
         DATE DATETIME PRIMARY KEY NOT NULL);''')

conn.close()
