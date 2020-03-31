import random

rezult_tuple=[]


def F2(n, *args):
    '''
    Функция, которая генерирует рамдомное колличество слов из заданной строки
    :param n: столько раз генерируется слова
    :param args: строка из которой генерируются данные
    :return: возвращает список значений
    '''

    for i in range(n):
        rezult_tuple.append(random.choice(*args))
    return rezult_tuple


help(F2)

s=F2(100, ('Pete', 'Alex', 'Niko', 'Френк', 'Василий', 'Виталий'))
print(s)
print(max(set(s),key=lambda x: s.count(x))) # находит самое часто повторяемое имя в списке
print(min(set(s),key=lambda x: s.count(x[0]))) # находит самую редкую букву с которой начинается список 