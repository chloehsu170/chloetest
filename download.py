import requests

print(requests.head('https://pypi.python.org/pypi/selenium').headers['Content-Type'])