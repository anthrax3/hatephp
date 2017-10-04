# HatePhp <sub>2.1</sub>

## What's new ?
* Now, you can call a python file as the index file (index.py)
* Support all ports (great when you don't have enough access to the 80 ports)
* The session variable has been added
* The project is more structured (./py and ./html folder)
* Custom 404 filenames
* Get and post var has been improuved:

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

## Old news:
### HatePHP <sup>2.0</sub>
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
