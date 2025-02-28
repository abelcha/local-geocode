# from geocode.geocode import Geocode
import json
# from fastapi import FastAPI
import pickle
from sys import argv
# import uvicorn 


class LocalGeocode():
    def __init__(self):
        self.geo_data_field_names = ['name', 'official_name', 'country_code', 'longitude', 'latitude', 'geoname_id', 'location_type', 'population']
        # self.default_location_types = ['city', 'place', 'country', 'admin1', 'admin2', 'admin3', 'admin4', 'admin5', 'admin6', 'admin_other', 'continent', 'region']

    def get_geonames_pickle(self):
        with open("geonames.pkl", 'rb') as f:
            df = pickle.load(f)
        return df

    def get_keyword_processor_pickle(self):
        with open("keyword_processor.pkl", 'rb') as f:
           kp = pickle.load(f)
           pickle
        return kp
    
    def load(self, recompute=False):
        self.kp = self.get_keyword_processor_pickle()
        self.geo_data = self.get_geonames_pickle()

    def decode(self, input_text):
        matches = self.kp.extract_keywords(input_text)
        if len(matches) == 0:
            return []
        # sort by priorities
        matches = sorted(list(set(int(m) for m in matches)))
        return [dict(zip(self.geo_data_field_names, self.geo_data[m])) for m in matches]


app = FastAPI()

@app.get('/search')
def search_location(q: str):
  locations = lc.decode(q)

  return locations
  # return json.dumps(locations, indent=4)

if __name__ == '__main__':
  uvicorn.run(app, host='0.0.0.0', port=7878)
