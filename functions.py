# def add(x,y):
#     '''
#     тут идет описнаие функции
#     '''
#     return x+y
#
# print(add('вова',' маша'))
#
# def f1(n):
#     def f2(m):
#         return n+m
#     return f2
# new_f=f1(100)
# print(new_f(50))
#
# def f():
#     pass
# print(f())

# Аргументы

def add (x, y, z=10):
    '''
    :param x: первый параметр
    :param y: второй параметр
    :param z: третий параметр
    :return: возврат суммы
    '''
    return x+y+z

print(add(3,5,5))

def function(*args):
    print(type(args),args)
    return args
function(123)

def function1(**kwargs):
    print(type(kwargs),kwargs)
    return kwargs
function1(a=1,b=2,c='volvo')


def funct_dificult(x, y, z=5, *args, **kwargs):
    '''

    :param x: обязательный параметр
    :param y: обязательный параметр
    :param z: не обязательный параметр
    :param args: кортеж
    :param kwargs: массив
    :return:
    '''
    print(type(x),x)
    print(type(y),y)
    print(type(args),args)
    print(type(kwargs),kwargs)

funct_dificult(3,7, (1,3,7),first=1, second=2)