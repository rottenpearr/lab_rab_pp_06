criteria_data = []
comparison_criteria_data = []
comparison = []
sum_line = []
comparison_amount = 0

# Данный цикл нужен для проверки правильности вводимых данных в name
while True:
    name = input('Критерии чего вы бы хотели проанализировать? ')
    if name:
        break
    else:
        print('Имя не может быть пустым. Впишите предмет для анализа!')
# Данный цикл нужен для проверки правильности вводимых данных в amount
while True:
    try:
        amount = int(input('Введите количество критериев: '))
        if amount > 0:
            break
        else:
            print('Количество критериев должно быть положительным числом.')
    except ValueError:
        print('Пожалуйста, введите целое положительное число для количества критериев.')
# Цикл создан для того, чтобы считывать и хранить названия
# критериев в массиве criteria_data
for criteria in range(amount):
    criteria = str(input(f'Введите имя для {criteria+1}-го критерия: '))
    criteria_data.append(criteria)
print('Для попарной оценки критериев вводите целые числа от 1 до 9!')
# Цикл создан для того, чтобы считывать и хранить данные о попарном сравнении критериев
# в виде матрицы построчно в массиве comparison_criteria_data
for a in range(len(criteria_data)):
    comparison = []
    for b in range(len(criteria_data)):
        # Оператор создан, чтобы отслеживать одинаковые критерии
        # (если критерии одинаковые - вносит в массив 1)
        if a == b:
            comparison.append(1)
        else:
            # Оператор создан с целью проверки на повторение критериев
            # (если у нас были критерий А и Б, далее перебором попались Б и А
            # то в массив программа впишет оценку критериев А и Б / 1)
            if b < a:
                previous_comparison = comparison_criteria_data[b][a]
                comparison.append(1 / previous_comparison)
            # Если условие одинаковости критериев не выполняется и если повторения
            # этих критериев не было, то программа запрашивает оценку критериев
            else:
                while True:
                    estimation = input(f'Сравнение "{criteria_data[a]}" и "{criteria_data[b]}": ')

                    if estimation.isnumeric() and 1 <= int(estimation) <= 9:
                        comparison.append(int(estimation))
                        break
                    else:
                        print("Вы ввели некорректное число!")
    comparison_criteria_data.append(comparison)
# Цикл нужен для подсчета суммы отдельных строк и всех строк в целом
for line in comparison_criteria_data:
    comparison_amount += sum(line)
    sum_line.append(sum(line))
print(name)
# Цикл нужен для того, чтобы выводить пользователю
# критерии и их рассчитанный коэффициент в удобной форме
for i, criteria in enumerate(criteria_data):
    print(f"Весовой коэффициент "{criteria}": {round(sum_line[i] / comparison_amount, 2)}")
