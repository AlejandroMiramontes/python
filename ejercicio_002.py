nombre=input('¿Cuál es tu nombre? ')

#Valida si el nombre escrito es válido
if nombre.isalpha() is True: # El método isalpha() regresa True si todos los caracteres son letras del alfabeto (a-z).
    inicial=nombre[0:1].lower()
else:
    print("Por favor revisa el nombre escrito.")
    exit()
    
sexo=input('¿Cuál es tu sexo? (hombre o mujer) ')

#Valida si el sexo es válido
if sexo.isalpha() is True:
    inicial_sexo=sexo[0:1].lower()
else:
    print("Por favor revisa el sexo")
    exit()
        
if not (str(sexo).lower() == 'mujer' or str(sexo).lower() == 'hombre'):
    print ("El sexo escrito no existe")
    exit()

#Validaciones para la separación de grupos
if str(inicial) < 'm' and str(inicial_sexo) == 'm':
    print("Tu grupo es el grupo A")
elif str(inicial) > 'n' and str(inicial_sexo) == 'h':
    print("Tu grupo es el grupo A")
else:
    print("Tu grupo es el grupo B")