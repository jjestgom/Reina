import math

"""metodo round"""
print(round(1.3))
print(round(1.7))
print(round(1.5))

# metodo abs
print(abs(-77))  # siempre te va a dar el numero en positivo.


# metodo: ceil
print(math.ceil(1.1))  # toma el numero entero superior.

# metodo: floor
# lo va a llevar al numero entero mas cercano inferior.
print(math.floor(1.999999))

# metodo: isnan
print(math.isnan(23))  # no manda si el dato no es un numero y nos da "false"
# print(math.isnan("23")) #aqui nos da error por que solo podemos dar de dato un numero real.

# metodo: pow
print(math.pow(10, 3))  # eleva un numero 10**3
print(10**3)

# metodo:sqrt
print(math.sqrt(9))  # podemos sacar la raiz cuadrada.
