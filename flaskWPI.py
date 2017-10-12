from flask import Flask, render_template, session, request
import sqlite3



conn = sqlite3.connect('test2.db')
cursor = conn.execute("SELECT windspeed, pressure, temp, date from WEATHER")
results = cursor.fetchall()

print("The DB has {} records".format(len(results)))




app = Flask(__name__)
# This is a test to verify that falsk works
@app.route('/hello')
def hello_flask():
    return 'Hello from flask\n'



@app.route('/sqlone')
def sqlone():
    return render_template('sqltest.html', varible = '1234')
        

    




















if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0")
