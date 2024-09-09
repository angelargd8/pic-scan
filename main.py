import os
from PIL import Image
import pytesseract
#ruta a la carpeta de imagenes
folder1 = './src/pictures1'

def cargarImagenes(folder): 
    #lista de imagenes
    pictures = []
    #extensiones validas
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    #recorremos los archivos de la carpeta
    for file in os.listdir(folder):
        extension = os.path.splitext(file)[1].lower()
        if extension in valid_extensions: 
            picturePath = os.path.join(folder, file)
            picture = Image.open(picturePath)
            pictures.append(picture)
    print("la cantidad de imagenes cargadas es: ", len(pictures))

cargarImagenes(folder1)