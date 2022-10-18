

palabrasecreta = "juan"
i = 0
 
while(palabrasecreta!="casa"):
    palabrasecreta = input("Dime la contraseña:")
    i=i+1
    if i>=3:
        print("Te has quedado sin intentos")
        exit()
if (palabrasecreta == "casa"): 
 print("Enhorabuena, has adivinado la contraseña")

