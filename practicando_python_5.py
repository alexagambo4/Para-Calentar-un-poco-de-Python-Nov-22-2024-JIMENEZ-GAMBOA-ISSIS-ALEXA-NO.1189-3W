#imprime los datos de la autora 
print("Jimenez Gamboa Issis Alexa ")
print("no.1189")
print("3W")
#imprime linea en banco para qu se vea mas limpio
print("")
#imprime el titulo del prgrama 
print("Ejercicio no.1 ")
#Se deja una linea en blanco para q se vea mas limpio
print("")
def sum(lista):
    total = 0
    for num in lista:
        total += num
    return total

def multip(lista):
    total = 1
    for num in lista:
        total *= num
    return total

#ejemplo de uso
numeros = [1, 2, 3, 4]
print("La suma de la lista es:", sum(numeros))
print("La multiplicación de la lista es:", multip(numeros))
