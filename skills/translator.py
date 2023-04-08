# coding: utf-8

"""
    Для работы этого модуля нужна библиотека 'translate'
    Библиотека предоставляет сервис переводов google translator
    и требует подключения интернета.
"""

from translate import Translator as Tr


class Action:
    intents = [{"tag": "translate_to_russian",
                "patterns": [
                    "Переведи на русский",
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


class Translator:
    """ Класс переводчик предоставляет два метода перевода:
        - с русского на английский;
        - с английского на русский.
    """

    @staticmethod
    def russian_to_english(text) -> str:
        """ Перевести переданный текст. """
        translator = Tr(from_lang="ru", to_lang="en")
        return translator.translate(text)


    @staticmethod
    def english_to_russian(text) -> str:
        """ Перевести переданный текст с
            английского языка на русский. """
        translator = Tr(from_lang="en", to_lang="ru")
        return translator.translate(text)


if __name__ == "__main__":
    # Код для проверки работоспособности модуля.
    translator = Translator()
    print(translator.russian_to_english("Здравствуй, меня зовут Астра. А как тебя зовут?"))
    print(translator.english_to_russian("Hello, my name is Astra. What's your name?"))
