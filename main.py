import os
from PIL import Image
import pytesseract
import cv2
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#ruta a la carpeta de imagenes
folder2 = './src/pictures2'

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
            #picture = Image.open(picturePath)
            picture = cv2.imread(picturePath)
            pictures.append(picture) #guardar la imagen
    
    print("la cantidad de imagenes cargadas es: ", len(pictures))
    return pictures

#cargarImagenes(folder1)

def readPicture(pictures): 
    for picture in pictures: 
        #convertir a escala de grises
        picture = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
        #aplicar umbral
        #_, picture = cv2.threshold(picture, 150, 255, cv2.THRESH_BINARY)
        text = pytesseract.image_to_string(picture, lang='spa')
        print(text)
        #print("imagen " + str(pictures.index(picture)+1))
        #result = pytesseract.image_to_string(picture)
        #print(result)
        return text

pictures = cargarImagenes(folder2)
resultado = readPicture(pictures)

#convertir los datos
data = resultado.split('\n')
data = [d.split() for d in data]
print("datos: ")
#print(data)
data = pd.DataFrame(data)
print(data)
data.to_csv('data.csv', index=False, header=False)