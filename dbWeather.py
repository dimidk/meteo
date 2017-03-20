#!/usr/bin/python
#-*- coding: utf-8 -*-


from sqlalchemy.orm import mapper,sessionmaker
from sqlalchemy import Table,Column, create_engine,MetaData,Integer,String,PrimaryKeyConstraint
from sqlalchemy.exc import *
import init

exitStatus=0

"""read table schema if table exists else exit -1"""
try:
	
	weather_table=Table(init.tableName,init.meta,autoload=True)
	weather_content=[c.name for c in weather_table.columns]
	
	
except:
	exitStatus=-1
	pass
	


"""create table if doesn't exist"""
if (exitStatus==-1):
	
	weather_table=Table(init.tableName,init.meta, 
			Column('id',Integer,primary_key=True),
			Column('info', String(400))
			)
	init.meta.create_all()


class weather(object):
	def __init__(self, id,info):
		self.id=id
		self.info=info
		

"""map class to table"""
mapper(weather,weather_table)



