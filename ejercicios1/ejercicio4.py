# funciones
def mifuncion():
    print("Mi primer función")

mifuncion()

def mifuncion(var1):
    print("Mi primer función " + var1)

mifuncion("llamada")

# funciones

def mifuncion():
    print("Mi primer función")

def mifuncion2(var1):
    print("Mi primer función " + var1)

mifuncion()
mifuncion2("llamada")

# funciones con argumentos variables

def mifuncion3(*vars):
    print("Mi primer función " + vars[1])

mifuncion3("primero","segundo","tercero")
mifuncion3("primero","segundo")

def mifuncion4(var3, var2, var1):
    print("Mi primer función " + var3)

mifuncion4(var1="primero", var3="tercero", var2="segundo")

def mifuncion5(**vars):
    print("Mi primer función " + vars["var1"])

mifuncion5(var1="primero", var2="segundo")

# funciones con argumento con valor por defecto

def mifuncion6(var1="primero"):
    print("Mi primer función " + var1)

mifuncion6("segundo")
mifuncion6()

# retorno de una funcion

def mifuncion7(var):
    return var +10

x=mifuncion7(5)
print(x)

# funcion lambda (es una función anónima)

x = lambda a : a + 10
print( x(5) )
x = lambda a, b : a * b
print( x(5,6) )

def mifuncionl(n):
    return lambda a : a * n

md = mifuncionl(2)
print( md(11) )
