#!/usr/bin/python
#-*- coding: utf-8 -*-

"""when I use __init__ in class constructor I use mapper
when I use __tablename__ then I don't use mapper"""

from sqlalchemy.orm import mapper,sessionmaker
from sqlalchemy import Table,Column, create_engine,MetaData,Integer,String,PrimaryKeyConstraint
from sqlalchemy.exc import *
from sqlalchemy.ext.declarative import declarative_base
import init


exitStatus=0

Base=declarative_base()
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
			Column('id',Integer,primary_key=True,autoincrement=True),
			Column('m_date',String(10)),
			Column('info', String(400))
			)
	init.meta.create_all()


"""class weather(object):
	def __init__(self, id,info):
		self.id=id
		self.info=info"""
		
class weather(Base):
	__tablename__='weather'
	id=Column(Integer,primary_key=True,autoincrement=True)
	m_date=Column(String(10))
	info=Column(String(400))

"""map class to table
mapper(weather,weather_table)"""



