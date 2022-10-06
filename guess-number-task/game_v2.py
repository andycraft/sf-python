"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def binary_search(number: int = 1) -> int:
    """Находим заданное число методом бинарного поиска

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    # задаем верхнюю и нижнюю границы искомого числа
    low_value, high_value = 1, 100

    while True:
        count += 1

        # определяем среднее арифметическое значение
        predict_number = (low_value + high_value) // 2

        if number > predict_number:
            # искомое число больше предсказанного, сдвигаем нижнюю границу
            low_value = predict_number + 1

        elif number < predict_number:
            # искомое число меньше предсказанного, сдвигаем верхнюю границу
            high_value = predict_number - 1

        else:
            # число найдено, выходим из цикла
            break

    return count


def score_game(predict_function) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict_function(number))

    score = int(np.mean(count_ls))
    print(f"Функция {predict_function.__name__} угадывает число",
          f"в среднем за: {score} попыток")

    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    score_game(binary_search)
