from grandpy.app.api_here import ApiHere

import requests as req

from pprint import pprint

"""
    https://www.mediawiki.org/wiki/API:Geosearch
    https://fr.wikipedia.org/w/api.php? action=query &prop=coordinates &titles=Wikimedia%20Foundation
    def __init__(self, place):
        '''
        initialize an instance
        '''
        def get_wikiurl(place_searched):
            blablabla
            # retourne un dic
        
        self.place = place
        self.pageid = str(get_wikiurl(place).get('pageid'))
        self.url = "https://fr.wikipedia.org/w/index.php?curid=" + self.pageid
        self.title = get_wikiurl(place)['title']
"""

class ApiWiki:

    def __init__(self):
        self.url = "https://fr.wikipedia.org/w/api.php"

    def search_geoloc(self):
        params = {
                "action": "query",
                "list": "geosearch",
                "gscoord": "45.89843|6.12914",
                "gsradius": 1000,
                "gslimit": 50,
                "format": "json"
        }
        response = req.get(self.url, params=params)
        results = response.json()
        return results['query']['geosearch'][1]['pageid']

    def search_content(self):
        title = ""
        url = "https://fr.wikipedia.org/w/api.php"
        extract_text = {
            "action" : "query",
            "pageids" : self.search_geoloc(),
            "prop" : "extracts",
            "exsectionformat" : "wiki",
            "explaintext" : True,
            "format": "json",
        }
        response = req.get(url, params=extract_text)
        results = response.json()
        return results['query']['pages']

init = ApiWiki()
pprint(init.search_content())


