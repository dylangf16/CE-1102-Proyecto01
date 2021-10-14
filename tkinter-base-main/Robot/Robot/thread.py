#           _____________________________
# __________/BIBLIOTECAS
from tkinter import *
from tkinter import messagebox
from threading import Thread
import os
import winsound
import sys
import serial
import time
import threading
import queue

sys.setrecursionlimit(10000000)


# -------------------------------------------------------

class myThread(threading.Thread):

    def __init__(self, myserial , queque):
        threading.Thread.__init__(self)
        self.queque = queque
        self.ser = myserial

    def run(self):
        while 1:
            if self.ser.readline() != None:
                #print("Leyendo")
                #print(self.ser.readline())

                if self.ser.readline() == b'IZQ\r\n':
                    #print("$$$$$$$$$$$$$$$$$PITILLO")
                    self.queque.put("IZQ")


# --------------------------------------------------------------------

class Robot:
    def __init__(self):
        self.miVentana = None
        self.ser = serial.Serial('COM3', 9600)
        self.botones = ""

    def update(self):
        while 1:
            if self.ser.readline() != None:
                #print(self.ser.readline())

                if self.ser.readline() == b'IZQ\r\n':
                    self.miVentana.right()





class GUI:
    def cargarImagen(self, nombre):
        ruta = os.path.join('Imagenes', nombre)
        imagen = PhotoImage(file=ruta)
        return imagen

    def __init__(self, master, myserial):
        # Crea la ventana principal
        self.master = master
        self.queque = queue.Queue()

        self.left_frames = ["W1L.png", "W2L.png", "W3L.png", "W4L.png"]
        self.right_frames = ["W1R.png", "W2R.png", "W3R.png", "W4R.png"]
        master.title("Azrael")
        master.minsize(1300, 800)
        master.resizable(width=NO, height=NO)

        self.pos = -1  # Variable de posicion
        self.x_azrael = 400  # posicion inicial en x del robot para left() y right()

        # Canvas donde estara el Robot
        self.fondo = Canvas(master, width=1300, height=800, bg="#000000")
        self.fondo.place(x=0, y=0)
        #           ____________________________
        # __________/Cargar una imagen de fondo
        # self.imagenFondo = self.cargarImagen("Front.png")
        # self.LabelFondo = Label(master, image=self.imagenFondo, bg="#FFFFFF")
        # self.LabelFondo.place(x=0, y=0)
        #           ______________________________
        # __________/Se crea el robot
        self.frame1 = self.cargarImagen("Front.png")
        self.azrael = Label(self.fondo, bg='white')
        self.azrael.config(image=self.frame1)
        self.azrael.image = self.frame1
        self.azrael.place(x=400, y=50)

        self.label_title = Label(master, text="Diseño del control:", fg="#ffffff", bg="#000000",
                                 font=("Eczar", 22, "bold"))
        self.label_title.place(x=90, y=650)

        #  AQUI VA UNA IMAGEN DEL CONTROL CON LOS BOTONES

        self.b1 = Button(self.master, text="Prueba right", command=self.right)
        self.b1.place(x=700, y=10)

        myThread(myserial, self.queque).start()
        self.updateMe()
        self.master.mainloop()

    def updateMe(self):
        #print("Entre al update")
        try:
            msg = self.queque.get(0)
            #print("Estoy aqui " + msg)
            if msg == "IZQ":
                self.right()
                print("$$$$")
                self.master.after(100, self.updateMe)
        except queue.Empty:
            pass
            #print("MAME VERGA")

        self.master.after(100, self.updateMe)


        #self.master.after()


    #           ______________________________
    # __________/Función que ejecuta que se mueva hacia la derecha


    def right(self):
        self.azrael.place(x=self.x_azrael, y=50)
        self.pos += 1
        self.x_azrael += 7
        if self.x_azrael == 399 or self.x_azrael in range(750, 757):
            self.pos = -1
            self.azrael.config(image=self.frame1)
            self.azrael.image = self.frame1
            return
        if self.x_azrael > 1220:
            self.pos = -1
            self.x_azrael = 0
        if self.pos == len(self.right_frames):
            self.pos = 0
        frame3 = self.cargarImagen(self.right_frames[self.pos])
        self.azrael.config(image=frame3)
        self.master.update()
        self.master.after(5, self.right)



    #def compare(self):
            #self.right()

#animation = Robot()
#arduino = Thread(target=animation.update, args=())
#arduino.start()
ser = serial.Serial('COM3', 9600, timeout=0, write_timeout=0)
root = Tk()
ventana_principal = GUI(root, ser)
root.mainloop()


