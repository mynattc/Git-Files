import requests, json
from http.client import responses
from pprint import pprint

def getAir(specUrl):
	
	print (specUrl)
	# this is used to put var message in Atlassian
	r = requests.get(specUrl)

	# get and tell response code
	print (r.status_code)
	print (responses[r.status_code])

	# pretty prints content of server response
	pprint(r.json())
	
	return;
	
#Returns a listing of all airlines, including those that are not currently active
allAirUrl ="https://api.flightstats.com/flex/airlines/rest/v1/json/all?appId=0b6c6a2b&appKey=12a28bffdd08a58fc394d52db5b901a8"

#Returns DelayIndexes for airports in the given Country
airDelayUrl = "https://api.flightstats.com/flex/delayindex/rest/v1/json/country/US?appId=0b6c6a2b&appKey=12a28bffdd08a58fc394d52db5b901a8&classification=1&score=3"

#Call function with a given url
getAir(airDelayUrl)
