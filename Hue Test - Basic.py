import requests
import json

from http.client import HTTPConnection 


bulb=input("Which lightbulb? (From 1-3): ")
color=input("What color? (From 0 to 65535): ")
bright=input("How bright? (From 1-254): ")

message_body = json.dumps({"hue":int(color), "bri":int(bright)})
web = HTTPConnection('192.168.0.101')
web.request('PUT', '/api/"key"/lights/'+bulb+'/state', message_body)
response = web.getresponse().read()

print(json.loads(response))
