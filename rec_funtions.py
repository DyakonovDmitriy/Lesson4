#g пишем функцию фактериал

def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)

print(fact(10))

fack=1

# циклом

for i in range (1,11):
    fack*=i
print(fack)

#A в степени B

def degree(a,b):
    if b==0:
        return 1
    else:
        return a*degree(a,b-1)

print(degree(5,2))

#циклом
deg=5
inc=2
for i in range (1,inc+1):
    deg*=2
print(deg)


