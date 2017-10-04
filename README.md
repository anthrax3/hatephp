# HatePhp <sub>2.0</sub>

## HatePhp <sub>2.1</sub>
* Session variable has been added
* The server can now open python file without inputs (you can make a file index.js)
* You can use the server with custom port
* Server variable structure

```python
	import random

	def getMethod(server):  # If the form's method is get, it calls this function
	min = server.get["min"] # from input called min
	max = server.get["max"] # from input called max
	nbr = random.randrange(min,max)
				return "<p>Your random number is {}</p>".format(nbr)

	def postMethod(server):
		return "<strong>Oops, I've coded this program only for get method</strong>"
```


## Old news ?
### HatePhp <sub>2.0</sub>
* The program is now coding in Python 2.7
* Anti-XSS & anti-Sqli (see the exemple included in the git)
* Server with Threading (So stop wasting your time when your restart the server)
* POST & GET Method with function exemple:
	```python
    import random

    def getMethod(get):  # If the form's method is get, it calls this function
 		min = get["min"] # from input called min
		max = get["max"] # from input called max
   	nbr = random.randrange(min,max)
        	return "<p>Your random number is {}</p>".format(nbr)

    def postMethod(post):
    	return "<strong>Oops, I've coded this program only for get method</strong>"
	```
