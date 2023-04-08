# coding: utf-8

import os
import queue
import sys
import json

import vosk
import sounddevice as sd

import speech_recognition as sr
from config import Config
from speaker import Speaker


class SpeechRecognizer:
    """ Распознаватель речи.
        Для работы с распознаванием во всей программе
        используется только этот класс. Он является
        единственной точкой входа и имеет один метод 'recognize()'
        В зависимости от наличия интернет подключения,
        может использоваться онлайн распознавание от Google
        или офлайн распознавание с модулем Vosk.
        В настоящее время настройка переключается в 'config.py'
    """
    def __init__(self):
        if Config.ONLINE_MODE:
            self.recognizer = SpeechRecognizerGoogle()
            Speaker().say('Активирован онлайн режим распознавания.')
        else:
            self.recognizer = SpeechRecognizerVosk()
            Speaker().say('Активирован офлайн режим распознавания.')

    def recognize(self) -> str:
        """ Распознать речь и вернуть текст. """
        print("Говорите...")
        return self.recognizer.recognize()


class SpeechRecognizerGoogle:
    """ Онлайн распознавание речи на основе сервисов Google.
        Распознает отлично, но без интернета не работает.
        """
    def __init__(self):
        self._voice_recognizer = sr.Recognizer()
        self._voice_recognizer.pause_threshold = 0.5
        self._microphone = sr.Microphone()

    def recognize(self) -> str:
        """ Эта функция будет слушать входящий звук с микрофона и
            пытаться распознать его с помощью Google Speech Recognition.
            Если распознавание произошло успешно, то функция вернет текст
            команды в нижнем регистре, иначе - строку "не удалось распознать команду".
        """
        with self._microphone as mic:
            self._voice_recognizer.adjust_for_ambient_noise(source=mic, duration=0.2)
            audio = self._voice_recognizer.listen(source=mic)
        try:
            voice_text = self._voice_recognizer.recognize_google(
                audio_data=audio, language=Config.RECOGNITION_LANGUAGE).lower()
            return voice_text
        except sr.UnknownValueError:
            # TODO: В будущем эти исключения надо пробрасывать наверх и обрабатывать.
            return "Не удалось распознать фразу. Повторите, пожалуйста."
        except sr.RequestError:
            # TODO: В будущем эти исключения надо пробрасывать наверх и обрабатывать.
            return "Не удалось распознать фразу. У нас проблемы с интернетом."


class SpeechRecognizerVosk:
    """ Офлайн распознавание речи на основе библиотеки Vosk.
        Основное достоинство в том, что распознавание работает без интернета.
    """
    def __init__(self):

        large_model = 'model'   # Большая модель подходит для мощного компа или сервера. Долго грузится в память.
        small_model = 'model_small'
        current_model = small_model
        if not os.path.exists(current_model):
            print("Модель не найдена!")
            sys.exit(1)

        self.q = queue.Queue()
        self.model = vosk.Model(current_model)
        self.recognizer = vosk.KaldiRecognizer(self.model, 16000)
        self.microphone_id, self.speakers_id = sd.default.device  # id микрофона и динамиков (1, 3)
        self.sample_rate = int(sd.query_devices(device=self.microphone_id, kind='input')['default_samplerate'])

    def _callback(self, indata, frames, time, status):
        """ Это вызывается (из отдельного потока) для каждого аудио-блока. """
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))

    def recognize(self):
        """ Преобразовать речь в текст. """
        with sd.RawInputStream(samplerate=self.sample_rate, blocksize=16000, device=self.microphone_id,
                               dtype='int16', channels=1, callback=self._callback):
            rec = vosk.KaldiRecognizer(self.model, self.sample_rate)
            while True:
                data = self.q.get()
                if rec.AcceptWaveform(data):
                    data = json.loads(rec.Result())['text']
                    if data:
                        return data.strip()


if __name__ == "__main__":

    # Тестовый код для проверки распознавания голоса.
    # Если все в порядке, он будет повторять за вами сказанное.
    # Для прерывания выполнения нажмите Ctrl+C или скажите "стоп"
    speech_recognizer = SpeechRecognizer()
    speaker = Speaker()

    while True:
        text = speech_recognizer.recognize()
        speaker.say(text)
        if text == "стоп":
            break
    speaker.say("Выполнение программы остановлено.")
