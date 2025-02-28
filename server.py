from geocode.geocode import Geocode
import json
from fastapi import FastAPI
import uvicorn

gc = Geocode()
gc.load(recompute=False)
app = FastAPI()


@app.get('/search')
def search_location(q: str):
  locations = gc.decode(q)

  return locations
  # return json.dumps(locations, indent=4)

if __name__ == '__main__':
  uvicorn.run(app, host='0.0.0.0', port=7777)
