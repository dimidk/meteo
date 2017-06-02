#!/usr/bin/python
# -*- coding: UTF-8 -*-


import web
import passwd
import string
import datetime

render=web.template.render('templates/')
urls=('/','Index')
app=web.application(urls,globals())


dbDict={'dbn':passwd.dbn,'db':passwd.databaseName,'user':passwd.userName,'pw':passwd.password, 'host':passwd.hostName}


"""not the best way"""
db=web.database(dbn=passwd.dbn,db=passwd.databaseName,user=passwd.userName,pw=passwd.password,host=passwd.hostName)

"""db=web.database(**dbDict)"""

		
class Index:
	
	def GET(weather_info):
		id_dict={'id':1}
		
		results=db.query("SELECT COUNT(*) AS total_info FROM weather")
		
		id_dict['id']=int(results[0].total_info)
		rec_num=id_dict['id']
		date_str=datetime.datetime.now()
		if date_str.month<10:
			timedate='0'+str(date_str.month)+'/'+str(date_str.day)
		else:
			timedate=str(date_str.month)+'/'+str(date_str.day)
		if rec_num !=0:

			info=db.select('weather', where=rec_num)
			
			for w in info:
				weather_info=w
				info=weather_info['info']
				timedate=weather_info['m_date']
				if info=='':
					"""datetime=''"""
					timing=''
					temprature=''
					huminity=''
					baro=''
					wind=''

				else:
					
					info_list=info.split(',')
					"""datetime=info_list[1]"""
					timing,huminity,baro,wind=info_list[1],info_list[3],info_list[4],info_list[6]
					temprature=(5*int(info_list[2]) - 32)/9
					"""timing=info_list[1]
					temprature=(5*int(info_list[2]) - 32)/9
					huminity=info_list[3]
					baro=info_list[4]
					wind=info_list[6]"""
					x=render.index(timedate,timing,temprature,huminity,baro,wind)

		"""else:
			datetime=''
			timing=''
			temprature=''
			huminity=''
			baro=''
			wind=''"""

		return render.index(timedate,timing,temprature,huminity,baro,wind)
		
		

if __name__=='__main__':
	app.run()
	application=app.wsgifunc()
	"""web.httpserver.runsimple(app.wsgifunc(),(None,8888))"""
