#Este fue el primer reproductor que hice, usé este código para mejorarlo
#y crear algo menos feo 
#Este reproductor fue creado aproximadamente 2 años de haber creado el main
from tkinter import *
from tkinter import filedialog
#from mutagen.easyid3 import performer_set
import pygame 
from pygame import mixer 
from pygame import *


pygame.init()
mixer.init()
ventana_main = Tk()
ventana_main.title("Reproductor mp3")
ventana_main.geometry("700x500")
ventana_main.configure(bg="#299CB8")



def agregar():

    musica = filedialog.askopenfilenames(initialdir="C:/",title="selecciona las canciones", filetypes=(("mp3","*.mp3"),("all","*.*")))
    for canciones in musica:
        
        canciones = canciones.replace(".mp3","")

        pantalla.insert(END,canciones)
 

def play():
    canciones = pantalla.get(ACTIVE)
    canciones = f'{canciones}.mp3'

    mixer.music.load(canciones)
    mixer.music.play(loops=0)

def next():
    global proxima
    proxima = pantalla.curselection()
    proxima = proxima[0]+1
    canciones = pantalla.get(proxima)
    canciones = f"{canciones}.mp3"

    mixer.music.load(canciones)
    mixer.music.play(loops=0)

    pantalla.select_clear(0,END)
    pantalla.activate(proxima)

    last = None
    pantalla.select_set(proxima,last)

    if canciones == None:
        proxima = proxima[0]+1

    
def after():
    anterior = pantalla.curselection()
    anterior = anterior[0]-1
    canciones = pantalla.get(anterior)
    canciones = f"{canciones}.mp3"

    mixer.music.load(canciones)
    mixer.music.play(loops=0)

    pantalla.select_clear(0,END)
    pantalla.activate(anterior)

    last = None
    pantalla.select_set(anterior,last)



pantalla = Listbox(ventana_main,bg="#1F9E8B",width=50,selectbackground="#159D7C",
selectforeground="black")
pantalla.place(x=5,y=5,width=400,height=400)


botonera = Frame(ventana_main)
botonera.place(x=420,y=200)


reproducir = Button(botonera, text="Start",command=play)
reproducir.grid(row=2,column=1)

add_can = Button(botonera,text="agregar",fg="black",command=agregar)
add_can.grid(row=2,column=2)

siguiente = Button(botonera,text="siguiente",fg="black",command=next)
siguiente.grid(row=2,column=3)

anterior = Button(botonera,text="anterior",fg="black",command=after)
anterior.grid(row=2,column=4)

#descargar = Button(botonera,text="Descargar",fg="black",command= )
#descargar.grid(row=2,column=5)

ventana_main.mainloop()