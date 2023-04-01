# coding: utf-8


from fuzzywuzzy import fuzz
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

from config import Config
from commands import commands
from speaker import Speaker


class CommandProcessor:
    """ Класс для обработки команд, получаемых из сообщений пользователя. """

    def text_content_assistants_name(self, user_text: str) -> bool:
        names_in_rext = Config.ASSISTANT.name_options.intersection(user_text.split())
        return names_in_rext is not None

    def text_starts_with_assistants_name(self, user_text: str) -> bool:
        """ Вернуть True, если фраза начинается с обращения к ассистенту. """
        return user_text.startswith(Config.ASSISTANT.name_options)

    def replace_assistant_name_from_text(self, user_text):
        names_in_rext = Config.ASSISTANT.name_options.intersection(user_text.split())
        user_text.replace(list(names_in_rext)[0], '')   # Удалить первое вхождение имени ассистента в тексте.

    def replace_assistant_name_from_start(self, user_text):
        return " ".join(user_text.split()[-1:])

    def process(self, user_text: str):
        """ Фраза пользователя ищется среди ключевых фраз в файле 'commands.py'.
            Если совпадение обнаружено - запускается ассоциированное с фразой
            действие ассистента.
        """
        if self.text_starts_with_assistants_name(user_text):
            user_text = self.replace_assistant_name_from_start(user_text)
        else:
            # Если не включен режим активного слушания, то ассистент
            # не реагирует на фразы, не начинающиеся с его имени.
            if not Config.ASSISTANT.active_listening:
                return

        for action, phrases in commands.items():
            if user_text in phrases:
                action()
