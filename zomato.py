import requests
import json
from pprint import pprint

class Zomato:
    '''
    Constructor for the Zomato class.

    Parameters:
        key                    - Zomato API Key.
                             Get it from http://www.zomato.com/api/key
        base_url (optional)    - base URL to be used for making API calls.
                             Defaults to https://developers.zomato.com/api/v2.1/
    '''
    def __init__(self, key, base_url='https://developers.zomato.com/api/v2.1/'):
        self.key = key
        self.base_url = base_url

    def json_parse(self):
        json_data = json.loads(self.response)

        return json_data
    
    def getCategories(self):
        URL = self.base_url + "categories"
        header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": self.key}

        response = requests.get(URL, headers=header)
        #pprint(response.json())
        return response.json()
        
    def getCategories(self, q, lat, lon, city_ids, count):
        city_ids = city_ids.split(",")
        for id in city_ids:
            id = id.strip()
        city_ids = "%2C".join(city_ids)
        URL = [self.base_url, "cities?", "q=", q, "&lat=", str(lat), "&lon=", str(lon), "&city_ids=", city_ids, "&count=", str(count)]
        URL = "".join(URL)
        header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": self.key}

        response = requests.get(URL, headers=header)
        #pprint(response.json())
        return response.json()
    
    def getCollections(self, city_id, lat, lon, count):
        URL = [self.base_url, "collections?", "city_id=", str(city_id), "&lat=", str(lat), "&lon=", str(lon), "&count=", str(count)]
        URL = "".join(URL)
        header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": self.key}

        response = requests.get(URL, headers=header)
        #pprint(response.json())
        return response.json()

    def getCuisines(self, city_id, lat, lon):
        URL = [self.base_url, "cuisines?", "city_id=", str(city_id), "&lat=", str(lat), "&lon=", str(lon)]
        URL = "".join(URL)
        header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": self.key}

        response = requests.get(URL, headers=header)
        #pprint(response.json())
        return response.json()
    
    def getEstablishments(self, city_id, lat, lon):
        URL = [self.base_url, "establishments?", "city_id=", str(city_id), "&lat=", str(lat), "&lon=", str(lon)]
        URL = "".join(URL)
        header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": self.key}

        response = requests.get(URL, headers=header)
        #pprint(response.json())
        return response.json()

    def getGeocode(self, lat, lon):
        URL = [self.base_url, "geocode?", "&lat=", str(lat), "&lon=", str(lon)]
        URL = "".join(URL)
        header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": self.key}

        response = requests.get(URL, headers=header)
        #pprint(response.json())
        return response.json()
        



