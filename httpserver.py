#-*- coding : utf-8 -*-

import socket
from htmlparse import *

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("", 80))

socket.listen(10)

while True:
	client, info = socket.accept()
	msg = client.recv(1024).decode("utf-8")
	if "GET" in msg:
		method = msg.split("\n")[0].split(" ")
		if method[1] == "/":
			file = open("index.html", "r")
			parse(file.read().split("\n"), client)
		elif method[1] == "/favicon.ico":
			continue
		else:
			file = open(method[1][1:], "r")
			parse(file.read().split("\n"), client, method[1][1:])
	elif "POST" in msg:
		filename = msg.split("\n")[0].split(" ")[1][1:]
		data = msg.split("\n")[14:]
		post_parse(filename, client, data)
