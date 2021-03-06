# py-mapzen-whosonfirst-api

Python package for working with the Who's On First API.

## Install

```
sudo pip install -r requirements.txt .
```

## Example

### Simple

```
import mapzen.whosonfirst.api.client

api = mapzen.whosonfirst.api.client.Mapzen("mapzen-XXXXXXX")
print api.execute_method("api.spec.formats", {})

# prints:
# {u'default_format': u'json', u'stat': u'ok', u'formats': [u'json', u'csv', u'meta']}
```

### Fancy

```
import mapzen.whosonfirst.api.client

api = mapzen.whosonfirst.api.client.Mapzen("mapzen-XXXXXXX")

method = "whosonfirst.places.getDescendants"
args = { "id": 85922583, "per_page": 1 }
    
def cb(rsp):

	print rsp
        return True
    
rsp = api.execute_method_paginated(method, args, cb)
```    

### Detailed

_This is basically what's going on under the hood in the `execute_method_paginated` method._

```
import mapzen.whosonfirst.api.client
import parse

api = mapzen.whosonfirst.api.client.Mapzen("mapzen-XXXXXXX")

method = "whosonfirst.places.search"

args = {
	"placetype": "venue",
	"iso": "us",
	"extras": "geom:latitude,geom:longitude,wof:hierarchy,addr:full,addr:housenumber,addr:street,addr:postcode",
	"per_page": 5,
}

writer = None

while True:    

	rsp = api.execute_method(method, args)

	if rsp.get("stat", None) != "ok":
		logging.error("Failed to return ok for '%s'" % args)
		sys.exit(1)
                          
	for row in rsp["places"]:
        
		neighbourhoods = []
		localities = []
		counties = []
		regions = []
        
	for h in row["wof:hierarchy"]:
            
		neighbourhoods.append(str(h.get("neighbourhood_id", -1)))
		localities.append(str(h.get("locality_id", -1)))
		counties.append(str(h.get("county_id", -1)))
		regions.append(str(h.get("region_id", -1)))

		repo = row["wof:repo"].split("-")
		state = repo[-1]
		state = state.upper()
            
		out = {
			"wof:id": row["wof:id"],
			"wof:repo": row["wof:repo"],
			"geom:latitude": row["geom:latitude"],
			"geom:longitude": row["geom:longitude"],
			"addr:full": row["addr:full"],
			"addr:housenumber": row["addr:housenumber"],
			"addr:street": row["addr:street"],
			"addr:postcode": row["addr:postcode"],
			"wof:neightbourhood_id": ";".join(neighbourhoods),
			"wof:locality_id": ";".join(localities),
			"wof:county_id": ";".join(counties),
			"wof:region_id": ";".join(regions),
			"wof:state": state
		}
        
		if not writer:
			fieldnames = out.keys()
			fieldnames.sort()
               
			writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
			writer.writeheader()
            
		writer.writerow(out)

	next_query = rsp.get('next_query', None)

	if not next_query:
		break
            
	tmp = urlparse.parse_qs(next_query)

	for k, v in tmp.items():
		args[k] = v[0]
```

## See also

* https://mapzen.com/documentation/wof/
* https://github.com/whosonfirst/py-flamework-api
