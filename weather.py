#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import serial
import time
import init
from dbWeather import weather
from sqlalchemy import func
from sqlalchemy.orm.exc import *

ser=serial.Serial(init.serialPort,9600, timeout=2)
try:
	ser.open()
except serial.SerialException:
	print "error:catch exception"
	
ser.write(':A\n')	
while True:
	buf=ser.readline()
	print buf
	
	
	select_cmd=init.dbsession.query(weather.id,weather.info).all()
	"""if table is empty"""
	if select_cmd is None:
		numrows=1
	else:
		"""if table is not empty get numrows"""
		for id,info in select_cmd:
			print id,info
		numrows=init.dbsession.query(func.count(weather.id)).scalar()
	print numrows

	""" insert into to table"""
	insert_file=weather(id=numrows+1,info=buf)
	init.dbsession.add(insert_file)	
	init.dbsession.commit()
	"""only close the session doesn't do disconnect"""
	init.dbsession.close()
	
	
	
