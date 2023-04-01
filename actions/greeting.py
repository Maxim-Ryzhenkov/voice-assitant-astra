f



def greeting():
    """ Приветствие. """
    say(random.choice((
        'Здравствуйте, Мастер.',
        f'Добрый день, {Config.USER.name}',
        f'Здравствуйте, {Config.USER.name}.'
    )))