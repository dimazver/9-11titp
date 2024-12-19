import random


def count_subarrays_with_sum(arr, target_sum):
    """
    Функция для подсчета количества подмассивов, сумма которых равна заданному числу.

    Параметры:
    arr (list of int): Массив целых чисел.
    target_sum (int): Целевая сумма, которую должны иметь подмассивы.

    Возвращаемое значение:
    int: Количество подмассивов, сумма которых равна target_sum.
    """
    count = 0
    current_sum = 0
    prefix_sums = {0: 1}

    for num in arr:
        current_sum += num
        if (current_sum - target_sum) in prefix_sums:
            count += prefix_sums[current_sum - target_sum]
        if current_sum in prefix_sums:
            prefix_sums[current_sum] += 1
        else:
            prefix_sums[current_sum] = 1

    return count


def add_large_numbers(arr1, arr2):
    """
    Функция для сложения двух больших чисел, представленных в виде массивов цифр.

    Параметры:
    arr1 (list of int): Первый массив цифр.
    arr2 (list of int): Второй массив цифр.

    Возвращаемое значение:
    list of int: Массив цифр, представляющий сумму двух больших чисел.
    """
    carry = 0
    result = []
    max_len = max(len(arr1), len(arr2))

    arr1 = [0] * (max_len - len(arr1)) + arr1
    arr2 = [0] * (max_len - len(arr2)) + arr2

    for i in range(max_len - 1, -1, -1):
        total = arr1[i] + arr2[i] + carry
        result.append(total % 10)
        carry = total // 10

    if carry:
        result.append(carry)

    return result[::-1]


def subtract_large_numbers(arr1, arr2):
    """
    Функция для вычитания двух больших чисел, представленных в виде массивов цифр.

    Параметры:
    arr1 (list of int): Первый массив цифр.
    arr2 (list of int): Второй массив цифр.

    Возвращаемое значение:
    list of int: Массив цифр, представляющий разность двух больших чисел.
    """
    borrow = 0
    result = []
    max_len = max(len(arr1), len(arr2))

    arr1 = [0] * (max_len - len(arr1)) + arr1
    arr2 = [0] * (max_len - len(arr2)) + arr2

    for i in range(max_len - 1, -1, -1):
        diff = arr1[i] - arr2[i] - borrow
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        result.append(diff)

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return result[::-1]


def is_reversed(n):
    """
    Функция для переворота числа.

    Параметры:
    n (int): Число для переворота.

    Возвращаемое значение:
    int: Перевернутое число.
    """
    return int(str(n)[::-1])


def count_common_numbers(arr1, arr2):
    """
    Функция для подсчета количества общих чисел в двух массивах, включая случаи, когда число в одном массиве является перевернутой версией числа в другом массиве.

    Параметры:
    arr1 (list of int): Первый массив чисел.
    arr2 (list of int): Второй массив чисел.

    Возвращаемое значение:
    int: Количество общих чисел.
    """
    set1 = set(arr1)
    set2 = set(arr2)

    reversed_set1 = set(is_reversed(n) for n in arr1)
    reversed_set2 = set(is_reversed(n) for n in arr2)

    combined_set1 = set1.union(reversed_set1)
    combined_set2 = set2.union(reversed_set2)

    common_elements = combined_set1.intersection(combined_set2)

    return len(common_elements)


def get_arr(length):
    """
    Функция для ввода массива чисел с клавиатуры.

    Параметры:
    length (int): Длина массива.

    Возвращаемое значение:
    list of int: Массив чисел, введенных пользователем.
    """
    a = []
    for i in range(length):
        a.append(int(input()))
    return a


def gen_arr(length):
    """
    Функция для генерации массива случайных чисел.

    Параметры:
    length (int): Длина массива.

    Возвращаемое значение:
    list of int: Массив случайных чисел.
    """
    a = []
    for i in range(length):
        a.append(random.randint(0, 9))
    return a


def gen_or_get_arr():
    """
    Функция для выбора способа получения массива: ввод с клавиатуры или генерация случайных чисел.

    Параметры:
    Нет.

    Возвращаемое значение:
    list of int: Массив чисел, полученный либо вводом с клавиатуры, либо генерацией случайных чисел.
    """
    print("Желаете ввести массив вручную? y/n \n В случае отказа массив будет сгенерирован случайно")
    ch = input()
    if ch == 'y':
        print("Введите длину массива")
        length = int(input())
        return get_arr(length)
    elif ch == 'n':
        print("Введите длину массива")
        length = int(input())
        return gen_arr(length)
    else:
        print("Неверные данные")
