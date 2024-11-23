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
def procedimiento(lista):
    for num in lista:
        # Imprimir una línea de asteriscos, cuya longitud es igual al número
        print('*' * num)

#ejemplo de uso
numeros = [3, 5, 1, 7, 4]
procedimiento(numeros)
