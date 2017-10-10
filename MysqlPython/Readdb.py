#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.execute("SELECT windspeed, pressure, temp, date from WEATHER")
results = cursor.fetchall()

print("The DB has {} records".format(len(results)))

print(results)

for row in results:
   print("windspeed = ", row[0])
   print("pressure = ", row[1])
   print("temp = ", row[2])
   print("date = ", row[3], "\n")

print("Operation done successfully")
conn.close()
