#Reto 1 spiderman y distancias

distancia1 = 0
distancia2 = 0
distanciatotal = 0

distancia1 = int(input("Dime la distancia al punto 1:\n "))
distancia2 = int(input("Dime la distancia al punto 2:\n "))

if abs(distancia1)>abs(distancia2):
    if (distancia1>0 and distancia2>0):

      print("El mejor camino es ir primero al punto 2 y luego al punto 1")
      print("La distancia total es",abs(distancia1))
    else:
        if distancia1<0 and distancia2<0:
         print("El mejor camino es ir primero al punto 2 y luego al punto 1")
         print("La distancia total es",abs(distancia1))
        else:
            print("El mejor camino es ir primero al punto 2 y luego al punto 1")
            print("La distancia total es",abs(distancia1)+abs(distancia2)*2)


else:
      if (distancia1>0 and distancia2>0):

       print("El mejor camino es ir primero al punto 1 y luego al punto 2")
       print("La distancia total es",abs(distancia2))
      else:
         if distancia1<0 and distancia2<0:
           print("El mejor camino es ir primero al punto 1 y luego al punto 2")
           print("La distancia total es",abs(distancia2)) 
         else:
           print("El mejor camino es ir primero al punto 1 y luego al punto 2") 
           print("La distancia total es",abs(distancia1)*2+abs(distancia2)) 

 