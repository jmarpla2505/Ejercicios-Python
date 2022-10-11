#Tipos de datos y variables

#Numéricos
#enteros -- int
#real -- float
#Cadena de caracteres -- str
#Lógico -- bool

nombre = "José Ángel"
edad = 17
mayorOmenorEdad = False 

#Entrada y salida de datos
#Salida con print()
print("Buenos días", nombre,"tu edad es", edad)

#Entrada de datos -- input()
nombre = input("Dime tu nombre:\n ")

edad = input("Dime tu edad:\n ")

print("Buenos días", nombre,"tu edad es", edad)

#Bucle while

i = 0
numero = 0
numero = int(input("Dime un número:"))

while (i <= 10):
    print(numero, "*", i, "=", numero*i)
    i = i+1
