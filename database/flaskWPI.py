from flask import Flask, render_template, session, request
import sqlite3



conn = sqlite3.connect('WeatherStation.db')
cursor = conn.execute("SELECT windspeed, pressure, temp, date from WEATHER")
results = cursor.fetchall()

print("The DB has {} records".format(len(results)))



def classify_results(db_results):
    # This function takes the DB results and iterates through them creating a new
    # list.  In the new list, each "row" is a class instance of Row
    results = []
    for row in db_results:
        # This is python shorthand for what was done before where it was doing
        # windspeed = row[0]
        windspeed, pressure, temp, date = row
        # Now we take those and create an instance of Row and feed it the values
        # which are appended to our *new* results list (array).
        results.append(Row(windspeed, pressure, temp, date))

    # And we return the new list of results which is a list of Row objects.
    return results


# Dummy class for making it easier to refer to the DB fields.  Simply
# instantiate the class and feed it the field results.
# Using named tuples would also be an option.
class Row(object):
    def __init__(self, windspeed, pressure, temp, date):
        self.windspeed = round(windspeed,2)
        self.pressure = pressure
        self.temp = round(temp,1)
        self.date = date




app = Flask(__name__)
# This is a test to verify that falsk works
@app.route('/hello')
def hello_flask():
    return 'Hello from flask\n'



@app.route('/sqlone')
def sqlone():        # Make the connection to the DB
    conn = sqlite3.connect('WeatherStation.db')
    
    cursor = conn.execute("SELECT * from WEATHER")
    
    # Fetch all the results
    results = classify_results(cursor.fetchall())
    
    print("The DB has {} records".format(len(results)))
    
    
    # Now when we iterate the results, we can refer to the DB fields
    # which seems easier than positional numbers in the list (array)
    
    html = "<html><body><table border=1><tr><th>windspeed</th><th>pressure</th><th>temp</th><th>date</th></tr>"# or its tuple
    for row in results:
        print(row.windspeed, row.pressure, row.temp, row.date)
        html += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(row.windspeed, row.pressure, row.temp, row.date)
    
    conn.close()   

    html+= "</table> </body> </html>"
    return html




















if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0")
