# today we will be learning about virtual enviroments
# Buckle up!

# api = Application Programming Interface
#
# we are going to use the requests library

# let's make a virtual enviroment!
import requests

data = requests.get('https://www.google.com')
print(data.status_code)
print(data.text)
