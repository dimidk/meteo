#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine,MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import *
import passwd



"""databaseName='weather.db'"""
tableName='weather'
serialPort='/dev/ttyUSB0'
logDbFile="meteoDatabase_log.txt"
logWebFile="meteoWeb_log.txt"
"""serialPort='/dev/ttyUSB1'"""


dbDict={'user':passwd.userName,'password':passwd.password,'host':passwd.hostName,'database':passwd.databaseName}
dbUrlFormat='mysql+mysqlconnector://{user}:{password}@{host}/{database}'
dbUrl=dbUrlFormat.format(**dbDict)


"""dbUrlFormat='sqlite:///'+databaseName"""

"""try to connect to database return exit code 0 if ok else -1"""

def connectDB():
	exitdb={}
	try:
		engine=create_engine(dbUrl,encoding='utf8',echo=True)
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
	
"""open connection to db"""
meta=MetaData(bind=exitDict['engine'])
Session=scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=exitDict['engine']))
dbsession=Session()



