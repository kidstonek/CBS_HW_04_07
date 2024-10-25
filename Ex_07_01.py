'''
Завдання 1
Створіть функцію, яка приймає список з елементів типу int,
а повертає новий список з рядкових значень вихідного масиву.
Додайте анотацію типів для вхідних і вислідних значень функції.
'''

from typing import List


def my_func(num: List[int]) -> List[str]:
    """
    Convert list with int`s to list with str`s
    :param num: List with int`s
    :type num: List[int]
    :return: List with str`s

    Example:
    .. cede-block:: python
        >> [1, 2, 3, 4, 5]

        << ['1', '2', '3', '4', '5']
    """
    return list(map(lambda n: str(n), num))


my_func()

