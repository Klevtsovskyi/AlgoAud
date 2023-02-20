"""
Реалізуйте інтерфейс для роботи з англійсько-українським словником та швидким пошуком перекладу.
"""

dictionary = []


def addTranslation(eng, translation):
    """ Додає до словника англійське слово та його переклад.
    Пари (eng, translation) приходяться у порядку, що відповідає лексикографічному порядку.

    :param eng: англійське слово
    :param translation: переклад
    """
    dictionary.append((eng, translation))


def find(eng):
    """ Повертає переклад слова зі словника.
    :param eng: англійське слово
    :return: переклад слова, якщо воно міститься у словнику, або порожній рядок у іншому разі.
    """
    l = 0
    r = len(dictionary) - 1
    while l < r:
        m = l + (r - l) // 2
        if dictionary[m][0] < eng:
            l = m + 1
        else:
            r = m

    if dictionary[l][0] == eng:
        return dictionary[l][1]
    return ""
