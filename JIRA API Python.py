# import needed libraries
import requests, json, datetime, time
from bs4 import BeautifulSoup
from pprint import pprint
from http.client import responses


def logStory(szSummary, szDescription, prjName):

	# input header and message for api
	header = {'Content-Type': 'application/json'}
	message = {"fields":{"project":{"key": prjName}, "summary":szSummary, "description":szDescription, "issuetype": {"name":"Story"}}}
	
	# this is used to put var message in Atlassian
	r = requests.post(toUrl, data=json.dumps(message), auth=loginCred, headers=header)

	# get and tell response code
	print (r.status_code)
	print (responses[r.status_code])

	# pretty prints content of server response
	#pprint(r.json())
	
	return;

def logComment(comment):

	# input header and message for api
	header = {'Content-Type': 'application/json'}
	message = {"body": comment}
	
	# this is used to put var message in Atlassian
	r = requests.post(commentUrl, data=json.dumps(message), auth=loginCred, headers=header)

	return;

def networkTest(fromUrl):
	
	#get HTML data from from initial website
	firstGet = requests.get(fromUrl, auth=('user', 'pass'))

	#Get timestamp after first request
	firstTime = datetime.datetime.now()
	
	#get HTML data from website for second time
	secGet = requests.get(fromUrl, auth=('user', 'pass'))

	#Get Timestamp immediately after second request
	secTime = datetime.datetime.now()

	#assign pages of website to variables
	soup1=BeautifulSoup(firstGet.content, 'html.parser')
	webText1=soup1.find(id="news")
	
	soup2=BeautifulSoup(secGet.content, 'html.parser')
	webText2=soup2.find(id="news")

	#Compare times to see response speed
	timeDelta = (secTime-firstTime).total_seconds()

	#adds time text for later comment in JIRA
	if timeDelta<1:
		warning = "with less than a 1 second response time. ("
	elif timeDelta>1:
		warning = "with greater than a 1 second response time. ("
	else:
		warning = "didn't work, "
		pass
		
	#compare website to itself, see if content is different?
	#place holder for website comparison after loop
	global oldGet
	
	if webText2 != oldGet and timeDelta>1:
		logStory(warning, warning, projectName)
		time.sleep(5)
		
	elif webText2 != oldGet:
		commentString= "New content added " + warning + str(timeDelta) + " seconds)"
		logComment(commentString)
		oldGet = webText2
		time.sleep(5)
	
	else:
		while webText2==oldGet:
			print("No change in website")
			time.sleep(5)
			if webText2 != oldGet:
				break
	
	return;


#Pass in vars/data for func logStory
user=input("Input Atlassian Cloud Username - ")
toUrl = "https://"+str(user)+".atlassian.net/rest/api/2/issue/"

password=input("Input Atlassian Cloud Password - ")
loginCred  =(str(user), str(password))

url=input("Input Test Website URL")
fromUrl = str(url)

summary=input("Input summary for Atlassian Cloud issue - ")
mySummary = str(summary)

desc=input("Input description for Atlassian Cloud issue - ")
myDesc = str(desc)


projectName = "TEST"

#Data for func logComment
commentNum = 10006
commentUrl = "https://user.atlassian.net/rest/api/2/issue/"+str(commentNum)+"/comment"

#data for func networkTest
oldGet = "placeholder"

while True:
	networkTest(fromUrl)
