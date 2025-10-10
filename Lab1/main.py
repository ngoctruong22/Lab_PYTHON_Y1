# Функция, которую будем тестировать
def twoSum(nums, target):
    # Проверка, что все элементы являются целыми числами
    if not all(isinstance(num, int) for num in nums):
        return None

    # Основной алгоритм поиска индексов
    for i in range(len(nums)):
        # Внутренний цикл начинается со следующего элемента
        for j in range(i + 1, len(nums)):
            # Проверяем, равна ли сумма целевому значению
            if nums[i] + nums[j] == target:
                # Возвращаем индексы элементов
                return [i, j]