#Funciones definidas por el usuario

from pytube import YouTube
"""""
def numerosenteros(numero1:int, numero2:int):
    #print("La suma es", numero1+numero2)
    return numero1+numero2


suma = numerosenteros(1,2)
print("La suma es:", suma)
"""
def descargaCancion(url:str):
    youtube = YouTube(url)
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion = youtube.streams.get_audio_only()
    cancion.download()

descargaCancion("https://www.youtube.com/watch?v=VL1r5KOE6nc")
