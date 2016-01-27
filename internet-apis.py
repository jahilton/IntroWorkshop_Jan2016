#urrllib2 is split into different modules on python3 so import would be different
import urllib2
import json

url = 'http://baselayertraining.herokuapp.com/api/states'
data = json.load(urllib2.urlopen(url))

print(data)

print(data['midwest'])

print(data['midwest']['MI'])
