import web
import re
import string

render=web.template.render('templates/')
urls=('/','Index',
	  'show','Show')
app=web.application(urls,globals())

"""web.config.db_params={
						'dbn':'MySQL',
						'host':'localhost',
						'user':'rainwise',
						'password':'dd260kt!#',
						'database':'weather'
				}"""

db=web.database(dbn='mysql',db='weather',user='rainwise',pw='dd260kt!#')

		
class Index:
	
	def GET(weather_info):
		id_dict={'id':1}
		
		results=db.query("SELECT COUNT(*) AS total_info FROM weather")
		
		num=int(results[0].total_info)
		
		id_dict['id']=num
		info=db.select('weather', where=id_dict)
		for w in info:
				weather_info=w
				info=weather_info['info']
					
		return render.index(info)
		
"""class foo:
	
	def foo():
		
		s=web.ctx.session
		s.start()
		
		try:
			s.click+=1
		except AttributeError:
			s.click=1
		
		print 'click',s.click
		s.save()"""



if __name__=='__main__':
	app.run()
