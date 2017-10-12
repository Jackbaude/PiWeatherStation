# PiWeatherStation
My science fair raspberry pi weather station.


# Install libraries


## Install sqlite
```
sudo apt-get install sqlite3
```
### Install the flask framework

```
# sudo apt-get install flask
```
### Use the Adafruit .git for the ADS1115
```
git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git
```

### Use python sql library to create/insert/read data (run this under the Directory that you want this code)

```
wget https://raw.githubusercontent.com/Jackbaude/PiWeatherStation/master/MysqlPython/InsertData.py
```
```
https://raw.githubusercontent.com/Jackbaude/PiWeatherStation/master/MysqlPython/Readdb.py
```
```
https://raw.githubusercontent.com/Jackbaude/PiWeatherStation/master/MysqlPython/createdb.py
```


### Edit SQlite data table 

```
sqlite3 mydatabase.db
```
