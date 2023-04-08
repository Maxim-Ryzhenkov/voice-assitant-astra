import pyttsx3
import torch
import time
from config import Config, Speakers
import sounddevice as sd


class Speaker:
    """ Класс синтезирующий и озвучивающий текст.
        Тип синтеза речи можно переключать в файле 'config.py'
        Доступно озвучивание с библиотеками:
            pyttsx3 - голос робота.
            silero - синтез речи из модели пакета pytorch. Есть несколько голосов и эмоции.
    """
    def __init__(self):
        if Config.CURRENT_SPEAKER == Speakers.silero:
            self.speaker = SpeakerSilero()
        elif Config.CURRENT_SPEAKER == Speakers.pyttsx3:
            self.speaker = SpeakerPyttsx3()

    def say(self, text) -> None:
        """ Озвучить переданный текст. """
        self.speaker.say(text)


class SpeakerSilero:
    """ Класс синтезирующий и озвучивающий текст.
        Для синтеза используется модель silero из пакета pytorch.
        Есть несколько голосов и эмоции.
    """
    def __init__(self):
        self.language = Config.SPEECH_LANGUAGE
        self.model_id = 'ru_v3'
        self.sample_rate = 48000
        self.speaker = 'xenia'  # aidar, baya, kseniya, xenia, random
        self.put_accent = True
        self.put_yoo = True
        self.device = torch.device('cpu')  # cpu

        self.model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                       model='silero_tts',
                                       language=self.language,
                                       speaker=self.model_id)
        self.model.to(self.device)

    def say(self, text: str):
        """ Озвучить переданный текст.
            Этот метод озвучки более качественный.
            Он передает интонации, акцент, и может звучать разными голосами.
            При этом он требует больше ресурсов.
        https://alphacephei.com/vosk/models
        """
        audio = self.model.apply_tts(text=text,
                                     speaker=self.speaker,
                                     sample_rate=self.sample_rate,
                                     put_accent=self.put_accent,
                                     put_yo=self.put_yoo)
        sd.play(audio, samplerate=self.sample_rate)
        time.sleep(len(audio) / self.sample_rate)
        # TODO: Если раскомментировать строчку с sd.wait(), то конец фразы начинает обрезаться.
        #  Хотя код внизу выглядит более правильным, чем искусственная задержка с time.sleep()
        #  Надо разобраться в документации в чем дело.
        # sd.wait()
        sd.stop()


class SpeakerPyttsx3:
    """ Класс синтезирующий и озвучивающий текст.
        pyttsx3 - голос робота.
    """
    def __init__(self):
        self.engine = pyttsx3.init()

    def say(self, text: str):
        """ Озвучить переданный текст.
            Этот метод озвучки звучит как 'голос робота',
            то есть довольно коряво, со сбитой дикцией и без эмоций.
            Но озвучивает точно и довольно неплохо.
        """
        self.engine.say(text)
        self.engine.runAndWait()


if __name__ == "__main__":
    # Тестовый код для проверки синтеза речи.
    SpeakerPyttsx3().say("Синтез речи 'Пи тэ тэ эс икс три' работает нормально!")
    SpeakerSilero().say("Синтез речи 'СилЕро' работает нормально!")

