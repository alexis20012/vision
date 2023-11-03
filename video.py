import cv2
import matplotlib.pyplot as plt
import threading
import numpy as np


#crear el objeto que maneja videos
# un numero representa el dispositivo a usar (camara)
# el nombre de un archivo, el posible video
cap = cv2.VideoCapture("prueba.mp4")
#obtenemos la velocidad e los fotogramas
fps = cap.get(cv2.CAP_PROP_FPS)
print("FPS:",fps)
# El tama;o de video
fWidth = int(cap.get(3))
fHeight = int(cap.get(4))
tam = (fWidth,fHeight)
print("Tamano:", tam)
#Genera un objeto para guardar el video
resultado = cv2.VideoWriter('lll.mp4',cv2.VideoWriter_fourcc(*'mp4v'),fps,tam)
while True:
    #leer el dispositivo de entrada
    plt.grid ('True')
    ret, frame = cap.read()

    # configuramos el ploat con la funcio de ion que nos permite activar modo interactivo
    with plt.ion():
        cv2.imshow ("video", frame)
        plt.cla () #limpiamos los datos de la grafica
        b, g, r = cv2.split (frame)
        histograma = cv2.calcHist ([b], [0], None, [256], [0, 256])
        histograma1 = cv2.calcHist ([g], [0], None, [256], [0, 256])
        histograma2 = cv2.calcHist ([r], [0], None, [256], [0, 256])
        plt.setp (plt.plot (histograma), 'color', 'b', 'linewidth', 2.0)
        plt.setp (plt.plot (histograma1), 'color', 'g', 'linewidth', 2.0)
        plt.setp (plt.plot (histograma2), 'color', 'r', 'linewidth', 2.0)
        plt.title ("histograma de los colores")
        plt.legend ("BGR")
        plt.xlabel ("bits")
        plt.ylabel ("intencidad")
        plt.pause(0.00000001) #damos un tiempo de pausa para que pueda ser visible los cambios de la grafica
    #si ret es False, quiere decir que no se obtuvo informacion alguna
    if ret == False:
        break #entonces, se rompe y no hace nada
    # continua la logica del pograma
    #tamano del video
    height, width,_ = frame.shape
    # convertir a escala de gris
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #guardar
    resultado.write(frame)
    #mostrar

    #si se preciona una tecla, en este caos ESC sale del ciclo
    if cv2.waitKey(1) & 0xFF == 27:
        break
# una vez hecho todo, liberamos a Willy
# el video
cap.release()
#el archivo guardado
resultado.release()
# Cerrar todas las ventanas
cv2.destroyAllWindows()