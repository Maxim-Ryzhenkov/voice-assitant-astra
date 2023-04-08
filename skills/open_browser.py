# coding: utf-8

"""
    Навык "открыть браузер" реализован
    с помощью модуля 'webbrowser'.
    Документация модуля здесь
    https://docs.python.org/3/library/webbrowser.html#
"""

import webbrowser


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
