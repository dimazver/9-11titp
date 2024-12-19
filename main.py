import funks


def menu(point):
    """
    Функция для выполнения различных задач в зависимости от выбранного пункта меню.

    Параметры:
    point (int): Номер выбранного пункта меню.

    Возвращаемое значение:
    Нет.
    """
    if point == 1:
        mas_a = funks.gen_or_get_arr()
        mas_b = funks.gen_or_get_arr()
        print("Сумма (1) или разность (2)")
        x = int(input())
        if x == 1:
            print(funks.add_large_numbers(mas_a, mas_b))
        elif x == 2:
            print(funks.subtract_large_numbers(mas_a, mas_b))
        else:
            print("Error")
    elif point == 2:
        arr1 = funks.gen_or_get_arr()
        arr2 = funks.gen_or_get_arr()
        print(funks.count_common_numbers(arr1, arr2))
    elif point == 3:
        arr = funks.gen_or_get_arr()
        print("Введите число: ")
        num = int(input())
        print(funks.count_subarrays_with_sum(arr, num))
    elif point == 4:
        exit()
    else:
        print("Error")


if __name__ == "__main__":
    while True:
        print("Задачи\n1.	Входные данные: 2 массива с цифрами, каждый представляет собой большое число. Нужно "
              "произвести сумму или разность массивов\n2.	Входные данные: 2 массива с "
              "числами. Требуется проверить, сколько у массивов общих чисел. Также, число будет считаться общим, "
              "если оно входит в один массив, а в другом массиве находится его перевернутая версия.\n3.	Входные "
              "данные: массив и число. Требуется проверить, "
              "сколько подмассивов из массива в сумме могут давать это число\n4.  Выход")
        print("Выберите пункт меню\n")
        menu(int(input()))
