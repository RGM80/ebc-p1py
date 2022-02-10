'''for i in range(10):
    print(i)'''

'''def fun(n):
    for i in range(n):
        yield i

for v in fun(8):
    print(v)'''

'''''
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power 
        power *=2

t =  list(powers_of_2(3))
print(t)
'''
'''''
the_list = []
for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0 )

    print(the_list)
'''


two = lambda:2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))






