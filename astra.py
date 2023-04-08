import sys
import threading

from speaker import SpeakerPyttsx3
from speech_recognizer import SpeechRecognizerGoogle
from common_phrases import CommonPhrases
from user_interface import UserInterface


class Astra:
    def __init__(self):
        self.name = 'Астра'
        self.voice = SpeakerPyttsx3()
        self.voice_recognizer = SpeechRecognizerGoogle()
        self.ui = UserInterface()
        self.active_listening_mode = False   # Будет слушать команду только после обращения по имени.

    def listen(self) -> str:
        """ Слушать команду пользователя и
            вернуть текст когда он замолчит. """
        text = self.voice_recognizer.recognize()
        print(f"Вы сказали: {text}")
        return text.lower()

    def say(self, text) -> None:
        """ Озвучить текст. """
        print(f"{self.name}: {text}")
        self.voice.say(text)

    def shut_up(self):
        """ Прервать текущую фразу. """
        print(f"{self.name}: OK. Молчу молчу...")
        self.voice.shut_up()

    def handle_command(self, command):
        """ Обработать полученную команду. """
        self.say(f"Вы сказали: {command}")

    def cancel_current_command(self):
        """ Прервать и отменить текущую команду. """
        # TODO: Реализовать по команде 'Астра, стоп.'
        pass

    def start(self) -> None:
        """ Начать работу голосового ассистента.
            Ассистент будет в бесконечном цикле слушать, пока его не позовут.
            После обращения по имени ассистент попытается распознать и выполнить команду.
        """
        self.say("Запуск ассистента.")
        while True:
            try:
                text = self.listen()
                name_trigger = set(w.lower() for w in CommonPhrases.va_name_options).intersection(set(text.split()))
                if name_trigger:
                    self.ui.mark_active()
                    text = self.listen()
                    if text in ("стоп", "завершить работу"):
                        self.stop()
                else:
                    self.ui.mark_passive()
            except Exception:
                self.ui.mark_passive()

    def stop(self) -> None:
        """ Остановить работу ассистента.
            Завершить работу голосового движка.
            Завершить работу графического интерфейса.
            Выйти из программы
        """
        self.say("До свидания")
        self.voice.speaker.runAndWait()
        self.voice.speaker.stop()
        self.ui.root.destroy()
        sys.exit(0)


if __name__ == "__main__":
    astra = Astra()

    try:
        threading.Thread(target=astra.start).start()
        astra.ui.run()
    except KeyboardInterrupt:
        astra.stop()
