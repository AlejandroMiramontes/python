diccionario = {
  "platano": 1.35,
  "manzana": 0.80,
  "pera": 0.85,
  "naranja": 0.70
}
#print(diccionario)
fruta=input("Escribe una fruta: ").lower()
if fruta not in diccionario:
    print(f"Fruta inválida, las opciones son: ")
    for keys, value in diccionario.items():
        print(keys)
else:
    kilos=input("¿Cuántos kilos quieres? ")
    if fruta.lower() == 'platano':
        total = (int(kilos) * diccionario["platano"])
        print(total)
    elif fruta.lower() == 'manzana':
        total = (int(kilos) * diccionario["manzana"])
        print(total)
    elif fruta.lower() == 'pera':
        total = (int(kilos) * diccionario["pera"])
        print(total)
    else:
        total = (int(kilos) * diccionario["naranja"])
        print(total)