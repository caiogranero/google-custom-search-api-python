# google-custom-search-api-python

### Install Google API

```
$ pip install --upgrade google-api-python-client
```

### The Code

```
import pprint, json

from googleapiclient.discovery import build

def main():
  service = build("customsearch", "v1",
            developerKey="PUT YOUR API KEY HERE")

  res = service.cse().list(
      q='Brasil', #Search words
      cx='PUT YOUR CSE KEY HERE',  #CSE Key
      lr='lang_pt', #Search language
    ).execute()
  pprint.pprint(res)

  with open('output.txt', 'w') as outfile:
    json.dump(res, outfile)

main()

```