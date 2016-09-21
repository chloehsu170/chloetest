import requests

print(requests.head('http://apache.fayea.com/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz').headers['Content-Type'])
print(requests.head('http://pypi.python.org/pypi/selenium/selenium-3.0.0b3.tar.gz').header['Content-Type'])