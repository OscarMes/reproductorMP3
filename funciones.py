from tkinter import filedialog, END, ACTIVE, Listbox
from pygame import mixer, base
import pygame
from figura import ClsFigura
import os 


class ClsFunciones:
    def __init__(self,listaElementos,ventana,canvas):
        self.ventana = ventana
        self.canvas = canvas
        self.listaElementos = listaElementos
        self.listaCanciones = []
        self.ultimaCancion = None
        pygame.init()
        mixer.init()
        
    def fntAgregar(self):

        self.canciones = filedialog.askopenfilenames(initialdir="C:/",title="Selecciona las canciones", filetypes=(("MP3","*.mp3"),("all","*.*")))
        for archivos in self.canciones:
            
            self.listaCanciones.append(archivos)
            archivos = archivos.replace(".mp3","")
       
            nuevoNombre = os.path.basename(archivos)

            self.listaElementos.insert(END,nuevoNombre)
        #print(self.listaCanciones)
            


    def fntRepoducir(self, estadoCancion):
        self.estadoCancion = estadoCancion

        #select_clear sirve para deseleccionar el último elemento antes seleccionado
        self.listaElementos.select_clear(0,END)
        #activate sirve para seleccionar y resaltar el elemento seleccionado
        self.listaElementos.activate(self.estadoCancion)
        #con selec_set selecciono el elemento de la lista
        self.listaElementos.select_set(self.estadoCancion,self.ultimaCancion)
        #selecciona la canción según la dirección que se le haya asignado

        #con get extraigo el texto del item seleccionado pero no lo necesito
        #self.seleccionarCancion = self.listaElementos.get(self.estadoCancion)
        self.seleccionarIndex = self.listaElementos.curselection()
        #if self.seleccionarIndex:
        self.seleccionarCancion = self.listaCanciones[self.seleccionarIndex[0]] 

        #print(self.seleccionarCancion)
        #self.seleccionarCancion = f"{self.seleccionarCancion}.mp3"

        #este es mi intento por usar un espectograma en mi reproductor
        # self.objBarras = ClsEspectrograma(self.seleccionarCancion,self.canvas, self.ventana)
        # self.threadBarras = threading.Thread(target=self.objBarras.fntEjecucion,args=(True,)
        # self.pool = ThreadPoolExecutor(max_workers=1)
        # self.pool.submit(self.objBarras.fntEjecucion,True )




        mixer.music.load(self.seleccionarCancion)
        mixer.music.play(loops=0)

        ClsFigura(self.canvas)

    def fntPausar(self):
        
        if pygame.mixer.music.get_busy() == True:
            pygame.mixer.music.pause()
            
        else:
            pygame.mixer.music.unpause()
  

                

    def fntAnteriorOSiguiente(self,direccion):

        #esto me indica que hay seleccionado
        siguienteCancion = self.listaElementos.curselection()
        if siguienteCancion:
            #aquí toma que dirección debe ir, si arriba o abajo
            siguienteCancion = siguienteCancion[0] + direccion
            #si al dar siguiente la lista se acaba se devuelve al primer elemento
            if siguienteCancion >= self.listaElementos.size():
                siguienteCancion = 0

            #esto toma el nombre del elemento de la lista 
            siguienteElemento = self.listaElementos.get(siguienteCancion)
            if siguienteElemento != "":
                
                self.fntRepoducir(siguienteCancion)
                
                

 



