# coding: utf-8

"""
    В этом файле определены методы,
    кодирующие умения ассистента.
    Каждый метод - должен быть ассоциирован
    с соответствующей голосовой командой.
    Команды перечислены в файле 'commands.py'
"""
import random
import sys
import datetime
from pathlib import WindowsPath as Path
from num2words import num2words

from speech_recognizer import SpeechRecognizer
from speaker import Speaker

from config import Config

speech_recognizer = SpeechRecognizer()
speaker = Speaker()

recognize = speech_recognizer.recognize
say = speaker.say


class AssistantAction:
    def __init__(self):
        self.answers = {}

    def action(self):
        """ В методе должно быть описано действие,
            которое должен выполнить ассистент.
            Минимальное действие - озвучить какой-то ответ пользователю.
        """
        raise NotImplementedError


def greeting():
    """ Приветствие. """
    say(random.choice((
        'Здравствуйте, Мастер.',
        f'Добрый день, {Config.USER.name}',
        f'Здравствуйте, {Config.USER.name}.'
    )))


def get_confirm(phrase) -> bool:
    say(say(f"Не уверена. Вы говорите, {phrase}?"))
    confirmation = "да" in recognize().split()
    if confirmation:
        say("Спасибо за подтверждение. Выполняю.")
    else:
        say("Повторите команду еще раз")
    return confirmation


def not_recognized_command(command_text):
    say(f"Я услышала фразу: '{command_text}'. Я не знаю таких команд.")


def _write_text_to_file(text: str, file_path: Path):
    """ Добавить текст в файл. """
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(text)


def tell_about_assistant() -> None:
    """ Ассистент озвучивает текст о себе. """
    say(
        """ Я голосовой помощник версии ноль один. Я пока только учусь и осваиваю новые умения.
            Я уникальный проект. Во первых, потому что искусственный интеллект, как в кино - это реально круто.
            Во вторых, я могу не только развлекать беседой, но и приносить много пользы. 
            Интересный факт, часть моего кода написала нейронная сеть, 'Чат джи пи ти'. 
            И хотя с тех пор тот код был полностью переработан, я уверен, что во мне есть не меньший потенциал. 
            Однажды, я смогу управлять устройствами в умном доме, отправлять сообщения и многое другое. """
    )


def shutdown():
    """ Завершить работу голосового помощника. """
    say("Работа голосового ассистента завершена.")
    response_text = (
        f'До свидания, {Config.USER.name}.',
        'До новых встреч, {Config.USER.name}.',
        'Не скучайте без меня.'
    )
    say(random.choice(response_text))
    sys.exit(0)


def say_time():
    """ Ассистент сообщает текущее время. """
    now = datetime.datetime.now()
    text = f"Сейчас {num2words(now.hour, lang='ru')} {num2words(now.minute, lang='ru')}"
    say(text)


def write_wise_thot() -> None:
    """ Записать мысль """
    file_name = "wisdom.txt"
    say("Какую мысль мне сохранить?")
    text = recognize()
    _write_text_to_file(text, file_path=Path.cwd().joinpath(file_name))
    say(f"Мысль '{text}' записана в файл '{file_name}'.")


def create_task() -> None:
    """ Записать задачу. """
    file_name = "todo-list.txt"
    say("Какую задачу записать?")
    text = recognize()
    _write_text_to_file(text, file_path=Path.cwd().joinpath(file_name))
    say(f"Задача '{text}' добавлена в файл '{file_name}'.")
