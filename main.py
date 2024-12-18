def count_subarrays_with_sum(arr, target_sum):
    """Функция для подсчета количества подмассивов, сумма которых равна заданному числу."""
    count = 0
    current_sum = 0
    prefix_sums = {0: 1}  # Инициализируем словарь для хранения префиксных сумм

    for num in arr:
        current_sum += num
        if (current_sum - target_sum) in prefix_sums:
            count += prefix_sums[current_sum - target_sum]
        if current_sum in prefix_sums:
            prefix_sums[current_sum] += 1
        else:
            prefix_sums[current_sum] = 1

    return count

# Пример использования
arr = [1, 2, 3, 4, 5, 6]
target_sum = 6

result = count_subarrays_with_sum(arr, target_sum)
print(f"Количество подмассивов, сумма которых равна {target_sum}: {result}")