#разбор лямбда функции
def f(x):
    print(x)

f(152)

pr = 'строка'

print(pr.title())
print((lambda x:x)(10))

ident_lambda = lambda x: x

print(ident_lambda(5))

car = lambda brend, volume_egine, price: f'Car: {brend.title()}, Engine_volume: {volume_egine}, price: {price}'

print(car('volvo',5,10))

print(type(f), type(car))
print(id(f), id(car))