# coding: utf-8

"""
    Для работы этого модуля нужна библиотека 'translate'
    Библиотека предоставляет сервис переводов google translator
    и требует подключения интернета.


"""

from translate import Translator as Tr


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
