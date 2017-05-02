#!/usr/bin/python
# -*- coding: UTF-8 -*-


import web
import passwd
import string

render=web.template.render('templates/')
urls=('/','Index')
app=web.application(urls,globals())


dbDict={'dbn':passwd.dbn,'db':passwd.databaseName,'user':passwd.userName,'pw':passwd.password,'host':passwd.hostName}

"""db=web.database(dbn='mysql',db='weather',user='rainwise',
	pw='dd260kt!#')"""
	
db=web.database(**dbDict)

		
class Index:
	
	def GET(weather_info):
		id_dict={'id':1}
		
		results=db.query("SELECT COUNT(*) AS total_info FROM weather")
		
		id_dict['id']=int(results[0].total_info)
		rec_num=id_dict['id']
		if rec_num !=0:

			info=db.select('weather', where=rec_num)
			
			for w in info:
				weather_info=w
				info=weather_info['info']
				if info=='':
					datetime=''
					timing=''
					temprature=''
					huminity=''
					baro=''
					wind=''
					
				else:
					info_list=info.split(',')
					datetime=info_list[1]
					timing=info_list[2]
					temprature=(5*int(info_list[3]) - 32)/9
					huminity=info_list[4]
					baro=info_list[5]
					wind=info_list[7]
					x=render.index(datetime,timing,temprature,huminity,baro,wind)

		else:
			datetime=''
			timing=''
			temprature=''
			huminity=''
			baro=''
			wind=''
			
			

		return render.index(datetime,timing,temprature,huminity,baro,wind)
		
		

if __name__=='__main__':
	app.run()
	application=app.wsgifunc()
	"""web.httpserver.runsimple(app.wsgifunc(),(None,8888))"""
