def separa_palabras():
    frase=input("Escribe una frase: ")
    frase_list = frase.split()
    diccionario = dict()
    for palabra in frase_list:
        diccionario[palabra] = len(palabra)
    print(diccionario)

separa_palabras()