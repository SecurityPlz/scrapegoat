import fileinput
import json
import tldextract
import re

# create lists for data storage
twitterList = []
finalList = []

# Getting input from pipe or redirect
with fileinput.input() as f_input:
    # seperating json objects 
    for jsonObj in f_input:
        # create individual json dictionary objects
        twitterDict = json.loads(jsonObj)
        # append json objects to list
        twitterList.append(twitterDict)
# iterate through all json objects
for tweet in twitterList:
        # concatenate JSON field(s) to string content for tweet body
	jsonToStr=''.join(tweet["content"])
	#find links in tweets
	reMatch = str(re.search("https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$", jsonToStr))
	print(reMatch)
	# tldextract.extract(reMatch)
	# match to list links and fails per line
	# for link in reMatch:
		# Build list from re output
		# finalList.append(reMatch)
	# def convert(finalList):
		# return tuple(i for i in finalList)
		# finalList = list(dict.fromkeys(finalList))
		# print(finalList)
		# print(finalList["match"])
		# tldextract.extract(reMatch)
		# print(reMatch)
        
