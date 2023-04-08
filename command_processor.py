# coding: utf-8
import random

from fuzzywuzzy import fuzz
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

from config import Config
from commands import commands
from skills import actions


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
        return " ".join(user_text.split()[1:])

    def process(self, user_text: str):
        """ Фраза пользователя ищется среди ключевых фраз в файле 'commands.py'.
            Если совпадение обнаружено - запускается ассоциированное с фразой
            действие ассистента.
        """
        # if self.text_starts_with_assistants_name(user_text):
        #     user_text = self.replace_assistant_name_from_start(user_text)
        # else:
        #     # Если не включен режим активного слушания, то ассистент
        #     # не реагирует на фразы, не начинающиеся с его имени.
        #     # TODO: нужно добавить это умение астре и добавить флаг ACTIVE_LISTENING в конфиг сессии.
        #     if not Config.ASSISTANT.active_listening:
        #         return
        print(user_text)
        command_recognized = True
        for action, phrases in commands.items():
            for phrase in phrases:
                percent_match = fuzz.WRatio(user_text, phrase)
                print(f"fuzz = {percent_match} for {user_text} in {phrase}")
                if percent_match == 100:
                    action()
                    break
                elif percent_match > 80:
                    if actions.get_confirm(phrase):
                        action()
                        break
                else:
                    command_recognized = False
        if not command_recognized:
            actions.not_recognized_command(user_text)



