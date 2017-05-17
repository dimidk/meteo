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
attempt=0
ser=serial.Serial(init.serialPort,9600,timeout=2)

"""while True:
	attempt+=1
	if attempt==4:
		print "exiting after 3  attempts to connect to port"
		sys.exit(0)
	print "try to connect to port"
	try:
		ser.open()
		break
	except serial.SerialException as e:
		print e
		print "error:catch exception"
		print "sleeping 2 secs"
		time.sleep(2)
		continue"""
	
ser.write(':A\n')
"""ser.write(':Q\n')
read from port"""

print "Start to read from station. Press Ctrl+C to stop the process"

while True:
	try:
		"""buf="D,01/01/17,05:50:00, 75, 81,21.75,170,"
		buf=buf+"8, 78, 0.00,1650,0.266, 4.7124, 5.67,  63,!184"""
		"""date_str="17/01/05"""

		
		
		buf=ser.readline()
		print buf
		
		
		
		if buf.startswith(' ')==True:
			print "There must be an error"
			exit(1)
		elif buf.startswith('>')==True:
			continue
		elif buf=='':
			continue
		else:
			print "read data"
		
		
		buf_list=buf.split(',')
		date_str=buf_list.pop(1)
		buf=buf_list.join(',')
		
		print buf_list
		print date_str
		
		print buf
	
		
		insert_file=weather(info=buf,m_date=date_str)
		init.dbsession.add(insert_file)	
		init.dbsession.commit()	
		time.sleep(10)
	except KeyboardInterrupt:
		print "you press Ctrl+C"
		init.dbsession.close()
		sys.exit()
