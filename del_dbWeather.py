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
	
		d=datetime.datetime.now()
		"""take date change to str or vice versa and compare with date from database"""
		
		"""select_cmd=init.dbsession.query(weather.id,weather.info).all()"""
		
		select_cmd=init.dbsession.query(weather).filter(weather.m_date<d.year)
		
		if select_cmd is None
				print "There are no previous days' records"
		else:

			delete_file=weather(m_date<=date_str)
			init.dbsession.delete(delete_file)	
			init.dbsession.commit()	
		
			
	except KeyboardInterrupt:
		print "you press Ctrl+C"
		init.dbsession.close()
		sys.exit()
