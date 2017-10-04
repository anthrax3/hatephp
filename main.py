import sys

sys.path.insert(0,"./py/")

from hatephp import WebServer

if __name__ == "__main__":
	web = WebServer(8080, "py/index.py","html/404.html")
	web.mainloop()
