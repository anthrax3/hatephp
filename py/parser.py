# -*- coding: utf-8 -*-
import sys
import traceback
from byemodule import delete_module as bye

def send(filename,default404):
	try:
		file = open(filename, 'r')
	except IOError:
		file = open(default404, 'r')
	content = file.read()
	file.close()
	return content

def parse(html, data, defaultfile,default404,server):
	datalst = data.split('\n')
	method = datalst[0].split(' ')[0]
	filename = datalst[0].split(' ')[1][1:]
	if(filename == ''):
		filename = defaultfile

	host = datalst[1].split(' ')[1]
	agent = datalst[2].split(' ')[1]
	lang = datalst[3].split(' ')[1].split(',')[0]
	html.send("HTTP/1.1 200 OK\nContent-Type: text/html\n\n")

	if(method == "GET"):
		error = False
		if("?" in filename):
			html.send("<meta charset=\"utf-8\">")
			file = filename.split('?')[0][:-3].split('/')[-1]
			var = filename.split('?')[1].split('&')

			for vari in var:
				todo = vari.split('=')
				server.get[todo[0]] = todo[1]

			try:
				exec("from {} import getMethod".format(file))
			except Exception as e:
				error = True
				html.send("<h1>Verify your source code</h1><pre>{}</pre>".format(str(traceback.format_exc()).replace('\n','<br />')))

			try:
				html.send(getMethod(server))
			except Exception as e:
				if(not error):
					html.send("<h1>Verify your source code</h1><pre>{}</pre>".format(str(traceback.format_exc()).replace('\n','<br />')))
			bye(file)

		else:
			if(".html" in filename):
				file = filename[:-3]
				html.send(send(filename,default404))
			elif(".py" in filename):
				error = False
				file = filename[:-3]
				print(file)
				try:
					exec("from {} import getMethod".format(file.split('/')[-1]))
				except Exception as e:
					error = True
					html.send("<h1>Verify your source code</h1><pre>{}</pre>".format(str(traceback.format_exc()).replace('\n','<br />')))

				try:
					html.send(getMethod(server))
				except Exception as e:
					if(not error):
						html.send("<h1>Verify your source code</h1><pre>{}</pre>".format(str(traceback.format_exc()).replace('\n','<br />')))
				bye(file.split('/')[-1])

		return 0

	if(method == "POST"):
		vari = datalst[13].split('&')
		if vari[0] != '\r':
			post = {}
			for done in vari:
				todo = done.split('=')
				post[todo[0]] = todo[1]

		if len(post) > 0 and ".py" in filename:
			filename = filename.split('/')[-1]
			html.send("<head><meta charset='utf-8'></head>")
			try:
				exec("from {} import postMethod".format(filename[:-3]))
			except Exception as e:
				html.send("<h1>Verify your source code</h1><pre>{}</pre>".format(str(traceback.format_exc()).replace('\n','<br />')))
			try:
				html.send(postMethod(server))

			except Exception as e:
				html.send("<h1>Verify your source code</h1><pre>{}</pre>".format(str(traceback.format_exc()).replace('\n','<br />')))

			bye(filename[:-3])
	return 0
