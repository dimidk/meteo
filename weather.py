#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import serial
import sys
import time
import datetime
import init
from dbWeather import weather
from sqlalchemy import func
from sqlalchemy.orm.exc import *
from  sqlalchemy import exc


"""connect to port"""
attempt=0
ser=serial.Serial(init.serialPort,9600,timeout=2)
fp=open(init.logFile,'w')

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
fp.write("read from port\n")

print "Start to read from station. Press Ctrl+C to stop the process"

while True:
	try:
		"""buf="D,05/18,05:50:00, 75, 81,21.75,170,"
		buf=buf+"8, 78, 0.00,1650,0.266, 4.7124, 5.67,  63,!184"""
		d=datetime.datetime.now()
	
		if d.month<10:
			date_str='0'+str(d.month)+"/"+str(d.day)
		else:
			date_str=str(d.month)+'/'+str(d.day)
	
	
		
		buf=ser.readline()
		print buf
		fp.write(buf+'\n')
		
		
		
		if buf.startswith(' ')==True:
			print "There must be an error"
			fp.write('Buffer str starts with space ' '. There must be an error\n')
			exit(1)
		elif buf.startswith('>')==True:
			fp.write('Waiting for command or data\n')
			continue
		elif buf=='':
			print "no data read"
			fp.write('No data read from port\n')
			"""exit(1)"""
			continue
		else:
			print "read data"
			fp.write('Data read from port\n')
			
		
		buf_list=buf.split(',')
		buf_list.pop(1)
		buf=','.join(buf_list)
		
		print buf_list
		print date_str
		
		print buf
		fp.write(buf+'\n')
	
		
		insert_file=weather(info=buf,m_date=date_str)
		fp.write('create insertion record \n')
		fp.write(insert_file+'\n')
		try:
			init.dbsession.add(insert_file)	
			init.dbsession.commit()
			fp.write('commit insertion to database\n')	
		except SQLAlchemyError as e:
			fp.write(e.message+'\n')
		fp.write('sleep 10 secs\n')	
		time.sleep(10)
		
		
	except KeyboardInterrupt:
		print "you press Ctrl+C"
		fp.close()
		init.dbsession.close()
		sys.exit()
