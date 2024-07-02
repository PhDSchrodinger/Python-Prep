def crearDiccionario(lista):

    if not isinstance(lista, list):
        raise TypeError("El argumento debe ser una lista")
    
    for numero in lista:
        if not isinstance(numero, int):
            raise TypeError("La lista solo puede contener números enteros")
    
    multiplos3 = [numero for numero in lista if numero % 3 == 0]
    cuadrados = [numero**2 for numero in lista]
    promedio = sum(lista) / len(lista)

    diccionario = {
        "multiplos3":multiplos3,
        "cuadrados":cuadrados
    }
    return diccionario

#Ejemplo de uso

crearDiccionario([3,6,7,12])
crearDiccionario["Hola",3,"Mundo",7]