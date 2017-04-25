# For more info: https://developers.google.com/resources/api-libraries/documentation/customsearch/v1/python/latest/customsearch_v1.cse.html#list
# To get yours Google APIs Key, enter: <http://code.google.com/apis/console>
# To get your Custom Search Engine Key, enter <https://cse.google.com/cse/all>

__author__ = 'Caio Granero'

import json

from googleapiclient.discovery import build

def getService():
    service = build("customsearch", "v1",
            developerKey="AIzaSyDxpJfGwM9KzeTFlKa-_Z-wEgI1sKMcKKo")

    return service

def main():

    pageLimit = 4
    service = getService()
    startIndex = 1
    response = []

    for nPage in range(0, pageLimit):
        print "Reading page number:",nPage+1

        response.append(service.cse().list(
            q='Temer Golpista', #Search words
            cx='001132580745589424302:jbscnf14_dw',  #CSE Key
            lr='lang_pt', #Search language
            start=startIndex
        ).execute())

        startIndex = response[nPage].get("queries").get("nextPage")[0].get("startIndex")

    with open('data.json', 'w') as outfile:
        json.dump(response, outfile)

main()
