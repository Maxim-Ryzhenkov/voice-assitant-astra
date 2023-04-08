# coding: utf-8

"""
    Навык "открыть браузер" реализован
    с помощью модуля 'webbrowser'.
    Документация модуля здесь
    https://docs.python.org/3/library/webbrowser.html#
"""

import webbrowser
from common_phrases import CommonPhrases


class Action:
    intents = [{"tag": "open_chrome",
                "patterns": [
                    "Открой браузер хром",
                    "Открой гугл браузер",
                    "Открой браузер"
                ],
                "responses": CommonPhrases.va_standard_confirmations
                },
               {"tag": "open_firefox",
                "patterns": [
                    "Открой браузер фаерфокс",
                    "Открой браузер мозилла",
                    "Открой лисицу"
                ],
                "responses": CommonPhrases.va_standard_confirmations
                },
               ]


class WebBrowser:
    """ Класс умеет открывать Chrome и FireFox.
    """

    @staticmethod
    def open_chrome() -> None:
        """ Открыть браузер 'Chrome'. """
        path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        webbrowser.register('chrome', None, webbrowser.Chrome(path), preferred=True)
        chrome = webbrowser.get('chrome')
        chrome.open(url="https://ya.ru")

    @staticmethod
    def open_firefox() -> None:
        """ Открыть браузер 'FireFox'. """
        path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        webbrowser.register('firefox', None, webbrowser.Mozilla(path), preferred=False)
        firefox = webbrowser.get('firefox')
        firefox.open(url="https://ya.ru")


if __name__ == "__main__":
    # Код для проверки работоспособности модуля.
    browser = WebBrowser()
    browser.open_chrome()
    browser.open_firefox()
