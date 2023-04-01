# coding: utf-8
import enum


class Speakers(enum.Enum):
    silero = 1
    pyttsx3 = 2


class Languages(enum.Enum):
    russian = 'ru', 'ru-RU'
    english = 'en', 'en-US'

    def __init__(self, speech, recognition):
        self.speech = speech
        self.recognition = recognition


class User:
    name = 'Максим'
    sex = 'male'
    current_location = 'Moscow'


class Assistant:
    name = 'Астра'
    name_options = (name.lower(), "робот", "ассистент", "помощник")
    sex = 'female'
    speech_language = Languages.russian
    active_listening = False


class Config:
    # Выбор озвучки голоса ассистента.
    # Подробные описания можно посмотреть в 'speaker.py'
    CURRENT_SPEAKER = Speakers.pyttsx3

    # Если True используем онлайн распознавание от Google.
    # Если False используем офлайн распознавание от Vosk.
    ONLINE_MODE = True

    ASSISTANT = Assistant
    USER = User

    SPEECH_LANGUAGE = Languages.russian.speech
    RECOGNITION_LANGUAGE = Languages.russian.recognition







