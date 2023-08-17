#import math

#raiz = math.sqrt(3249)

#print(raiz)

#import Uteis

#gato = Uteis.desenhar_gato()

#print(gato)


#from Uteis import *

#pizza = emoji_pizza()

#print(pizza)

#from Pacotes import OpMat

#raiz = OpMat.raiz_quadrada(3249)

#print(raiz)

#from Pacotes.Datas import *

#desenho = Desenho.desenhar_peixe()

#print(desenho)

#from googletrans import Translator

#tradutor = Translator()

#texto = str(input('Digite um texto:'))
#ingles = tradutor.translate(texto,dest='en')
#print("Tradução: ", ingles.text)

import cv2

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) == ord ('q'):
        break

camera.release()
cv2.destroyALLWindows()