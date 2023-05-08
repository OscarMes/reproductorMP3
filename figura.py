from tkinter import *

class ClsFigura:
    def __init__(self,canvas):
        #el atributo canvas fue pasado desde la clase ClsFunciones
        #que fue pasado desde la clase ClsConsola, para que el canva 
        self.canvas = canvas
        self.circulo = self.canvas.create_oval(190,175,175,190, fill="")
        self.velocidadX = 5
        self.velocidadY = 5
        self.aceleracion = 0
        #debo llamar a fntMovimieneto desde el init para no tener que 
        #estar instanciando en el otro archivo la clase y despues la función
        self.fntMovimiento()

    def fntMovimiento(self):
        moviento = self.canvas.move(self.circulo,self.velocidadX,self.velocidadY)
        limiteIzquiero,limiteArriba,limiteDerecho,limiteAbajo = self.canvas.coords(self.circulo)
      
        if limiteIzquiero <= 0 or limiteDerecho > self.canvas.winfo_width(): 
            self.velocidadX *= -1

        if limiteArriba <= 0 or limiteAbajo > self.canvas.winfo_height():
            self.velocidadY *= -1
           


  
      
        self.canvas.after(60,self.fntMovimiento)
