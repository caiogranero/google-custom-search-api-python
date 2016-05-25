# For more info: https://developers.google.com/resources/api-libraries/documentation/customsearch/v1/python/latest/customsearch_v1.cse.html#list
# To get yours Google APIs Key, enter: <http://code.google.com/apis/console>
# To get your Custom Search Engine Key, enter <https://cse.google.com/cse/all>

__author__ = 'Caio Granero'

import json

from googleapiclient.discovery import build

def main():
  service = build("customsearch", "v1",
            developerKey="AIzaSyDxpJfGwM9KzeTFlKa-_Z-wEgI1sKMcKKo")

  res = service.cse().list(
      q='IT4Biz', #Search words
      cx='001132580745589424302:jbscnf14_dw',  #CSE Key
      lr='lang_pt', #Search language
    ).execute()

  with open('data.json', 'w') as outfile:
    json.dump(res, outfile)

main()