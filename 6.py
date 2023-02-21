a = float (input())
b = float (input())
c = float (input())
d = (b ** 2) - (4 * a * c)
x1 = (-b + (d ** 0.5)) / (2*a)
x2 = (-b - (d ** 0.5)) / (2*a)
if (-b + (d ** 0.5))  % (2*a) != 0  and (-b - (d ** 0.5)) %  (2*a) != 0:
    print (x1, x2)
elif (-b + (d ** 0.5))  % (2*a) == 0  and (-b - (d ** 0.5)) %  (2*a) != 0:
    print (x2)
elif  (-b + (d ** 0.5))  % (2*a) != 0  and (-b - (d ** 0.5)) %  (2*a) == 0:
    print (x1)
else:
    print(0)