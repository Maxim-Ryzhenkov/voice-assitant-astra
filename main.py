# coding: utf-8

""" Пример бота для распознавания речи. """

from speech_recognizer import SpeechRecognizer
from command_processor import CommandProcessor


speech_recognizer = SpeechRecognizer()
command_processor = CommandProcessor()


if __name__ == "__main__":
    while True:
        user_phrase = speech_recognizer.recognize()
        command_processor.process(user_phrase)
