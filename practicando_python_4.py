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
def es_vocal(c):
    return c.lower() in 'aeiou'

#ejemplo de uso
caracter = 'a'
print(f"¿'{caracter}' es una vocal?:", es_vocal(caracter))
caracter = 'b'
print(f"¿'{caracter}' es una vocal?:", es_vocal(caracter))
