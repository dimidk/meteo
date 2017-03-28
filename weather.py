#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import serial
import sys
import time
import init
from dbWeather import weather
from sqlalchemy import func
from sqlalchemy.orm.exc import *


"""connect to port"""
ser=serial.Serial(init.serialPort,9600, timeout=2)
try:
	ser.open()
except serial.SerialException:
	print "error:catch exception"
	
"""ser.write(':A\n')"""
ser.write(':Q\n')
"""read from port"""



while True:
	try:
		"""buf="D,01/13,05:50:00, 75, 81,21.75,170,""" 
		"""buf=buf+8, 78, 0.00,1650,0.266, 4.7124, 5.67,  63,!184"""


		buf=ser.readline()
		if buf.find('OK')!=-1:
			continue
		print buf
	
	
		"""select_cmd=init.dbsession.query(weather.id,weather.info).all()"""
		
		"""if select_cmd is None
				numrows=1
			else:

				for id,info in select_cmd:
					print id,info
				numrows=init.dbsession.query(func.count(weather.id)).scalar()
			print numrows"""




		"""insert_file=weather(info=buf)
		init.dbsession.add(insert_file)	
		init.dbsession.commit()	
		time.sleep(1)"""
	except KeyboardInterrupt:
		print "you press Ctrl+C"
		sys.exit()
	
	

	
	
"""init.dbsession.close()"""
	
	
	

