#!/usr/bin/python
#-*- coding: utf-8 -*-

from sqlalchemy import create_engine,MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import *


dbUrlFormat='sqlite:///weather.db'

def connectDB():
	exitdb={}
	try:
		engine=create_engine(dbUrlFormat,encoding='utf8',echo=True)
		conn=engine.connect()
		exitdb['engine']=engine
		exitdb['exitcode']=0

	except ProgrammingError:
		print("Database doesn't exist")
		exitdb['engine']=engine
		exitdb['exitcode']=-1

	return exitdb



exitDict=connectDB()
exitStatus=exitDict['exitcode']

if exitStatus==0:
	print "Connected to database"
	engine=exitDict['engine']
	
else:
	print "Problem with Database Connection"
	

meta=MetaData(bind=engine)
Session=scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
dbsession=Session()



