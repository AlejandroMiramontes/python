#Ejercicio 1

nombre = input('¿Cuál es tu nombre?:')
apellido_paterno = input('¿Cuál es tu primer apellido?:')
apellido_materno= input('¿Cuál es tu segundo apellido?:')

from datetime import datetime
anio = input ('¿En qué año naciste?:')
anio_actual = 2023
nacimiento = input('¿En qué mes y día naciste? (en el siguiente formato “mm-dd”):')
fecha=datetime.strptime(nacimiento, "%m-%d")

nombre_completo = nombre + apellido_paterno + apellido_materno
vocales = ["a", "e", "i", "o", "u"]
contador = 0

for i in nombre_completo:
    if i in vocales:
        contador += 1
        
edad = ((int(anio_actual) - int(anio)))

print('Este es tu nombre completo en mayúsculas: ' + nombre.upper() + " " + apellido_paterno.upper() + " " +apellido_materno.upper())
print('Este es tu nombre completo en minúsculas: ' + nombre.lower() + " " + apellido_paterno.lower() + " " +apellido_materno.lower())
print('Esta es tu fecha de nacimiento: ' + str(fecha.day) + "-" + str(fecha.strftime("%m")) + "-"  + anio)
print("Esta es tu edad: " + str((int(anio_actual) - int(anio))))
print("Tu nombre completo tiene " + str(contador) + " vocales")
print("Tu nombre completo tiene " + str(len(nombre_completo)) + " letras")
print("¿Tu edad es un caracter de tipo número? " + str(isinstance(edad, int)))
print("¿Tu nombre completo es un carácter de tipo alfanumérico? " + str(nombre_completo.isalpha()))
print("Tu edad en 10 años será: " + str(edad + 10))
print("La media de tu edad actual y tu edad en 20 años es: " + str(((edad + 20) + edad)/2))