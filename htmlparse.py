import os

def post_parse(python, client, data):
    form = {}

    for i in data:
        o = i.split("=")
        print(o)
        o[1] = o[1].replace("+", " ")
        form[o[0]] = o[1]

    script = open(python, "r").read().split("\n")
    for i in script:
        exec(i)

def parse(code, client, filename="index.html"):
    code.remove(code[0])
    send(code, client)

def send(data, client):
    for i in data:
        client.send(i.encode("utf-8"))
