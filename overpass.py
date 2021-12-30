import requests
import json

params = []
output = []

overpass = "http://overpass-api.de/api/interpreter"
query = """
[out:json];
{{radius=1000}}
(
  node["addr:housenumber"](around:{{radius}},{{geocodeCoords:5520 Chevrolet Blvd, Parma, OH 44130}});
  way["addr:housenumber"](around:{{radius}},{{geocodeCoords:5520 Chevrolet Blvd, Parma, OH 44130}});
  relation["addr:housenumber"](around:{{radius}},{{geocodeCoords:5520 Chevrolet Blvd, Parma, OH 44130}});
);
out body;
>;
out skel qt;
"""

url = overpass + "?data=" + query

r = requests.get(url, params = params)
response = json.loads(r.content)

print(response)
