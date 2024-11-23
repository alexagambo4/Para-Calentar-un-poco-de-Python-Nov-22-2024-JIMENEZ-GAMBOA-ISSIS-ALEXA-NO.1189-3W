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
def superposicion(lista1, lista2):
    for i in lista1:
        for j in lista2:
            if i == j:
                return True
    return False

#ejemplo de uso
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 3, 7]
print("¿Tienen las listas una superposición?", superposicion(lista1, lista2))
