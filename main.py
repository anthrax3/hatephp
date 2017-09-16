import sys
from hatephp import WebServer


if __name__ == "__main__":
	web = WebServer(80, "index.html")
	web.mainloop()