# -*- coding: utf-8 -*-
import sys
import traceback
from byemodule import delete_module as bye

def send(filename):
	try:
		file = open(filename, 'r')
	except IOError:
		file = open('404.html', 'r')
	content = file.read()
	file.close()
	return content

def parse(html, data, post):
	datalst = data.split('\n')
	method = datalst[0].split(' ')[0]
	filename = datalst[0].split(' ')[1][1:]
	if(filename == ''):
		filename = 'index.html'
	
	host = datalst[1].split(' ')[1]
	agent = datalst[2].split(' ')[1]
	lang = datalst[3].split(' ')[1].split(',')[0]


	if(method == "GET"):
		if(".py" in filename):
			if("?" in filename):
				file = filename.split('?')[0][:-3]
				var = filename.split('?')[1].split('&')
			else:
				file = filename[:-3]

			get = {}
			for vari in var:
				todo = vari.split('=')
				get[todo[0]] = todo[1]

			exec("from {} import getMethod".format(file))
			html.send("<head><meta charset='utf-8'></head>")
			html.send(getMethod(get))
			bye(file)
		else:
			html.send(send(filename))

	if(method == "POST"):
		vari = datalst[13].split('&')
		if vari[0] != '\r':
			post = {}
			for done in vari:
				todo = done.split('=')
				post[todo[0]] = todo[1]
		
		if len(post) > 0 and ".py" in filename:
			html.send("<head><meta charset='utf-8'></head>")
			try:
				exec("from {} import postMethod".format(filename[:-3]))
			except Exception as e:
				html.send("<h1>Verify your source code</h1><pre>{}</pre>".format(str(traceback.format_exc()).replace('\n','<br />')))	
			try:
				html.send(postMethod(post))
			
			except Exception as e:
				html.send("<h1>Verify your source code</h1><pre>{}</pre>".format(str(traceback.format_exc()).replace('\n','<br />')))

			bye(filename[:-3])
		return post