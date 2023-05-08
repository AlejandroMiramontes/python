contra="Welcome1!"
contador=1
while contador != 2: 
    contra_usr=input("por favor escribe la contraseña: ")
    if contra_usr != contra:
        print("¡La contraseña es incorrecta!")
    else:
        print("¡Contraseña válida!")
        contador+=1
exit()