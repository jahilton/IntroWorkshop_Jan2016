#urllib2 is split into different modules in python3
import urllib2
from urlparse import urlparse

response = urllib2.urlopen('http://stanford.edu')

print('Response from:',response.geturl())
print('Response from hostname:',urlparse(response.geturl()).hostname)
print('Status code:',response.getcode())

with open('response.html','w') as f:
	f.write(response.read())

f.close()
