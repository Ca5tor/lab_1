
"""
Все лабораторные выполняются без использования встроенных функций
на подобии (max, reverse, sorted и тд).
Если нужно отсортировать массив используйте сортировку пузырьком
или любую другую сортировку оформленную кодом,
а не встроенным методом или библиотекой.
"""

#   1. Найдите сумму и произведение элементов списка.
#   Результаты вывести на экран.

def amountNumList(list):
    count = 0
    for i in list: count += 1
    return (count)

def getSum(s, len):
    i, sum = 0, 0
    while i < len:
        sum += s[i]     
        i += 1
    return (sum)

def getProd(s, len):
    i, prod = 0, 1
    while i < len:
        prod *= s[i]
        i += 1
    return (prod)

def main_0():
    s   = [2, 1, 4, 3, 6, 5, 8, 7, 9, 0.54]
    len = amountNumList(s)
    print("Сумма= ", getSum(s, len), "\nПроизведение= ", getProd(s, len))
    return ()

#   2. В массиве действительных чисел
#   все нулевые элементы заменить
#   на ср.арифм. всех элементов массива.

def replaceZeroWithNum(s, len, num):
    i = 0
    while i < len:
        if s[i] == 0: s[i] = num
        i+=1
    return (s)

def main_1():
    s       = [2.1, 0, 2.28, -5, 0, 0.25, -1, 0]
    print ("Было:  ", s)
    len     = amountNumList(s)
    average = (getSum(s, len) / len)
    s       = replaceZeroWithNum(s, len, average)
    print("Стало: ", s)
    return ()

#Вызов функций решения заданий
print("\tЗадание №1"),   main_0()
print("\n\tЗадание №2"), main_1()