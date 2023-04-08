# coding: utf-8

""" Пример бота для распознавания речи. """

from astra import Astra
from command_processor import CommandProcessor

astra = Astra()


if __name__ == "__main__":
    while True:

        user_phrase = Astra.listen()
        command_processor.process(user_phrase)
