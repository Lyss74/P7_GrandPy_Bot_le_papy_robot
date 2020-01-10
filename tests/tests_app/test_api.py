from grandpy.app.api import ApiWiki, ApiHere


class TestApiWikipedia:

    def test_http_result_wiki_api(self): #Add moock the test
        init = ApiWiki()
        pass


class TestApiHere:

    def test_init_the_here_api(self, monkeypatch):  # Add moock the test
        init = ApiHere()
        results = {'results':[{
             "title": str,
             "position": [int]
         }]}
        def mockreturn():
            return results
        monkeypatch.setattr(init.init_api(), 'requests', mockreturn)
        assert init.init_api() == results

    def test_format_tags(self):
        name = []
        position = []
        address = []
        pass

    def test_position_search(self):
        init = ApiHere()
        position =[]
    #assert init.position_check() == list
        pass


