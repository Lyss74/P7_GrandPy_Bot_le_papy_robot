import requests as req
from pprint import pprint


class ApiHere:
    """
    """

    def __init__(self):
        # self.api_key = "E5tVPI4PE_8k-DjY6K6mHs2Y8yfXZrLH24wyVKtHfXQ"
        # self.app_id = "kU4vodSxjBgYcdfru1mmkNE6lzYHHhoay8TAm0sC"
        self.app_code = "Ewh4xfXfh7YgUWJ0CcYPEg"
        self.app_id ="pZFDXXi2dxp6lKAgAyg5"

    def search(self, terms_place):
        url = "https://places.cit.api.here.com/places/v1/discover/search"
        params = {
            "at": "0.74917,-0.98529",
            "q": terms_place,
            "app_id": self.app_id,
            "app_code" : self.app_code
        }
        response = req.get(url, params=params)
        results = response.json()
        return results

    def key_tag(self, pos):
        init = self.search(terms_place="lac annecy")
        try:
            results = init['results'][pos]
            title = results['title']
            address = results['vicinity']
            longitude = results['position'][0]
            latitude = results['position'][1]
            key = (
                title + " |",
                address + " |",
                longitude,
                latitude
            )
            return key
        except KeyError:
            self.key_tag(0)

    def picture(self):
        pass

    def weather(self):
        pass

init = ApiHere()
# geoloc = init.search("lac annecy")
# final = init.key_tag(1)
# pprint(geoloc)
# pprint(geoloc)