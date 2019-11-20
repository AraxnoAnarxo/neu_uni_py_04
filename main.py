import random

print()
print("Задача 1. \nВыбор 100 случайных имен из списка")
# 20 имен
list_names = 'Natalia Ksenia Viola Ivan Kostya Kosmos Katya Darya Valya Nikita Serezha Vitya Sarah Petya Victor Seva Lyonya Maxim Vova Raya'.split()


def name_n(list_names, n):
    '''

    :param list_names: список имен
    :param n: длина списка на выходе
    :return: список из 20 случайных имен
    '''
    list_names_random = []
    len_list = len(list_names)
    newName = ''

    for i in range(1, n + 1):
        # randomChoice - это случайное число в пределах длины начального списка,
        # случайным образом выбираем индекс
        randomChoice = random.randint(0, len_list-1)
        # newName - это случайное слово по индексу
        newName = list_names[randomChoice]
        # Добавляем случайное слово newName в список
        list_names_random.append(newName)

    return list_names_random

list_names_random = name_n(list_names, 100) # n == 100
print('Список: \n%s\nКоличество слов: %s\nИзначально слов: %s' % (list_names_random, len(list_names_random), len(list_names)))
print()

print("Задача 2. \nСамое популярное имя:")

def popular_name(list_names_random):
    # Создаем словарь, который считает количество упоминаний
    list_names_random = {a: list_names_random.count(a) for a in list_names_random}
    print(list_names_random) # для проверки - словарь с именем и количеством упоминаний

    # Создаем список со значениями
    values_list = []

    for values in list_names_random.values():
        values_list.append(values)

    # из списка со значениями выбираем максимальное значение,
    # создаем список из ключей, которым соответсвует максимальное значение
    popular_names_list = []

    for items, values in list_names_random.items():
        if values == max(values_list):
            popular_names_list.append(items)


    return popular_names_list

print('Имя:', popular_name(list_names_random))
print()

print('Задача 3.\nСамая редкая буква, с которой начинается имя:')

# Напишите функцию вывода самой редкой буквы,
# с которой начинаются имена в списке на выходе функции F.
def rare_letter(list_names_random):
    first_letter_list = []
    first_letter = ''
    # Создаем список из начальных букв
    for name in list_names_random:
        first_letter = name[0]
        first_letter_list.append(first_letter)
    #print(first_letter_list, len(first_letter_list)) # для проверки количества букв

    # Создаем словарь из букв и количества их упоминаний
    dict_rare_letter = {a: first_letter_list.count(a) for a in first_letter_list}

    print (dict_rare_letter) # для проверки - количество упоминаний букв

    # Создаем список значений
    letter_values = []

    for values in dict_rare_letter.values():
        letter_values.append(values)

    # Создаем список из ключей, которым соответвует минимальное значение
    rare_letter_list = []
    for items, values in dict_rare_letter.items():
        if values == min(letter_values):
            rare_letter_list.append(items)

    return rare_letter_list


print('Самая редкая начальная буква:', rare_letter(list_names_random))
print()