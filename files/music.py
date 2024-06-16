#using API(Application programming interface)
#Use the request package from pip to communicate with API's
import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=25&term=" + sys.argv[1])

#get the items from the trackName from any band or artists
o = response.json()
for result in o["results"]:
    print(result["trackName"])