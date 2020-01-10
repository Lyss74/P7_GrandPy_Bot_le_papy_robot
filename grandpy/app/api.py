import requests as req
from pprint import pprint

class ApiWiki:

    def __init__(self):
        pass

    def init_api(self):
        shearch = 'annecy'
        api = "https://fr.wikipedia.org/w/api.php?action=opensearch&search=annecy"
        api2 = "https://fr.wikipedia.org/w/api.php?action=opensearch&search=" + shearch + "&format=json"
        api3 = "https://fr.wikipedia.org/w/api.php?action=help&modules=query"
        config =  {
            "query": {
                "pages": {
                    "217225": {
                        "pageid": 217225,"ns": 0,"title": "Main page"
                    }
                }
            }
        }

        response = req.get(api2, params=config)
        results = response.json()
        #pprint(results)
        #return results

    def test_request(self):
        pass


class ApiHere:
    """
        url_picture = https://developer.here.com/documentation/map-image/dev_guide/topics/quick-start-show-default-location.html
        url_commentary = https://developer.here.com/documentation/map-feedback/dev_guide/topics/quick-start-submit-feedback.html
        url_weather = https://developer.here.com/documentation/weather/dev_guide/topics/request-constructing.html
    """

    def __init__(self):
        self.key = "r3dhXO7hfa6FLN_M1YgrHGkPYNM-pMdLQqJGgg_9aww"
        self.app_id = "kU4vodSxjBgYcdfru1mm"

    def init_api(self):
        search = "lac Annecy"
        url = (f"https://places.sit.ls.hereapi.com/"
               f"places/v1/autosuggest?at=40.74917,-73.98529&q="
               f"{search}&apiKey="
               f"{self.key}")
        response = req.get(url)
        results = response.json()
        pprint(results)

# init = ApiHere()
# test = init.init_api()