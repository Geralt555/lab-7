#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ввести список А из 10 элементов, найти разность положительных элементов, и вывести ее
# на экран.

# import sys

if __name__ == '__main__':
    tuple = (1, 4, -5, -6, -9, 5, 8, -11, 13)
    print(tuple)
    negatives = [i for i in tuple if i < 0]
    mul = 1
    for i in negatives:
        mul *= i
    print('Произведение отрицательных: ', mul)
