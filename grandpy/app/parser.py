import re

class Parser:

    def __init__(self, question):
        self.question = question

    def to_lower(self):
        self.question = self.question.lower()

    def clean_accent(self):
        self.question = (self.question
                         .replace("é", "e")
                         .replace("è", "e")
                         .replace("ê", "e")
                         .replace("à", "a")
                         .replace("â", "a")
                         .replace("î", "i")
                         .replace("ï", "i")
                         .replace("ô", "o")
                         .replace("ö", "o")
                         .replace("û", "u")
                         .replace("ü", "u")
                         .replace("ù", "u")
                         )

    def clean_ponctuation(self):
        self.question = (self.question
                         .replace("'", " ")
                         .replace(";", " ")
                         )

    def extract_the_place(self):
        # self.question = "Trouve-moi l'adresse du lac d'Annecy"
        regex_place = r"(l'adresse |" \
                r" ou se trouve |" \
                r" ou se situe |" \
                r" trouve moi |" \
                r" ou est |" \
                r" quel est |" \
                r" quel endroit)" \
                r"(?P<lieu>[^,;:!?.]+)"
        match = re.match(regex_place, self.question)
        phrasing_clean = match.group("lieu")
        stop_words = {"le", "la", "les", "de", "des", "du"}
        words = []
        for word in phrasing_clean.split():
            if word not in stop_words:
                words.append(word)
                return " ".join(words)

    def extract_the_monument(self):
        regex_monument = r"(place |" \
                r" tour |" \
                r" pont |" \
                r" cathedrale |" \
                r" eglise |" \
                r" quel est |" \
                r" monument)" \
                r"(?P<monument>[^,;:!?.]+)"
        pass
