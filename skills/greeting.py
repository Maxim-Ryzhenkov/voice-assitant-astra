from random import choice

intents = [{"tag": "greeting",
            "patterns": [
                "Привет",
                "Здравствуй",
                "Здорово",
                "Добрый день",
                "Добрый вечер",
                "Доброе утро",
                "Доброй ночи"
            ],
            "responses": [
                "Здравствуйте",
                "Моё почтение",
                "Рада встрече",
                "Салют!"
            ]
            },
           ]


def greeting():
    """ Приветствие. """
    return choice(intents[0].get('responses'))
