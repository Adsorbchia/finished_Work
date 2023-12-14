"""
Задание №1
Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
Например отлавливаем ошибку деления на ноль.
"""
import logging

logging.basicConfig(filename='logs/log.log',
                    filemode='+w',
                    format='{levelname}-{asctime} - {msg}',
                    style='{',
                    encoding='utf-8',
                    level=logging.NOTSET)
logger = logging.getLogger(__name__)


def func(a, b):
    c = None
    try:
        c = b // a
        return c
    except ZeroDivisionError as e:
        logger.error(f'отлавливаем ошибку {e} -  деления на ноль запрещено')


print(func(0, 4))
