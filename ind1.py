# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# Ввести список А из 10 элементов, найти разность положительных элементов, и вывести ее
# на экран. и причём надо,чтобы вычитания были попарно,2 числа и из двух ищется разница

if __name__ == '__main__':
    lst = tuple(map(int, input().split(" ")))
    new_lst = ()

    # Уберем все отрицательные значения
    for item in lst:
        if item > 0:
            new_lst = new_lst + (item,)

    # Исключим возможность нечетного количества положительных элементов
    if len(new_lst) % 2 != 0:
        new_lst = tuple(new_lst[:len(new_lst) - 1])

    res = ()
    skip = False
    for i, item in enumerate(new_lst):
        if skip:
            skip = False
            continue
        if i < len(new_lst) - 1:
            res = res + (new_lst[i] - new_lst[i + 1], )
            skip = True

    print(new_lst, res)

    # tuples = [tuple(k) for k in zip(lst[::2], lst[1::2])]
    # print(*tuples)
    # result = [i - j for i, j in tuples]
    # print(*result)
