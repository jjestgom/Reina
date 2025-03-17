# tipos de operadores basicos

a = 2+3
b = 12-3
c = 12*2
d = 9/3
e = 9//3  # realiza la division con resultado de numero entero.
f = 16 % 2  # proporciona el resto de una division
print(f)
print(a)
g = 5**2
print(g)


# tipos operadores relacionales.
""" se emple para comparar y
establecer la relacion
entre ellos. devuelve un valor booleano."""

5 < 8
7 > 2
8 == 7
8 == 8
8 <= 0
2 >= 2
7 != 6  # devuelve true si ambos operandos no son iguales.
print(6 == 8)


# operadores bit a bit.
"""realiza operaciones en los
operandos bit a bit."""


print(f"10+3={10+3}")


# estructura de control
# condicionales.
my_string = "juan josee"

if my_string == "juanjo":
    print("my_string es 'juanjo'")
elif my_string == "juan jose":
    print("my_string es 'juan jose'")
else:
    print("my_string no es 'juanjo'")
    print("my_string no es 'juan jose'")


# iteractivas

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

# excepciones
try:
    print(10/0)
except:
    print("se ha producido un error")
finally:
    print("ha finalizado el manejo de exepciones")


for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
