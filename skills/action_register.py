# coding: utf-8

"""
    Здесь находится список команд, известных ассистенту.
"""

from skills import actions


commands = {
    actions.greeting: {'привет', 'здравствуй'},
    actions.tell_about_assistant: {'расскажи о себе', },
    actions.shutdown: {'выключись', 'отключись'},
    actions.say_time: {'сколько времени', 'сколько на часах', 'какое сейчас время', 'сколько сейчас времени'},
    actions.create_task: {'запиши задачу', 'записать задачу', 'сохранить задачу', 'сохрани задачу'},
    actions.write_wise_thot: {'запиши мысль', 'запиши текст'},
    # skills.translate: {'переведи фразу', 'как сказать на английском',
    #                     'как на английском будет', 'переведи на английский'}

}