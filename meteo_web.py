#!/usr/bin/python
# -*- coding: UTF-8 -*-


import web
import cgi
import string

render=web.template.render('templates/')
urls=('/','Index')
app=web.application(urls,globals())


db=web.database(dbn='mysql',db='weather',user='rainwise',
	pw='dd260kt!@#',host='10.8.42.10')

		
class Index:
	
	def GET(weather_info):
		id_dict={'id':1}
		
		results=db.query("SELECT COUNT(*) AS total_info FROM weather")
		
		id_dict['id']=int(results[0].total_info)
		rec_num=id_dict['id']
		if rec_num !=0:
			info=db.select('weather', where=id_dict)
			if info is None:
				datetime=1
				timing=1
				temprature=1
				huminity=1
				baro=1
				wind=1
			else:
				for w in info:
					weather_info=w
					info=weather_info['info']
					if info=='':
						datetime=2
						timing=2
						temprature=2
						huminity=2
						baro=2	
						wind=2
					else:
						info_list=info.split(',')
						datetime=info_list[1]
						timing=info_list[2]
						temprature=(5*int(info_list[3]) - 32)/9
						huminity=info_list[4]
						baro=info_list[5]
						wind=info_list[7]
		else:
			datetime=0
			timing=0
			temprature=0
			huminity=0
			baro=0
			wind=0
			

		return render.index(datetime,timing,temprature,huminity,baro,wind)
		

if __name__=='__main__':
	app.run()
	application=app.wsgifunc()
	"""web.httpserver.runsimple(app.wsgifunc(),(None,8888))"""
