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
def es_palindromo(palabra):
    return palabra == palabra[::-1]

#ejemplo de uso
palabra1 = "radar"
palabra2 = "hola"
print(f"¿'{palabra1}' es un palíndromo?:", es_palindromo(palabra1))
print(f"¿'{palabra2}' es un palíndromo?:", es_palindromo(palabra2))
