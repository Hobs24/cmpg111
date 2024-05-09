#using API(Application programming interface)
#Use the request package from pip to communicate with API's
import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2)) #json() insures that the data that you get back is formmatted in json

