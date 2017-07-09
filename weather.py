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

"""write to log file, eventually too large"""


"""connect to port"""
attempt=0
ser=serial.Serial(init.serialPort,9600,timeout=2)
"""ser=serial.Serial('/dev/ttyUSB1',9600,timeout=2)"""
fp=open(init.logDbFile,'a+')

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
fp.close()

print "Start to read from station. Press Ctrl+C to stop the process"

while True:
	try:
		"""buf="D,05/18,05:50:00, 75, 81,21.75,170,"
		buf=buf+"8, 78, 0.00,1650,0.266, 4.7124, 5.67,  63,!184"""
		if init.dbsession.is_active:
			print "session active"
			fp=open(init.logDbFile,'a+')
			d=datetime.datetime.now()
	
			timing=str(d.hour)+":"+str(d.minute)+":"+str(d.second)
	
			if d.month<10:	
				date_str='0'+str(d.month)+"/"+str(d.day)
			else:
				date_str=str(d.month)+'/'+str(d.day)
		
			buf=ser.readline()
			print buf, len(buf)
			fp.write(date_str+" "+timing+":"+buf+'\n')
		
			"""if buf.startswith(' ')==True:
				print "There must be an error"
				fp.write(date_str+" "+timing+":"+'Buffer str starts with space ' '. There must be an error\n')
				exit(1)
			elif buf.startswith('>')==True:
				fp.write(date_str+" "+timing+":"+'Waiting for command or data\n')
				continue
			elif buf=='' or buf=='\n':
				print "no data read"
				fp.write(date_str+" "+timing+":"+'No data read from port\n')
			
			
				continue
			else:
				print "read data"
				fp.write(date_str+" "+timing+":"+'Data read from port\n')
				fp.write(date_str+" "+timing+":"+buf+'\n')"""
			
			if len(buf)>10 and buf.find(',')!=-1:
			
				buf_list=buf.split(',')
				buf_list.pop(1)
				buf=','.join(buf_list)
			else:
				fp.close()
				continue
				
			fp.write(date_str+" "+timing+":"+buf+'\n')
	
			insert_file=weather(info=buf,m_date=date_str)
		
			fp.write(date_str+" "+timing+":"+'create insertion record \n')
		
		
			try:
							
				init.dbsession.add(insert_file)	
				init.dbsession.commit()
		
				fp.write(date_str+" "+timing+":"+'commit insertion to database\n')
			except:
			
				"""fp.write(date_str+" "+timing+":"+e.message+'\n')"""
				fp.write(date_str+" "+timing+":database error\n")
				raise Exception("database connection error")
			"""finally:
				init.dbsession.close()"""
			
			fp.write(date_str+" "+timing+":"+'sleep 10 secs\n')
			fp.close()
			time.sleep(10)
		
		else:
			raise Exception("database connection closed")
			
	except KeyboardInterrupt:
		print "you press Ctrl+C"
		fp.close()
		init.dbsession.close()
		sys.exit()
