from speaker import SpeakerPyttsx3
from speech_recognizer import SpeechRecognizerGoogle


class Astra:
    def __init__(self):
        self.name = 'Астра'
        self.voice = SpeakerPyttsx3()
        self.voice_recognizer = SpeechRecognizerGoogle()
        self.active_listening_mode = False   # Будет слушать команду только после обращения по имени.

    def listen(self) -> str:
        """ Слушать команду пользователя и
            вернуть текст когда он замолчит. """
        self.say('Слушаю...')
        text = self.voice_recognizer.recognize()
        print(f"Вы сказали: {text}")
        return text

    def say(self, text) -> None:
        """ Озвучить текст. """
        print(f"{self.name}: {text}")
        self.voice.say(text)

    def handle_command(self, command):
        """ Обработать полученную команду. """
        self.say(f"Вы сказали: {command}")

    def cancel_current_command(self):
        """ Прервать и отменить текущую команду. """
        # TODO: Реализовать по команде 'Астра, стоп.'
        pass

    def start(self):
        self.say("Запуск ассистента.")
        while True:
            text = self.listen()
            self.handle_command(command=text)

    def stop(self):
        self.say('До скорого!')
        exit()


if __name__ == "__main__":
    astra = Astra()

    try:
        astra.start()
    except KeyboardInterrupt:
        astra.stop()
