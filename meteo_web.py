#!/usr/bin/python
# -*- coding: UTF-8 -*-


import web
import passwd
import string
import datetime
import passwd

render=web.template.render('templates/')
urls=('/','Index')
app=web.application(urls,globals())
try:
	fp=open(passwd.logWebFile,'a+')
except:
	print "open file error"


dbDict={'dbn':passwd.dbn,'db':passwd.databaseName,'user':passwd.userName,'pw':passwd.password, 'host':passwd.hostName}
fp.write('connect to database\n')

"""not the best way"""
db=web.database(dbn=passwd.dbn,db=passwd.databaseName,user=passwd.userName,pw=passwd.password,host=passwd.hostName)

"""db=web.database(**dbDict)
because of deletion records in database the id may differ from total number of records, thus not id=rec_num"""

		
class Index:
	
	def GET(weather_info):
		id_dict={'id':1}
		
		"""results=db.query("SELECT COUNT(*) AS total_info FROM weather")"""
		results=db.query("SELECT max(id) as total_info from weather")
		id_dict['id']=int(results[0].total_info)
		rec_num=id_dict['id']
		fp.write("max record in database "+str(rec_num)+'\n')
		
		date_str=datetime.datetime.now()
		cur_timing=str(date_str.hour)+":"+str(date_str.minute)+":"+str(date_str.second)
		
		if date_str.month<10:
			cur_date='0'+str(date_str.month)+'/'+str(date_str.day)
		else:
			cur_date=str(date_str.month)+'/'+str(date_str.day)
			
		if rec_num ==0:
			
			temprature,huminity,baro,wind='','','','',''
	
		else:			

			info=db.select('weather', where=rec_num)
			fp.write("query database the last information about weather\n")
			
			for w in info:
				weather_info=w
				info=weather_info['info']
				timedate=weather_info['m_date']
				
				fp.write(info+" "+timedate+'\n')
				
				if info=='':

					temprature,huminity,baro,wind='','','','',''

				else:
					
					info_list=info.split(',')
				
					if len(info_list)>1:
						timing=info_list[1]
						huminity,baro,wind=info_list[3],info_list[4],info_list[6]
						temprature=(5*int(info_list[2]) - 32)/9
					else:
						temprature,huminity,baro,wind='','','',''
						"""timing=info_list[1]
					temprature=(5*int(info_list[2]) - 32)/9
					huminity=info_list[3]
					baro=info_list[4]
					wind=info_list[6]"""
					
					x=render.index(timedate,timing,temprature,huminity,baro,wind,cur_date,cur_timing)
					fp.write("return last info\n")

		"""fp.close()"""
		return render.index(timedate,timing,temprature,huminity,baro,wind,cur_date,cur_timing)
		
		

if __name__=='__main__':

	app.run()
	application=app.wsgifunc()
	fp.close()
	"""web.httpserver.runsimple(app.wsgifunc(),(None,8888))"""
