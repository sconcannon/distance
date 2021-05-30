import urllib.request
import json

# My distance matrix API key is []
#
try:
    res = urllib.request.urlopen("https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=Rockville+MD&destinations=baltimore+md&key=[add key]").read()
except:
    print("The API call failed")

data = json.loads(res.decode())
print(data)
print(data["rows"][0]["elements"][0]["distance"])
print(data["rows"][0]["elements"][0]["distance"]["value"])
# {'text': '127 mi', 'value': 204914}
