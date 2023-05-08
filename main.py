from tkinter import *
import PIL.Image
import PIL.ImageTk
from funciones import ClsFunciones


#Creo una clase botón para crear los botones de la consola 
class ClsBoton:
    #los objetos de la clase deben pasar los siguientes atributos
    def __init__(self,imagen,posicion,funcion,frmBotonera):
        self.imagen = imagen
        self.posicion = posicion
        self.funcion = funcion
        #manipulo las imagenes con PIL 
        self.selcImagen = PIL.Image.open(self.imagen)
        self.selcImagen = self.selcImagen.resize((self.selcImagen.width // 12, self.selcImagen.height // 12))
        self.imgBoton = PIL.ImageTk.PhotoImage(self.selcImagen)
        self.btnBotones = Button(frmBotonera,bg="#299CB8", image=self.imgBoton, borderwidth=0, height= 40, width= 40,activebackground="#299CB8", command=self.funcion)
        self.btnBotones.grid(row= int(self.posicion[0]), column = int(self.posicion[1]))
    


#mi clase para la ventana tkinter
class ClsConsola:
    def __init__(self):
        self.ventana = Tk()
        #desactivo el maximizar
        self.ventana.resizable(False,False)
        self.ventana.title("Consola de Musica MP3") 
        self.ventana.geometry("700x500")
        self.ventana.configure(bg="#299CB8")
        
        self.canvas = Canvas(self.ventana, width=380,height=350)
        self.canvas.place(y=5,x=5)
        #llamo a los componentes dentro del bucle principal de la ventana
        self.fntcomponentes()

        self.ventana.mainloop()
    
    def fntcomponentes(self):
      
        #listaElementos es un listBox
        self.listaElementos = Listbox(self.ventana,bg="#1F9E8B",width=50,
                                      selectbackground="#159D7C",
                                    selectforeground="black", font=15)
        self.listaElementos.place(x=395,y=5,width=300,height=400)

        #Un frame sencillo para ubicar los botones
        self.frmBotonera = Frame(self.ventana)
        self.frmBotonera.place(x=250,y=410)

        #instancio la clase funciones del otro archivo para pasarle los elementos 
        #necesarios y que me maneje esos elementos desde allá
        objClsFunciones = ClsFunciones(self.listaElementos,self.ventana,self.canvas) 

        #aquí se ponen los objetos de los botones junto con sus parametros
        self.btnAtras = ClsBoton(imagen="icons/back.png",posicion=(1,1),funcion=lambda:objClsFunciones.fntAnteriorOSiguiente(-1) ,frmBotonera= self.frmBotonera)
        self.btnReproducir = ClsBoton(imagen="icons/play.png",posicion=(1,2),funcion=lambda: objClsFunciones.fntRepoducir(ACTIVE),frmBotonera= self.frmBotonera)
        self.btnPausar = ClsBoton(imagen="icons/pause.png",posicion=(1,3),funcion=objClsFunciones.fntPausar ,frmBotonera= self.frmBotonera)
        self.btnSiguiente  = ClsBoton(imagen="icons/next.png",posicion=(1,4),funcion=lambda:objClsFunciones.fntAnteriorOSiguiente(+1) ,frmBotonera= self.frmBotonera)
        self.btnAgregar = ClsBoton(imagen="icons/add.png",posicion=(1,5),funcion=objClsFunciones.fntAgregar  ,frmBotonera= self.frmBotonera)

#solo si el archivo es ejecutado desde acá se puede llamar a la clase
#ClsConsola 
if __name__ == '__main__':
    #Nota: cuando la clase recibe atributos desde el init se debe llamar
    #con "()" al final
    objConsola = ClsConsola()   