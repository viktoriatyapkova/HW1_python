x=int(input())
x1=x%50
x2=x1%10
a='I'
b='V'
c='X'
d='XC'
e='XL'
f='IX'
g='IV'
s=0
# Сначала вычисляем число десятков, далее узнаем число единиц, выводим полученные данные
if x==100:
    print('C')
else:
    if x<50:
        if x//10==4:
            if x%10==9:
                print(e+f)
            elif x%10==4:
                print(e+g)
            else:
                if x%10<4:
                     print(e+a*(x%10))
                else:
                    print(e+b+b+a*(x2%5))
        else:
            s+=x//10
            if x%10==9:
                print(s*c+f)
            elif x%10==4:
                print(s*c+g)
            else:
                if x%10<4:
                     print(s*c+a*(x%10))
                else:
                    print(s*c+b+a*(x2%5))
    else:
        if x//10==9:
            if x%10==9:
                print(d+f)
            elif x%10==4:
                print(d+g)
            else:
                if x%10<4:
                     print(d+a*(x%10))
                else:
                    print(d+b+b+a*(x2%5))
        else:
            s+=x1//10
            if x%10==9:
                print('L'+s*c+f)
            elif x%10==4:
                print('L'+s*c+g)
            else:
                if x%10<4:
                     print('L'+s*c+a*(x%10))
                else:
                    print('L'+s*c+b+a*(x2%5))
