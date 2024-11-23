#imprime los datos de la autora 
print("Jimenez Gamboa Issis Alexa ")
print("no.1189")
print("3W")
#imprime linea en banco para qu se vea mas limpio
print("")
#imprime el titulo del prgrama 
print("Ejercicio no.1 ")
#se deja una linea en blanco para que se vea mas limpio
print("")
def longitud(coleccion):
    contador = 0
    for _ in coleccion:
        contador += 1
    return contador

#ejemplo de uso
cadena = "Hola, mundo!"
lista = [1, 2, 3, 4, 5]
print("La longitud de la cadena es:", longitud(cadena))
print("La longitud de la lista es:", longitud(lista))
