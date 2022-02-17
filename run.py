'''''
def fun(in=2, out=3):
    return in * out
print(fun(3))
'''
''''
tup = (1, ) + (1, 1)
tup = tup + tup 
print(len(tup))
'''
try:
    first_prompt = input("ingresa el primer valor")
    a = len(first_prompt)
    second_prompt = input("ingresa el segundo valor: ")
    b = len(second_prompt) * 2
    print(a/b)
except zerodivisionerror:
    print("¡no divida entre cero: ")
except ValueError:
    print("valor incorrecto")
except:
    print("error.error.error.")
