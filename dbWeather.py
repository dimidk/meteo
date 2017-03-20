#!/usr/bin/python
#-*- coding: utf-8 -*-


from sqlalchemy.orm import mapper,sessionmaker
from sqlalchemy import Table,Column, create_engine,MetaData,Integer,String,PrimaryKeyConstraint
from sqlalchemy.exc import *
import init

exitStatus=0

try:
	
	weather_table=Table('weather',init.meta,autoload=True)
	weather_content=[c.name for c in weather_table.columns]
	"""for c in weather_content:
		print c"""
	
	
except:
	exitStatus=-1
	pass
	
print "exit code is: ",exitStatus


if (exitStatus==-1):
	
	weather_table=Table('weather',init.meta, 
			Column('id',Integer,primary_key=True),
			Column('info', String(400))
			)
	init.meta.create_all()


class weather(object):
	def __init__(self, id,info):
		self.id=id
		self.info=info
		

mapper(weather,weather_table)



