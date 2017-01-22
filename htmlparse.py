#-*- coding : utf-8 -*-
#!/usr/bin/env python3

def post_parse(python, client, data):
    form = {}
    for i in data:
        o = i.split("=")
        o[1] = o[1].replace("+", " ")
        form[o[0]] = o[1]

    script = open(python, "r").read().split("\n")
    for i in script:
        exec(i)
    client.close()

def parse(code, client, filename="index.html"):
    send(code, client)
    client.close()

def find_data(msg):
    suivant = False
    data = []
    print(msg.encode("utf-8"))
    for ligne in msg.split("\n"):
        if ligne == "\r":
            suivant = True
        if suivant and ligne != "\r":
            data.append(ligne)

    return data

def send(data, client):
    for i in data:
        client.send(i.encode("utf-8"))
