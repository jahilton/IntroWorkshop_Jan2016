import urllib2
import json

#print the results - location of all earthquakes more than 2.5 (url dictates 2.5+)
def print_results(data):
	theJSON = json.loads(data)
	#Number of evens
	count = theJSON['metadata']['count']
	print count,'earthquakes'
	#location of events
	for i in theJSON['features']:
		print i['properties']['place']

#print different results - magnitude and location of all earthquakes more than 4.0
def more_results(data):
	print '----------------------------'
	print 'magnitude location'
	magnitude_limit = 4.0
	theJSON = json.loads(data)
	#location of events
	count = 0
	for i in theJSON['features']:
		if i['properties']['mag'] >= magnitude_limit:
			count += 1
			print i['properties']['mag'],i['properties']['place']
	print count,'earthquakes greater than or equal to %d' % magnitude_limit

#connect to the API
def main():
	urlData = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
	webUrl = urllib2.urlopen(urlData)
	data = webUrl.read()
	print_results(data)
	more_results(data)

main()
