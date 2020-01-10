from grandpy.app.parser import Parser

class TestParser:

    def test_to_lower(self):
        parser = Parser(question="abcd")
        parser.to_lower()
        assert parser.question == parser.question.lower()

    def test_remove_the_accent(self):
        parser = Parser(question="éèêàâîïôöûüù")
        parser.clean_accent()
        assert parser.question == "eeeaaiioouuu"

    def test_remove_the_ponctuation(self):
        parser = Parser(question="'")
        parser.clean_ponctuation()
        assert parser.question == " "

