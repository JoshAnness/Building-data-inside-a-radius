import requests
import json
import time

api_key = 'Your API Key'

lat='39.19181108038322'
lon='-84.59725660906095'
radius='1000'
region='us'

places = []
params = {}

#https://developers.google.com/maps/documentation/places/web-service/supported_types
type = "street_address"

URL = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+ lat + ',' + lon +'&radius=' + radius + '&region=' + region + '&addresstype=' + type + '&key=' + api_key)
r = requests.get(URL, params = params)
response = json.loads(r.content)
places.extend(response['results'])
time.sleep(1)
while "next_page_token" in response:
    params['pagetoken'] = response['next_page_token'],
    r = requests.get(URL, params = params)
    response = json.loads(r.content)
    places.extend(response['results'])
    time.sleep(1)

addressList = []

for place in places:
    addressList.append(place['name'])

print(addressList)
