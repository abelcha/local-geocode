from geocode.geocode import Geocode
import json
import logging
import json
from fastapi import FastAPI
import uvicorn
import sys
import re

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

gc = Geocode()
gc.load(recompute=False)
app = FastAPI()

with open('geocode/communes.fr.json', 'r') as file:
  zipcodes = json.load(file)
  
print("lolz")

@app.get('/search')
def search_location(q: str):

  locations = gc.decode(q)

  return locations
  # return json.dumps(locations, indent=4)
@app.get('/geocode')
def geocode_location(q: str):
  if qz := re.search(r'\b\d{5}\b', q):
    zip = qz.group(0)
    if zip in zipcodes:
      json.dumps(zipcodes[zip], indent=4)
      return (zipcodes[zip].get('lat'), zipcodes[zip].get('lng'), zipcodes[zip].get('city'))
    
  props = gc.decode(q)
  props = [p for p in props if p.get('location_type') != 'country']
  if props:
    return (props[0].get('latitude'), props[0].get('longitude'), props[0].get('name'))
  return (None, None, None)
if __name__ == '__main__':
  # args includes --search
  if '--geocode' in sys.argv:
    print(geocode_location(sys.argv.pop()))
  else:
    uvicorn.run(app, host='0.0.0.0', port=7777, log_level='info')

