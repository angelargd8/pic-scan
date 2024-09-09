import os
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

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
            pictures.append(picture) #guardar la imagen
    
    print("la cantidad de imagenes cargadas es: ", len(pictures))
    return pictures

#cargarImagenes(folder1)

def readPicture(pictures): 
    for picture in pictures: 
        print("imagen " + str(pictures.index(picture)+1))
        result = pytesseract.image_to_string(picture)
        print(result)

pictures = cargarImagenes(folder1)
readPicture(pictures)
