#imprime los datos de la autora 
print("Jimenez Gamboa Issis Alexa ")
print("no.1189")
print("3W")
#imprime linea en banco para qu se vea mas limpio
print("")
#imprime el titulo del prgrama 
print("Ejercicio no.1 ")
#se deja ua linea enlanco para que se vea mas limpio
print("")
def max_de_tres(a, b, c):
    return max(max(a, b), c)

#ejemplo de uso
num1 = 5
num2 = 15
num3 = 10
print("El mayor de", num1, ",", num2, "y", num3, "es:", max_de_tres(num1, num2, num3))
