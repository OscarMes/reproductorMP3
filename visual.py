#esto fue un intento de usar un espectograma junto a las canciones
#no funcionó como esperaba ya que generaba lag y bugs

import librosa
import numpy as np
import tkinter as tk
import pygame
import threading


def fntControlTamano(valorMin, valorMax,valor):
    if valor < valorMin:
        return valorMin
    if valor > valorMax:
        return valorMax
    return valor

class ClsBarraAudio:
    def __init__(self,ventana,canvas,x,y,frecuencia,color,ancho=50,altoMin=10,altoMax=100,decibelMin=-80,decibelMax=0):
        self.ventana = ventana
        self.canvas, self.x, self.y, self.frecuencia = canvas,x,y,frecuencia
        self.color = color
        self.ancho, self.altoMin, self.altoMax = ancho,altoMin,altoMax
        self.alto = altoMin
        self.decibelMin, self.decibelMax = decibelMin,decibelMax
        self.representarDecibelios = (self.altoMax - self.altoMin)/(self.decibelMax - self.decibelMin)
        self.idRectang = None

    def fntActualizar(self,tiempoDiferencia, decibel):
        self.alturaDeseadaBarra = decibel * self.representarDecibelios + self.altoMax 
        self.velocidad = (self.alturaDeseadaBarra - self.alto)/0.1
        self.alto += self.velocidad * tiempoDiferencia
        self.alto = fntControlTamano(self.altoMin, self.altoMax, self.alto)

    def fntCrearBarras(self):
        if self.idRectang is not None:
            self.canvas.delete(self.idRectang)

        if self.ventana.winfo_exists() and self.ventana.winfo_ismapped():
            self.idRectang = self.canvas.create_rectangle(self.x,self.y + self.altoMax - self.alto, self.x + self.ancho, self.y + self.altoMax, fill=self.color)

class ClsEspectrograma:
    def __init__(self, cancion, canvas, ventana):
        self.ventana = ventana
        self.canvas = canvas
        self.serieTiempo, self.frecuenciaMuestreo = librosa.load(cancion)
        self.stft = np.abs(librosa.stft(self.serieTiempo,hop_length=512, n_fft=2048*4))
        self.espectrograma = librosa.amplitude_to_db(self.stft, ref=np.max)
        self.frecuencias = librosa.core.fft_frequencies(n_fft=2048*4)
        self.tiempos = librosa.core.frames_to_time(np.arange(self.espectrograma.shape[1]),sr=self.frecuenciaMuestreo,hop_length=512, n_fft=2048*4)
        self.indiceRelacionTiempo = len(self.tiempos)/self.tiempos[len(self.tiempos)-1]
        self.indiceRelacionFrecuencia = len(self.frecuencias)/self.frecuencias[len(self.frecuencias)-1]

        self.barras = []
        frecuencias = np.arange(100,8000,100)
        longitud = len(frecuencias)
        anchoCanvas = 380/longitud
        centrarBarras = (380 - anchoCanvas*longitud)/2

        for c in frecuencias:
            self.barras.append(ClsBarraAudio(self.ventana,self.canvas,centrarBarras,100,c,"#33FFC1", altoMax=300, ancho=anchoCanvas))
            centrarBarras += anchoCanvas
        
        self.tiempoTranscurrido = 0
        self.tiempoActualizarBarras = 0.01
        pygame.mixer.init()

        pygame.mixer.music.load(cancion)
        pygame.mixer.music.play(0)


    def fntObtenerDecibeles(self,tiempoObjetivo, frecuencia):
        return self.espectrograma[int(frecuencia*self.indiceRelacionFrecuencia)][int(tiempoObjetivo*self.indiceRelacionTiempo)]
        
    def fntEjecucion(self,controlHilo):
        if self.ventana.winfo_exists():
            while controlHilo == True:
                self.tiempoTranscurrido += self.tiempoActualizarBarras
                print("Hpta")
                for b in self.barras:
                    b.fntActualizar(self.tiempoActualizarBarras,self.fntObtenerDecibeles(pygame.mixer.music.get_pos()/1000.0,b.frecuencia))
                    b.fntCrearBarras()

        # else:
        #     pygame.mixer.music.stop()
            # if controlHilo == False:
            #     break
                #self.fntEjecucion(controlHilo=False)

        #     if self.ventana.winfo_exists():
        #         self.canvas.update()
        #     else:
        #         pygame.mixer.music.stop()
        #         self.ventana.destroy()
        #         break
        # if controlHilo == False:
        #     print("Si lo toma")
