# Вам необходимо написать 3 функции:
# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает
# кортеж из: длины этой строки, строку в верхнем регистре, строку
# в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список,
# и возвращает True, если строка находится в этом списке, False
# - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

calls = 0
def countCalls():
    global calls
    calls += 1

def stringInfo(str =''):
    strInfo = (len(str), str.upper(), str.lower())
    countCalls()
    return strInfo

def isContains(string, listToSearch):
    countCalls()
    string = string.upper()
    listToSearch = [i.upper() for i in listToSearch]
    if listToSearch.count(string):
        return True
    else:
        return False


print(stringInfo('Capybara'))
print(stringInfo('Armageddon'))
print(isContains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(isContains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

