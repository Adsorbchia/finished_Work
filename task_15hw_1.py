"""
Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""
import logging
import argparse

logging.basicConfig(filename='logs/logHW.log',
                    encoding='utf-8',
                    format='{levelname:<6} - "{funcName}()" - {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def key_params(**kwargs):
    result = {}
    for key, val in kwargs.items():
        try:
            if hash(val):
                result[val] = key
        except TypeError as e:
            logger.debug(f'Поймали ошибку {e}')
            result[str(val)] = key
    return result


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Принимаем на вход ключевые параметры')
    parser.add_argument('-a', action='store_const', const=5)
    parser.add_argument('-b', action='store_const', const='hello')
    parser.add_argument('-c', nargs="+", type=int)
    parser.add_argument('-d', action='append_const', const=list)
    args = parser.parse_args()
    print(key_params(a=args.a, b=args.b, c=args.c, d=args.d))
