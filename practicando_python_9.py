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
def generar_n_caracteres(n, caracter):
    return caracter * n

#ejemplo de uso
n = 5
caracter = "x"
print(f"Generando {n} caracteres '{caracter}':", generar_n_caracteres(n, caracter))
