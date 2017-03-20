#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import serial
import time
import init
from dbWeather import weather
from sqlalchemy import func
from sqlalchemy.orm.exc import *

"""ser=serial.Serial('/dev/ttyUSB1',9600, timeout=2)
try:
	ser.open()
except serial.SerialException:
	print "error:catch exception"
	
ser.write(':A\n')	
while True:
	buf=ser.readline()"""
select_cmd=init.dbsession.query(weather.id,weather.info).all()
for id,info in select_cmd:
	print id,info
numrows=init.dbsession.query(func.count(weather.id)).scalar()
print numrows
buf="D,12/3/12,12:32:33,45,234,432,213,443"	
insert_file=weather(id=numrows+1,info=buf)
init.dbsession.add(insert_file)	
init.dbsession.commit()
"""only close the session doesn't do disconnect"""
init.dbsession.close()
	
	
	

