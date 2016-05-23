# For more info: https://developers.google.com/resources/api-libraries/documentation/customsearch/v1/python/latest/customsearch_v1.cse.html#list
# To get yours Google APIs Key, enter: <http://code.google.com/apis/console>
# To get your Custom Search Engine Key, enter <https://cse.google.com/cse/all>

__author__ = 'Caio Granero'

import json

from googleapiclient.discovery import build

def main():
  service = build("customsearch", "v1",
            developerKey="PUT YOUR API KEY HERE")

  res = service.cse().list(
      q='Brasil', #Search words
      cx='PUT YOUR CSE KEY HERE',  #CSE Key
      lr='lang_pt', #Search language
    ).execute()

  with open('output.json', 'w') as outfile:
    json.dump(res, outfile)

main()