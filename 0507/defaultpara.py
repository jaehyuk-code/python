def func3(a=1, b=1):
       c = a + b
       return c

a = 6
b =func3(a,5)
print(b)
b = func3(a,1)
print(b)
b = func3(a)
print(b)
b = func3()
print(b)
