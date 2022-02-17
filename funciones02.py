""""
print("Se comienza aquí.")
message()
print("Se termina aquí.")


def message():
    print("Ingresa un valor: ")
"""
'''''
def message():
    print("Ingresa un valor: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())
'''
'''''
def hello(name):    # definiendo una función
    print("Hola,", name)    # cuerpo de la función


name = input("Ingresa tu nombre: ")

hello(name)    # invocación de la función

'''
'''''
hi()

def hi():
    print("¡Hola ese!")

'''
'''''
def hi():
    print("hola")

hi(5)
'''
'''''
def function(parameter):
    ###
'''
'''''
def message(what, number):
    print("Ingresa", what, "número", number)

message("teléfono", 11)
message("precio", 5)
message("número", "número")
'''
'''''
def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)
'''
'''''
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction("Juanita", "Skywalker")
introduction("Lolita", "Quick")
introduction("Lupita", "Kent")
'''
'''''
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")

'''

def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction(first_name = "Juancho", last_name = "Bond")
introduction(last_name = "Poncho", first_name = "Luke")
