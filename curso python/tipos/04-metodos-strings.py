nombre = "juan jose"
apellido = "estevez"
nombre_completo = f"{nombre} {apellido}"
print(f"nombre completo: {nombre_completo}")


animal = "  la vera es una PERRITA MARAVILLOSA y el leo es un PERrito CAsi MaraVIlloso (es broma) "

print(animal.upper())  # transforma toda la variable en mayuscula.
# lo pone todo en minuscula y la primela letra en mayuscula
print(animal.capitalize())
print(animal.lower())  # lo pone todo en minuscula
# todo en minuscula y primera letra de todas en mayuscula.
print(animal.title())

print(animal.strip())
print(animal.strip().capitalize())

print(animal.lstrip())  # quita los espacios de la izquierza.
print(animal.rstrip())  # quita los espacios de la derecha.

print(animal.find("le"))
print(animal.replace("CAsi", "tambien"))
print("leo" in animal)
print("leo" not in animal)
