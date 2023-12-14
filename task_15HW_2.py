"""
На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
Первый список ваш лотерейный билет.
Второй список содержит список чисел, которые выпали в лотерею.
Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.

Напишите класс LotteryGame, который будет иметь метод compare_lists, который будет сравнивать числа из вашего билета из
list1 со списком выпавших чисел list2

Если совпадающих чисел нет, то выведите на экран:
Совпадающих чисел нет. Результат работы функции запишем в файл.
"""

import logging
import argparse


logging.basicConfig(filename='logs/logHW2.log',
                    encoding='utf-8',
                    format='{levelname:<6} - {asctime} - "{funcName}()" - {msg}',
                    style='{',
                    level=logging.INFO
                    )
logger = logging.getLogger(__name__)


class LotteryGame:

    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        list_1_2 = []
        for i in self.list1:
            for j in self.list2:
                if i == j:
                    list_1_2.append(i)
                    break
        if len(list_1_2) > 0:
            logger.info(f'Совпадающие числа: {list_1_2}'
                        f'kо-во сов. чисел: {len(list_1_2)}')

        else:
            logger.info(f'Cовпадения  не найдены')


if __name__ == "__main__":
    list_1 = [9, 5, 6, 12, 14, 8, 12, 6, 8]
    list_2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]
    parser = argparse.ArgumentParser()
    parser.add_argument('-list_1', nargs='+', type=int)
    parser.add_argument('-list_2', nargs='+', type=int)
    args = parser.parse_args()
    game = LotteryGame(args.list_1, args.list_2)
    game.compare_lists()
