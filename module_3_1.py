calls = 0


def count_calls():  # подсчитывает функций
    global calls
    calls += 1


def string_info(
        string):  # принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string,
                list_to_search):  # принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)
