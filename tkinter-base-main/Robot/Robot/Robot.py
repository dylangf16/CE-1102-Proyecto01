#           _____________________________
#__________/BIBLIOTECAS
from tkinter import *
from tkinter import messagebox
from threading import Thread
import os
import winsound
import sys
import pickle


#           ____________________________
#__________/Código


sys.setrecursionlimit(100000) #Se incrementa el limite de recursion para evitar errores y poder usar el programa de
                              #manera continua

#           ____________________________
#__________/Ventana Principal
ventana_principal = Tk()
ventana_principal.title("Bienvenidos")
ventana_principal.minsize(640, 480)
ventana_principal.resizable(width=NO, height=NO)

#           ______________________________
#__________/Se crea un lienzo para objetos
contenedor_principal = Canvas(ventana_principal, width=640, height=480, bg="#000000")
contenedor_principal.place(x=0, y=0)

#           ____________________________
#__________/Variables globales
pos = -1 #Variable de posicion
rep = -1 #Variable de repeticion
user_entry = StringVar() #Variable para el entry
x_azrael = 570 #posicion inicial en x del robot para left() y right()
energy = IntVar() #Variable de energia que debe ser un numero


def dont():
    print("0")


#           ____________________________
#__________/Función para cargar imagenes
def cargarImagen(nombre):
    ruta = os.path.join('Imagenes', nombre)
    imagen = PhotoImage(file=ruta)
    return imagen

#           ____________________________
#__________/Se cargan los archivos de audio
def song_dance():#audio cuando baila
    winsound.PlaySound('dance.wav', winsound.SND_ASYNC)


def song_hello():#audio cuando saluda
    winsound.PlaySound('bello.wav', winsound.SND_ASYNC)


def song_built():#audio cuando dice su fecha de creacion
    winsound.PlaySound('built.wav', winsound.SND_ASYNC)


def song_cry():#audio cuando llora
    winsound.PlaySound('cry.wav', winsound.SND_ASYNC)


def song_own1():#audio cuando va a la playa
    winsound.PlaySound('beach.wav', winsound.SND_ASYNC)


def song_own2():#audio cuando entrega su corazon
    winsound.PlaySound('kiss.wav', winsound.SND_ASYNC)


def song_smile():#audio cuando rie
    winsound.PlaySound('smile.wav', winsound.SND_ASYNC)


def song_music():#audio cuando baila
    winsound.PlaySound('dance.wav', winsound.SND_ASYNC | winsound.SND_LOOP)


def song_alert():#audio cuando la energia esta baja
    winsound.PlaySound('alert.wav', winsound.SND_ASYNC)

#           ____________________________
#__________/Cargar una imagen de fondo
imagenFondo = cargarImagen("logo.png")
LabelFondo = Label(contenedor_principal, image=imagenFondo, bg="#FFFFFF")
LabelFondo.place(x=0, y=0)

#           ____________________________
#__________/Crear una nueva ventana
def VentanaRobot():
    ventana_principal.withdraw()
    ventanarobot = Toplevel()
    ventanarobot.title("Azrael")
    ventanarobot.minsize(1580, 988)
    ventanarobot.resizable(width=NO, height=NO)

    #Canvas donde estara el Robot
    fondo = Canvas(ventanarobot, width=1580, height=988, bg="#ffffff")
    fondo.place(x=0, y=0)

    #           ______________________________
    # __________/Se crean listas con nombre de las fotos para las animaciones
    cry_frames = ["Cry2.png", "Cry3.png", "Cry4.png", "Cry5.png", "Cry1.png"]

    hello_frames = ["Hello1.png", "Hello2.png", "Hello3.png", "Hello4.png", "Hello5.png", "Hello6.png", "Hello7.png",
                    "Hello8.png", "Hello9.png", "Hello10.png", "Hello11.png", "Hello12.png", "Hello13.png",
                    "Hello13.png",
                    "Cry1.png"]

    built_frames = ["Built.png", "Cry1.png"]

    smile_frames = ["Smile1.png", "Smile2.png", "Smile3.png", "Smile4.png", "Smile5.png", "Smile6.png", "Cry1.png"]

    move_frames = ["Move1.png", "Move2.png", "Move3.png", "Move4.png"]

    dance_frames = ["Dance1.png", "Dance2.png", "Dance1.png", "Dance2.png", "Dance3.png", "Dance4.png", "Dance5.png",
                    "Dance6.png", "Dance7.png", "Dance8.png", "Dance9.png", "Dance10.png", "Dance11.png", "Dance12.png",
                    "Dance1.png", "Dance2.png", "Dance8.png", "Dance9.png", "Dance10.png", "Dance11.png", "Dance12.png",
                    "Dance1.png", "Dance2.png", "Dance1.png", "Dance2.png", "Dance3.png", "Dance4.png", "Dance5.png",
                    "Dance6.png", "Dance7.png", "Dance8.png", "Dance9.png", "Dance10.png", "Dance11.png", "Dance12.png",
                    "Dance1.png", "Dance2.png", "Dance8.png", "Dance9.png", "Dance10.png", "Dance11.png", "Dance12.png",
                    "Cry1.png"]

    music_frame = "Play.png"

    beach_frames = ["Beach2.png", "Beach3.png", "Beach4.png", "Cry1.png"]

    kiss_frames = ["Kiss1.png", "Kiss2.png", "Kiss3.png", "Kiss4.png", "Kiss5.png", "Kiss6.png", "Kiss7.png",
                   "Kiss8.png", "Kiss9.png", "Cry1.png"]

    goahead_frames = ["10Cry.png", "20Cry.png", "30Cry.png", "Cry1.png"]

    goback_frames = ["Cry80.png", "Cry50.png", "Cry30.png", "Cry1.png"]

    #           ______________________________
    # __________/Se crea el robot
    frame1 = cargarImagen("Cry1.png")
    azrael = Label(fondo, bg='white')
    azrael.config(image=frame1)
    azrael.image = frame1
    azrael.place(x=570, y=110)

    #           ______________________________
    # __________/Se crea un lista con nombre de fotos para la bateria
    battery_status = ["zero.png", "20%.png", "40%.png", "70%.png", "full.png"]

    #           ______________________________
    # __________/Se crea la batería
    bat_leak = cargarImagen("bat.png")
    battery = Label(fondo, bg="#ffffff")
    battery.config(image=bat_leak)
    battery.image = bat_leak
    battery.place(x=1450, y=10)
    messagebox.showinfo("Bienvenido", "Por favor utilice power(#) para darle energia a Azrael")#Se crea un mensaje inicial para que el usuario de energia


    #Funcion que revisa el nivel de energia, la indica si el usuario la pide y alerta si la energia es menor a 20
    def status():
        global energy
        if energy > 20:
            return messagebox.showinfo("Estatus de Azrael", "La energia actual es " + str(energy))
        if 20 >= energy > 1:
            return low_energy()
        if energy == 1:
            return zero_energy()


    #funcion que revisa el nivel de energia y cambia la imagen de la bateria, ademas alerta si es menor que 20 o igual a 1 y cierra la ventana si es 0
    def battery_level():
        global energy
        if isinstance(energy, int) and 0 <= energy <= 100:
            if 70 < energy <= 100:
                level_100 = cargarImagen(battery_status[4])
                battery.config(image=level_100)
                battery.image = level_100
                return
            if 40 < energy <= 70:
                level_70 = cargarImagen(battery_status[3])
                battery.config(image=level_70)
                battery.image = level_70
                return
            if 20 < energy <= 40:
                level_40 = cargarImagen(battery_status[2])
                battery.config(image=level_40)
                battery.image = level_40
                return
            if 1 < energy <= 20:
                level_20 = cargarImagen(battery_status[1])
                battery.config(image=level_20)
                battery.image = level_20
                return
            if energy == 1:
                level_zero = cargarImagen(battery_status[0])
                battery.config(image=level_zero)
                battery.image = level_zero
                zero_energy()
                return
        elif energy < 0:
            return regresar()
        else:
            return energy_warning()
        ventanarobot.mainloop()

    #Cambia el valor de la energia por la entrada del usuario
    def power(n):
        global energy
        energy = int(str(n))
        battery_level()
        ventanarobot.mainloop()

    #Alerta cuando solo queda 1% de energia restante
    def zero_energy():
        return messagebox.showerror("ALERTA Batería 1%", "Por favor aumente el nivel de batería con el comando power(n)")

    #Alerta cuando la energia es menor que 20 con sonido
    def low_energy():
        global energy
        s = Thread(target=song_alert, args=())
        s.start()
        messagebox.showwarning("Energia Baja", "Azrael tiene " + str(energy) + " de energía")
        ventanarobot.mainloop()

    #Mensaje cuando el usuario ingresa un valor que no esta entre 0 y 100
    def energy_warning():
        return messagebox.showwarning("Error", "El valor de energía debe estar entre 100 y 0 para que Azrael pueda "
                                               "funcionar")

    #Mensaje cuando el usuario ingrese un comando que no existe
    def misscommand():
        return messagebox.showerror("Error", "Por favor digite un comando valido")

    #           ___________________________________
    # __________/Función que ejecuta la animacion para que llore
    def cry():
        global energy
        energy -= 1
        battery_level()
        s = Thread(target=song_cry, args=())
        s.start()
        cry_aux()
        ventanarobot.mainloop()

    def cry_aux():
        global pos
        global rep
        pos += 1
        rep += 1
        if rep > 4:
            pos = -1
            rep = -1
            return
        if pos == len(cry_frames):
            pos = 0
        frame2 = cargarImagen(cry_frames[pos])
        azrael.config(image=frame2)
        ventanarobot.after(430, cry_aux)
        ventanarobot.mainloop()

    #           ___________________________________
    # __________/Función que ejecuta la animacion para que salude
    def hello():
        global energy
        energy -= 1
        battery_level()
        s = Thread(target=song_hello, args=())
        s.start()
        hello_aux()
        ventanarobot.mainloop()

    def hello_aux():
        global pos
        global rep
        pos += 1
        rep += 1
        if rep > 14:
            pos = -1
            rep = -1
            return
        if pos == len(hello_frames):
            pos = 0
        frame2 = cargarImagen(hello_frames[pos])
        azrael.config(image=frame2)
        ventanarobot.after(270, hello_aux)
        ventanarobot.mainloop()

    #           ___________________________________
    # __________/Función que ejecuta la aniamcion para que muestre su fecha de creacion
    def built():
        global energy
        energy -= 1
        battery_level()
        s = Thread(target=song_built, args=())
        s.start()
        built_aux()
        ventanarobot.mainloop()

    def built_aux():
        global pos
        global rep
        pos += 1
        rep += 1
        if rep > 1:
            pos = -1
            rep = -1
            return
        if pos == len(built_frames):
            pos = 0
        frame2 = cargarImagen(built_frames[pos])
        azrael.config(image=frame2)
        ventanarobot.after(1700, built_aux)
        ventanarobot.mainloop()

    #           ___________________________________
    # __________/Función que ejecuta la animacion para que ria
    def smile():
        s = Thread(target=song_smile, args=())
        s.start()
        smile_aux()
        ventanarobot.mainloop()


    def smile_aux():
        global pos
        global rep
        pos += 1
        rep += 1
        if rep > 6:
            pos = -1
            rep = -1
            return
        if pos == len(smile_frames):
            pos = 0
        frame3 = cargarImagen(smile_frames[pos])
        azrael.config(image=frame3)
        ventanarobot.after(300, smile_aux)
        ventanarobot.mainloop()

    #           ___________________________________
    # __________/Función que ejecuta la animacion para que se mueve a la derecha
    def right():
        global energy
        right_aux()
        energy -= 1
        battery_level()
        ventanarobot.mainloop()

    def right_aux():
        global x_azrael
        global pos
        azrael.place(x=x_azrael, y=110)
        pos += 1
        x_azrael += 7
        if x_azrael == 563:
            pos = -1
            frame = cargarImagen(built_frames[1])
            azrael.config(image=frame)
            azrael.image = frame
            return
        if x_azrael >= 970:
            pos = -1
            frame5 = cargarImagen(built_frames[1])
            azrael.config(image=frame5)
            azrael.image = frame5
            return
        if pos == len(move_frames):
            pos = 0
        frame3 = cargarImagen(move_frames[pos])
        azrael.config(image=frame3)
        ventanarobot.after(10, right)
        ventanarobot.mainloop()

    #           ___________________________________
    # __________/Función que ejecuta la animacion para que se mueva a la izquierda
    def left():
        global energy
        left_aux()
        energy -= 1
        battery_level()
        ventanarobot.mainloop()

    def left_aux():
        global x_azrael
        global pos
        azrael.place(x=x_azrael, y=110)
        pos += 1
        x_azrael -= 7
        if x_azrael == 577:
            pos = -1
            frame = cargarImagen(built_frames[1])
            azrael.config(image=frame)
            azrael.image = frame
            return
        if x_azrael <= 170:
            pos = -1
            frame4 = cargarImagen(built_frames[1])
            azrael.config(image=frame4)
            azrael.image = frame4
            return
        if pos == len(move_frames):
            pos = 0
        frame3 = cargarImagen(move_frames[pos])
        azrael.config(image=frame3)
        ventanarobot.after(10, left)
        ventanarobot.mainloop()

    #           ___________________________________
    # __________/Función que ejecuta la animacion para que baile
    def dance():
        global energy
        energy -= 2
        battery_level()
        s = Thread(target=song_dance, args=())
        s.start()
        dance_aux()
        ventanarobot.mainloop()

    def dance_aux():
        global pos
        global rep
        pos += 1
        rep += 1
        if rep > 42:
            pos = -1
            rep = -1
            return
        if pos == len(dance_frames):
            pos = 0
        frame3 = cargarImagen(dance_frames[pos])
        azrael.config(image=frame3)
        ventanarobot.after(127, dance_aux)
        ventanarobot.mainloop()

    #           ___________________________________
    # __________/Función que ejecuta la animacion para que vaya a la playa
    def own1():
        global energy
        energy -= 3
        battery_level()
        s = Thread(target=song_own1, args=())
        s.start()
        own1_aux()
        ventanarobot.mainloop()

    def own1_aux():
        global pos
        global rep
        pos += 1
        rep += 1
        if rep > 3:
            pos = -1
            rep = -1
            return
        if pos == len(beach_frames):
            pos = 0
        frame3 = cargarImagen(beach_frames[pos])
        azrael.config(image=frame3)
        ventanarobot.after(500, own1_aux)
        ventanarobot.mainloop()

    #           ___________________________________
    # __________/Función que ejecuta la animacion para que entregue su corazon
    def own2():
        global energy
        energy -= 7
        battery_level()
        s = Thread(target=song_own2, args=())
        s.start()
        own2_aux()
        ventanarobot.mainloop()

    def own2_aux():
        global pos
        global rep
        pos += 1
        rep += 1
        if rep > 9:
            pos = -1
            rep = -1
            return
        if pos == len(kiss_frames):
            pos = 0
        frame3 = cargarImagen(kiss_frames[pos])
        azrael.config(image=frame3)
        ventanarobot.after(300, own2_aux)
        ventanarobot.mainloop()

    #           ___________________________________
    # __________/Función que empieza a reproducir musica
    def music_on():
        global energy
        energy -= 1
        battery_level()
        s = Thread(target=song_music, args=())
        s.start()
        frame2 = cargarImagen(music_frame)
        azrael.config(image=frame2)
        ventanarobot.mainloop()

    #           ___________________________________
    # __________/Función que detiene la musica
    def music_off():
        winsound.PlaySound(None, winsound.SND_ASYNC)
        frame3 = cargarImagen(built_frames[1])
        azrael.config(image=frame3)
        azrael.image = frame3

    #           ___________________________________
    # __________/Función que ejecuta la animacion para que se mueva hacia adelante
    def goahead():
        global energy
        energy -= 1
        battery_level()
        goahead_aux()
        ventanarobot.mainloop()

    def goahead_aux():
        global pos
        global rep
        pos += 1
        rep += 1
        if rep > 3:
            pos = -1
            rep = -1
            return
        if pos == len(goahead_frames):
            pos = 0
        frame3 = cargarImagen(goahead_frames[pos])
        azrael.config(image=frame3)
        ventanarobot.after(300, goahead)
        ventanarobot.mainloop()

    #           ___________________________________
    # __________/Función que ejecuta la animacion para que se mueva hacia atras
    def goback():
        global energy
        energy -= 1
        battery_level()
        goback_aux()
        ventanarobot.mainloop()

    def goback_aux():
        global pos
        global rep
        pos += 1
        rep += 1
        if rep > 3:
            pos = -1
            rep = -1
            return
        if pos == len(goback_frames):
            pos = 0
        frame3 = cargarImagen(goback_frames[pos])
        azrael.config(image=frame3)
        ventanarobot.after(300, goback)
        ventanarobot.mainloop()

    #           ___________________________________
    # __________/Función que revisa el entry y ejecuta su respectiva funcion
    def read(entry):
        entry = user_entry.get()
        entry = entry.lower()
        entry_power_int = entry[:-1]
        entry_power_int = entry_power_int[6:]
        entry_power = entry[:5]
        if entry == "hello":
            return hello()
        if entry == "cry":
            return cry()
        if entry == "built":
            return built()
        if entry == "smile":
            return smile()
        if entry == "dance":
            return dance()
        if entry == "own1":
            return own1()
        if entry == "own2":
            return own2()
        if entry == "music-on":
            return music_on()
        if entry == "music-off":
            return music_off()
        if entry == "goahead":
            return goahead()
        if entry == "goback":
            return goback()
        if entry == "right":
            return right()
        if entry == "left":
            return left()
        if entry == "status":
            return status()
        if entry_power == "power":
            return power(int(entry_power_int))
        else:
            return misscommand()

    # ______________________________
    # __________/Se crea un lienzo para la shell y minipantalla de ayuda
    shell = Canvas(fondo, width=1580, height=200, bg="#00cc00")
    shell.place(x=0, y=784)

    #           ______________________________
    # __________/Se crean labels para mostrar los datos de la shell
    label_1 = Label(shell, text="Ingrese un comando", fg="#000000", bg="#00cc00", font=("Source Code Pro", 22, "bold"))
    label_1.place(x=150, y=15)

    label_2 = Label(shell, text=">>>", fg="#000000", bg="#00cc00", font=("Source Code Pro", 22, "bold"))
    label_2.place(x=150, y=70)

    label_title = Label(shell, text="Lista de Comandos", fg="#000000", bg="#00cc00", font=("Eczar", 22, "bold"))
    label_title.place(x=900, y=10)

    label_C1 = Label(shell, text="hello", fg="#000000", bg="#00cc00", font=("Roboto Slab", 20))
    label_C1.place(x=700, y=60)

    label_C2 = Label(shell, text="built", fg="#000000", bg="#00cc00", font=("Roboto Slab", 20))
    label_C2.place(x=700, y=110)

    label_C3 = Label(shell, text="power(n)", fg="#000000", bg="#00cc00", font=("Roboto Slab", 20))
    label_C3.place(x=700, y=160)

    label_C4 = Label(shell, text="status", fg="#000000", bg="#00cc00", font=("Roboto Slab", 20))
    label_C4.place(x=850, y=60)

    label_C5 = Label(shell, text="goahead", fg="#000000", bg="#00cc00", font=("Roboto Slab", 20))
    label_C5.place(x=850, y=110)

    label_C6 = Label(shell, text="goback", fg="#000000", bg="#00cc00", font=("Roboto Slab", 20))
    label_C6.place(x=850, y=160 )

    label_C7 = Label(shell, text="right", fg="#000000", bg="#00cc00", font=("Roboto Slab", 20))
    label_C7.place(x=1000, y=60)

    label_C8 = Label(shell, text="left", fg="#000000", bg="#00cc00", font=("Roboto Slab", 20))
    label_C8.place(x=1000, y=110 )

    label_C9 = Label(shell, text="dance", fg="#000000", bg="#00cc00", font=("Roboto Slab", 20))
    label_C9.place(x=1000, y=160 )

    label_C10 = Label(shell, text="music-on", fg="#000000", bg="#00cc00", font=("Roboto Slab", 20))
    label_C10.place(x=1110, y=60 )

    label_C11 = Label(shell, text="music-off", fg="#000000", bg="#00cc00", font=("Roboto Slab", 20))
    label_C11.place(x=1110, y=110)

    label_C12 = Label(shell, text="smile", fg="#000000", bg="#00cc00", font=("Roboto Slab", 20))
    label_C12.place(x=1110, y=160)

    label_C13 = Label(shell, text="cry", fg="#000000", bg="#00cc00", font=("Roboto Slab", 20))
    label_C13.place(x=1280, y=60 )

    label_C14 = Label(shell, text="own1", fg="#000000", bg="#00cc00", font=("Roboto Slab", 20))
    label_C14.place(x=1280, y=110)

    label_C15 = Label(shell, text="own2", fg="#000000", bg="#00cc00", font=("Roboto Slab", 20))
    label_C15.place(x=1280, y=160)

    #           ______________________________
    # __________/Se crea un entry para el usuario
    entrada_shell = Entry(shell, width=17, bg="#000000", fg="#ffffff", disabledbackground="#00ff00", insertwidth=10,
                          borderwidth=5, insertbackground="#00ff00", font=("Source Code Pro", 18, "bold"),
                          textvariable=user_entry)
    entrada_shell.place(x=210, y=70)

    #           ______________________________
    # __________/Se vincula la tecla Enter con el entry
    entrada_shell.bind("<Return>", read)
    entrada_shell.focus_set()

    #           _____________________________
    # __________/Volver a la ventana principal
    def regresar():
        ventanarobot.destroy()
        ventana_principal.deiconify()

    #           ____________________________
    # __________/Crear una nueva ventana de Ayuda
    def VentanaHelp():
        ventanarobot.withdraw()
        ventanahelp = Toplevel()
        ventanahelp.title("Help")
        ventanahelp.minsize(500, 500)
        ventanahelp.resizable(width=NO, height=NO)

        #           ____________________________
        # __________/Crear un widget de texto y un scrollbar para el mismo
        S = Scrollbar(ventanahelp)
        help_text = Text(ventanahelp, width=130, height=37)
        S.pack(side=RIGHT, fill=Y)
        help_text.pack(side=LEFT, fill=Y)
        S.config(command=help_text.yview)
        help_text.config(yscrollcommand=S.set)

        body = "Bienvenido a la ventana de ayuda :D\n\n\nEn el cuadro de entrada de texto se deben escribir alguno de" \
               " los " \
               "siguientes comandos para que Azrael realice lo que el comando indique, entonces por ejemplo si se desea" \
               " que"\
               " Azrael llore se escribe cry en la entrada de texto.\nNote que se deben escribir EXACTAMENTE como se" \
               " indica "\
               "en la lista de comandos.\n\nLista de Comandos: \n\nhello: Azrael saluda y muestra en la pantalla su" \
               " nombre."\
               "\nbuilt: Azrael muestra en pantalla su fecha de creación.\npower(n):  Azrael recibe una cantidad n de" \
               " energía"\
               " que debe un numero entero ser entre 0 y 100.\nstatus: Azrael indica cuanto tiene de energía." \
               " \ngoahead: " \
               "Azrael camina hacia adelante y se reduce en uno la energía. \ngoback: Azrael camina hacia atras y se " \
               "reduce "\
               "en uno la energía.\nright: Azrael camina hacia la derecha y se reduce en uno la energía." \
               " \nleft: Azrael" \
               " camina" \
               "hacia la izquierda y se reduce en uno la energía. \ndance: Azrael baila y se reduce en dos la energía." \
               " \nmusic" \
               "-on:  Azrael reproduce musica y se reduce en uno la energía. \nmusic-off:  Azrael detiene la musica." \
               " \nsmile: " \
               "Azrael rie. \ncry: Azrael llora y se reduce en uno la energía. \nown1: Azrael va a la playa y se" \
               " reduce" \
               " en tres la energia \nown2: Azrael " \
               "entrega su corazón y se reduce en siete la energia.\n\n"

        #           ____________________________
        # __________/ Se crean tags para darle formato al contenido de la pantalla de Ayuda
        help_text.insert(END, body)
        help_text.config(wrap=WORD)
        help_text.tag_add("Title", 1.0, 1.35)
        help_text.tag_add("Body", 4.0, 5.26)
        help_text.tag_add("Exactamente", 5.27, 5.38)
        help_text.tag_add("Body_2", 5.39, 5.99)
        help_text.tag_add("Subtitle", 7.0, 7.35)
        help_text.tag_add("C1", 9.0, 9.6)
        help_text.tag_add("C2", 10.0, 10.6)
        help_text.tag_add("C3", 11.0, 11.9)
        help_text.tag_add("C4", 12.0, 12.7)
        help_text.tag_add("C5", 13.0, 13.8)
        help_text.tag_add("C6", 14.0, 14.7)
        help_text.tag_add("C7", 15.0, 15.6)
        help_text.tag_add("C8", 16.0, 16.5)
        help_text.tag_add("C9", 17.0, 17.6)
        help_text.tag_add("C10", 18.0, 18.9)
        help_text.tag_add("C11", 19.0, 19.11)
        help_text.tag_add("C12", 20.0, 20.6)
        help_text.tag_add("C13", 21.0, 21.4)
        help_text.tag_add("C14", 22.0, 22.5)
        help_text.tag_add("C15", 23.0, 23.5)
        help_text.tag_add("C1_Body", 9.7, 9.99)
        help_text.tag_add("C2_Body", 10.7, 10.69)
        help_text.tag_add("C3_Body", 11.11, 11.99)
        help_text.tag_add("C4_Body", 12.8, 12.79)
        help_text.tag_add("C5_Body", 13.9, 13.89)
        help_text.tag_add("C6_Body", 14.8, 14.79)
        help_text.tag_add("C7_Body", 15.7, 15.69)
        help_text.tag_add("C8_Body", 16.6, 16.99)
        help_text.tag_add("C9_Body", 17.7, 17.69)
        help_text.tag_add("C10_Body", 18.11, 18.99)
        help_text.tag_add("C11_Body", 19.12, 19.99)
        help_text.tag_add("C12_Body", 20.7, 20.69)
        help_text.tag_add("C13_Body", 21.5, 21.49)
        help_text.tag_add("C14_Body", 22.6, 22.59)
        help_text.tag_add("C15_Body", 23.6, 23.99)
        help_text.tag_config("Title", font=("Eczar", 32))
        help_text.tag_config("Body", font=("Gentium Basic", 20))
        help_text.tag_config("Exactamente", font=("Rubik", 17, "bold"))
        help_text.tag_config("Body_2", font=("Gentium Basic", 20))
        help_text.tag_config("Subtitle", font=("Eczar", 26))
        help_text.tag_config("C1", font=("Roboto Slab", 20))
        help_text.tag_config("C2", font=("Roboto Slab", 20))
        help_text.tag_config("C3", font=("Roboto Slab", 20))
        help_text.tag_config("C4", font=("Roboto Slab", 20))
        help_text.tag_config("C5", font=("Roboto Slab", 20))
        help_text.tag_config("C6", font=("Roboto Slab", 20))
        help_text.tag_config("C7", font=("Roboto Slab", 20))
        help_text.tag_config("C8", font=("Roboto Slab", 20))
        help_text.tag_config("C9", font=("Roboto Slab", 20))
        help_text.tag_config("C10", font=("Roboto Slab", 20))
        help_text.tag_config("C11", font=("Roboto Slab", 20))
        help_text.tag_config("C12", font=("Roboto Slab", 20))
        help_text.tag_config("C13", font=("Roboto Slab", 20))
        help_text.tag_config("C14", font=("Roboto Slab", 20))
        help_text.tag_config("C15", font=("Roboto Slab", 20))
        help_text.tag_config("C1_Body", font=("Gentium Basic", 20))
        help_text.tag_config("C2_Body", font=("Gentium Basic", 20))
        help_text.tag_config("C3_Body", font=("Gentium Basic", 20))
        help_text.tag_config("C4_Body", font=("Gentium Basic", 20))
        help_text.tag_config("C5_Body", font=("Gentium Basic", 20))
        help_text.tag_config("C6_Body", font=("Gentium Basic", 20))
        help_text.tag_config("C7_Body", font=("Gentium Basic", 20))
        help_text.tag_config("C8_Body", font=("Gentium Basic", 20))
        help_text.tag_config("C9_Body", font=("Gentium Basic", 20))
        help_text.tag_config("C10_Body", font=("Gentium Basic", 20))
        help_text.tag_config("C11_Body", font=("Gentium Basic", 20))
        help_text.tag_config("C12_Body", font=("Gentium Basic", 20))
        help_text.tag_config("C13_Body", font=("Gentium Basic", 20))
        help_text.tag_config("C14_Body", font=("Gentium Basic", 20))
        help_text.tag_config("C15_Body", font=("Gentium Basic", 20))
        help_text.config(state=DISABLED)

        #           _____________________________
        # __________/Volver a la ventana robot
        def regresar():
            ventanahelp.destroy()
            ventanarobot.deiconify()

        #           ____________________________
        # __________/Se crea un boton de regreso
        imagenvolverbk = cargarImagen("exit.png")
        botonvolver = Button(ventanahelp, image=imagenvolverbk, command=regresar, fg="#000000", bg="#00cc00",
                                activebackground = "#cc2900")
        botonvolver.pack(side=BOTTOM)

        ventanahelp.mainloop()

    #           ____________________________
    # __________/Botones de ventana robot
    imagenvolverbk = cargarImagen("exit.png")
    botonvolver = Button(fondo, image=imagenvolverbk, command=regresar, fg="#000000", bg="#00cc00",
                         activebackground="#cc2900")
    botonvolver.place(x=10, y=910)

    imagenhelp = cargarImagen("help.png")
    botonhelp = Button(ventanarobot, image=imagenhelp, command=VentanaHelp, bg="#00cc00",
                       fg="#000000", activebackground="#cc2900")
    botonhelp.place(x=1500, y=910)

    ventanarobot.mainloop()

#           ____________________________
#__________/Botones de ventana principal
boton_start = Button(contenedor_principal, text="Start", command=VentanaRobot, bg="#ffffff", fg="#000000",
                     font=("Eczar", 18, "bold"))
boton_start.place(x=50, y=205)

boton_load = Button(contenedor_principal, text="Load", command=dont, bg="#ffffff", fg="#000000",
                    font=("Eczar", 18, "bold"))
boton_load.place(x=510, y=205)

ventana_principal.mainloop()
