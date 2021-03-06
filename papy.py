import json
from random import choice

from maps import MapsApi
from wiki import WikiApi
from myparser import Parser


class Papy:

    def __init__(self, question):
        self.question = question
        self.errors = []
        self.error_message = None

    def cogitation(self):
        """ Papy will fill the following fields :
            - palce
            - location
            - maps
            - wiki """

        parser = Parser(self.question)
        self.place = parser.get_place()

        if self.place:
            maps_api = MapsApi(self.place)
            wiki_api = WikiApi(self.place)

            self.location = maps_api.get_location()
            self.wiki = wiki_api.get_wiki()

            if not self.location:
                self.errors.append("NO_LOCATION")

            if not self.wiki:
                self.errors.append("NO_WIKI")

        else:
            self.errors.append("BAD_QUESTION")

            self.location = None
            self.wiki = [None, None]


    def get_response(self):
        """ Papy will answer with a complete json. """

        response = {
            'question': self.question,
            'place': self.place,
            'location': self.location,
            'wiki': self.wiki[0],
            'wiki_link': self.wiki[1],
            'hello': self.get_hello(),
            'introduction_maps': self.get_introduction_maps(),
            'introduction_wiki': self.get_introduction_wiki(),
            'bye': self.get_bye(),
            'errors': self.errors,
            'error_message': self.error_message,
        }

        return response


    def get_response_dict(self):

        self.cogitation()

        if len(self.errors) > 0:
            for error in self.errors:
                if error == 'BAD_QUESTION':
                    self.error_message = self.get_bad_question_message()
        else:
            self.errors = None

        return self.get_response()


    def get_hello(self):
        """ Papy will say hello with a random sentence. """

        hello = [
            "Salut !",
            "Bonjour fistion...",
            "Quelle joie de te revoir !",
            "Salut la jeunesse !",
        ]

        return choice(hello)


    def get_introduction_maps(self):
        """ Papy will introduce the maps with a random sentence. """

        introduction = [
            "Je me rappel cet endroit...",
            "J'y allais faire mon footing autrefois !",
            "Laisse-moi te chercher ma carte... Ah ! Voilà ! Elle est là...",
            "Penses-tu pouvoir retrouver cet endroit ?",
        ]

        return choice(introduction)


    def get_introduction_wiki(self):
        """ Papy will introduce the wiki with a random sentence. """

        introduction = [
            "Connais-tu l'histoire de ce lieu ?",
            "J'ai une anecdote assez insolite à te raconter...",
            "J'ai, à propos de cet endroit, un belle histoire à te compter...",
            "D'ailleurs, j'ai une anecdote à te raconter !",
        ]

        return choice(introduction)


    def get_bye(self):
        """ Papy will say bye with a random sentence. """

        bye = [
            "Allé n'oublie pas de me ramener du Schnaps la prochaine fois !",
            "Après je ne me rappel plus très bien de la suite...",
            "Tu m'enverras une carte postale !",
            "Bon je dois me reposer maintenant, à la prochaine !",
        ]

        return choice(bye)


    def get_bad_question_message(self):
        """ Papy will say he don't understand when a BAD_QUESTION error
        append """

        message = [
            "Je n'ai pas très bien entendu... Peux-tu reformuler ta phrase ?",
            "Je ne suis plus tout jeune, peux-tu reformuler ta question ?",
        ]

        return choice(message)
