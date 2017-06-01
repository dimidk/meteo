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


"""empty previous day records
   best way is to add a column date to do the deletion of previous day's records"""

print "Start to read from station. Press Ctrl+C to stop the process"

while True:
	try:
		"""buf="D,01/01/17,05:50:00, 75, 81,21.75,170,"
		buf=buf+"8, 78, 0.00,1650,0.266, 4.7124, 5.67,  63,!184"
		
		date_str="01/17"
		print buf"""
		
		
		print "Give a date or press Ctrl+C to exit"
		date_str=raw_input("Give a date or press enter to get system date (MM/DD) or Ctrl+C")
		sys_date=date_str
		if date_str=='':
			date_str=datetime.datetime.now()
			if date_str.month<10:
				sys_date='0'+str(date_str.month)+'/'+str(date_str.day)
			else:
				sys_date=str(date_str.month)+'/'+str(date_str.day)
			
		"""take date change to str or vice versa and compare with date from database"""
		
	
		select_cmd=init.dbsession.query(weather.id).filter(weather.m_date<sys_date).count()
		print "there are ",select_cmd, " records with that date. Do you want to delete (y/n)"
		
		while True:
			answer=raw_input()
			if not answer=='y' and not answer=='n':
				continue
			else:
				break
		if answer=='y':
			for record_date in init.dbsession.query(weather).filter(weather.m_date<sys_date):
				init.dbsession.delete(record_date)
				init.dbsession.commit()
				
		else:
			continue
		
		
			
	except KeyboardInterrupt:
		print "you press Ctrl+C"
		init.dbsession.close()
		sys.exit()
