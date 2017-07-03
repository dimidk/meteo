# meteo
meteo

Reads from a weather station (weather.py) and writes to a database(dbWeather.py file ). Runs on raspberry PI.

Using a specific url reports about the weather, reading information from database (meteo_web.py).

The weather station model is MKIIICC Rainwise using XMODEM protocol.

In detail the project consists of files:

init.py:Defines database name and database table name, port to connect to weather station, log file name.

dbWeather.py:creates database table, or reads table's schema. Database connection and table creation is done using ORM SQLAlchemy.

weather.py:connects to specific port to weather station and reads data. Connect to database and insert records data and writes to a log file.

meteo_web.py:A small web application which creates a simple html page (index.html) reporting weather information from database.This is done by using web.py.

del_dbWeather.py:Delete records from mysql database, the user specifies exactly date and all records are deleted

Prerequisites:mysql_connector, sqlalchemy, PySerial (module to connect to port) on raspberry
              web.py for web application
      
Installation Dependencies:

install web.py

	-pip2 install web.py
otherwise 

	-cd /opt/
		wget http://webpy.org/static/web.py-0.37.tar.gz
		tar -xzvf web.py-0.37.tar.gz
		cd /opt/web.py-0.37/
		python setup.py install

if want to upgrade

	-cd /opt/webpy/
		git clean -f 
		git pull
		python setup.py install
		
install python mysql module

	-sudo apt-get install libmysqlclient-dev
	 sudo apt-get install python-mysqldb

raspberry

	-install mysql-connector
		get mysql-connector....deb and unpack using dpkg
	
	-install sqlalchemy
		install easy_install
			python ez_setup.py
		easy_install SQLAlchemy
	-install PySerial
		easy_install PySerial
