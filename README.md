# HatePhp <sub>2.0</sub>



## What's new ?
* The program is now coding in Python 2.7
* Anti-XSS & anti-Sqli (see the exemple included in the git)
* Server with Threading (So stop wasting your time when your restart the server)
* POST & GET Method with function exemple:
	```python
    import random
    
    def getMethod(get):  # If the form's method is get, it calls this function
    	min = get["min"] # from input called min
        max = get["max"] # from input called max
   		nbr = random.randrange(0,11)
        return "<p>Your random number is {}</p>".format(nbr)
        
    def postMethod(post):
    	return "<strong>Oops, I've coded this program only for get method</strong>"
	```
    
