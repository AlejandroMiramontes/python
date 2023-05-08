#Fórmula para calcular el área de un círculo: A=pi*(r**2)
#Fórmula para calcular el volúmen de un cilindro: V=pi*(r**2)*h

def volumen_cilindro():
    altura=input("Escribe la altura: ")
    def area_circulo():
        radio=input("Escribe el radio: ")
        area=(3.1416)*(int(radio)**2)
        print(f"El área del círculo es: {area}")
        return area
    volumen=area_circulo()*(int(altura))
    print(f"El volúmen del cilindro es: {volumen}")

volumen_cilindro()