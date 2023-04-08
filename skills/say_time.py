# coding: utf-8

"""
    Для работы этого модуля нужна библиотека 'datetime'
"""


class Action:
    intents = [{"tag": "say_time",
                "patterns": [
                    "",
                    "Переведи с английского",
                    "Как на русском будет",
                    "Как по русски сказать",
                    "Как на русский перевести фразу",
                    "Translate to russian",
                    "Translate from English",
                    "How will it be in Russian",
                    "How to say in Russian"
                    "How to translate a phrase into Russian"
                ],
                "responses": []
                },
               {"tag": "translate_to_english",
                "patterns": [
                    "Переведи на английский",
                    "Переведи с русского",
                    "Как на английском будет",
                    "Как по английски сказать",
                    "Как на английский перевести фразу"
                ],
                "responses": []
                },
               ]


def say_time():
    """ Ассистент сообщает текущее время. """
    now = datetime.datetime.now()
    text = f"Сейчас {num2words(now.hour, lang='ru')} {num2words(now.minute, lang='ru')}"
    say(text)


if name =