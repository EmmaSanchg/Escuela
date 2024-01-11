edad = 17
limite_edad = 22
estudiante = True

pase = (edad >= limite_edad) and (estudiante)

print(pase)
# False

pase = (edad >= limite_edad) or (estudiante)
print(pase)
# True

pase = not( (edad >= limite_edad) and (estudiante) )
print(pase)
# True

pase = not( (edad >= limite_edad) or (estudiante) )
print(pase)
# False