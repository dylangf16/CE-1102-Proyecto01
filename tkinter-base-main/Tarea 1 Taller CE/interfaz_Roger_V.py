from tkinter import *
from tkinter import messagebox
from threading import Thread
import time
import random
import os
import winsound

ventana_principal = Tk()
ventana_principal.title("Bienvenidos")
ventana_principal.minsize(700, 438)
ventana_principal.resizable(width=NO, height=NO)

contenedor_principal = Canvas(ventana_principal, width=700, height=438, bg="#000000")
contenedor_principal.place(x=0, y=0)


contador = 0
tiempo_ejecucion = StringVar()
result = StringVar()
contador_aux = StringVar()


# 1: Comparación
# E: Dos números
# S: Valor de verdad si los dígitos del primer numero son menores o iguales a los del segundo dígito.
# R: Números enteros positivos
def compare(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int) and num1 >= 0 and num2 >= 0:
        primer = largo(num1)
        segundo = largo(num2)
        if primer == segundo:
            return compare_aux(num1, num2)
    else:
        return "Error"


def largo(num1):
    if isinstance(num1, int):
        return largo_aux(num1)
    else:
        return "Error2"


def largo_aux(num1):
    if num1 // 10 == 0:
        return 1
    else:
        return 1 + largo_aux(num1 // 10)


def compare_aux(num1, num2):
    if num1 == 0:
        return "True"
    elif num1 > num2:
        return "False"
    elif num1%10 > num2%10:
        return "False"
    else:
        return compare_aux(num1 // 10, num2 // 10)

# 2:Fibonacci
# E: Número "n"
# S: Numero correspondiente según la sucesión de Fibonacci
# R: Número enteros positivo

def fib(num):
    global tiempo_ejecucion
    global result
    global contador
    global contador_aux
    if isinstance(num, int) and num >= 0 and num <= 30:
        tiempo_inicial = time.time()
        contador = 0
        result.set(str(fib_aux(num)))
        tiempo_final = time.time()
        tiempo_ejecucion.set(str(tiempo_final - tiempo_inicial))
        contador_aux.set((str(contador)))
        return result


def fib_aux(num):
    global contador
    contador += 1
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib_aux(num-1) + fib_aux(num-2)


def cargarImagen(nombre):
    ruta = os.path.join('Imagenes', nombre)
    imagen = PhotoImage(file=ruta)
    return imagen

imagenFondo = cargarImagen("Atom.gif")
LabelFondo = Label(contenedor_principal, image=imagenFondo, bg="#FFFFFF")
LabelFondo.place(x=0, y=0)


def mostrarventcomp(num1, num2):
    res = compare(int(num1), int(num2))
    messagebox.showinfo("Resultado", "El resultado es: " + res)


def VentanaComparacion():
    ventana_principal.withdraw()
    ventanacomp = Toplevel()
    ventanacomp.title("Comparación de un número")
    ventanacomp.minsize(500, 300)
    ventanacomp.resizable(width=NO, height=NO)

    fondo = Canvas(ventanacomp, width=500, height=300, bg="#EDC951")
    fondo.place(x=0, y=0)

    imagenFondo = cargarImagen("math.gif")
    LabelFondo = Label(ventanacomp, image=imagenFondo, bg="#FFFFFF")
    LabelFondo.place(x=0, y=0)

    label_1 = Label(ventanacomp, text="Inserte dos números para comparar", bg="#EDC951", fg="#6A4A3C",
                    font=("Courier", 18, "bold"))
    label_1.place(x=70, y=30)

    entradanum1 = Entry(ventanacomp, width=10, bg="#EB6841")
    entradanum1.place(x=100, y=80)

    entradanum2 = Entry(ventanacomp, width=10, bg="#EB6841")
    entradanum2.place(x=300, y=80)

    label_2 = Label(ventanacomp, text="=?", bg="#EDC951", fg="#CC333F", font=("Courier", 28, "bold"))
    label_2.place(x=225, y=80)

    label_3 = Label(ventanacomp, text="Numero 1", bg="#EDC951", fg="#00A0B0", font=("Courier", 16, "bold"))
    label_3.place(x=100, y=110)

    label_4 = Label(ventanacomp, text="Numero 2", bg="#EDC951", fg="#00A0B0", font=("Courier", 16, "bold"))
    label_4.place(x=300, y=110)

    botoncalcular = Button(ventanacomp, text="Calcular",
                           command= lambda : mostrarventcomp(entradanum1.get(),entradanum2.get()), bg="#ffff66",
                           fg="#000000")
    botoncalcular.place(x=240, y=150)

    def regresar():
        ventanacomp.destroy()

        ventana_principal.deiconify()

    imagenvolverwh = cargarImagen("exitwh.gif")
    botonVolver = Button(ventanacomp, image= imagenvolverwh, command=regresar, fg="#000000", bg="#000000")
    botonVolver.place(x=380, y=245)

    ventanacomp.mainloop()


botoncompare = Button(contenedor_principal, text="Comparación \n de un numero", command=VentanaComparacion, bg="#ffff66", fg="#000000",font=("Courier", 18, "bold"))
botoncompare.place(x=70, y=213)


def mostrarfib(num):
    resu = fib(int(num))
    return resu

def VentanaFib():
    global result
    global tiempo_ejecucion
    global contador
    ventana_principal.withdraw()
    ventanaFib = Toplevel()
    ventanaFib.title("Sucesion de Fibonacci")
    ventanaFib.minsize(800, 400)
    ventanaFib.resizable(width=NO, height=NO)

    fondo = Canvas(ventanaFib, width=800, height=400, bg="#E1DBBB")
    fondo.place(x=0, y=0)

    label_1 = Label(ventanaFib, text="Inserte un número", bg="#E1DBBB", fg="#19232F", font=("Courier", 18, "bold"))
    label_1.place(x=50, y=30)

    entradafib = Entry(ventanaFib, width=10, bg="#C08752")
    entradafib.place(x=100, y=80)

    imagenfib = cargarImagen("fib.gif")
    label_imgfib = Label(ventanaFib, image=imagenfib, bg="#E1DBBB")
    label_imgfib.place(x=350, y=35)


    botonCalcular = Button(ventanaFib, text="Calcular", command = lambda : mostrarfib(entradafib.get()), bg="#865328",
                           fg="#19232F", font=("Courier", 18, "italic"))
    botonCalcular.place(x=210, y=80)

    label_2 = Label(ventanaFib, text="Resultado = ", bg="#E1DBBB", fg="#19232F", font=("Courier", 18, "bold"))
    label_2.place(x=50, y=130)


    labelresult = Label(ventanaFib, textvariable= result, bg="#BC5542", fg="#19232F", font=("Courier", 18, "bold"))
    labelresult.configure(textvariable=result)
    labelresult.place(x=200, y=130)


    label_3 = Label(ventanaFib, bg="#BC5542", fg="#19232F", font=("Courier", 18, "bold"), text = "Tiempo de ejecución:")
    label_3.place(x=50, y=180)


    labeltemp = Label(ventanaFib, textvariable=tiempo_ejecucion, bg="#BC5542", fg="#19232F",
                      font=("Courier", 18, "bold"))
    labeltemp.configure(textvariable = tiempo_ejecucion)
    labeltemp.place(x=50, y=200)

    label_4 = Label(ventanaFib, bg="#BC5542", fg="#19232F", font=("Courier", 18, "bold"), text="Llamadas recursivas:")
    label_4.place(x=50, y=320)

    labelcont = Label(ventanaFib, textvariable=contador_aux, bg="#BC5542", fg="#19232F", font=("Courier", 18, "bold"))
    labelcont.configure(textvariable = contador_aux)
    labelcont.place(x=50, y=350)

    def regresar():
        ventanaFib.destroy()

        ventana_principal.deiconify()

    imagenvolverbk = cargarImagen("exitbk.gif")
    botonVolver = Button(fondo, image=imagenvolverbk, command=regresar, fg="#000000", bg="#E1DBBB")
    botonVolver.place(x=640, y=345)

    ventanaFib.mainloop()


botonfib = Button(contenedor_principal, text="Serie de \n Fibonacci", command=VentanaFib, bg="#ffff66", fg="#000000",
                  font=("Courier", 18, "bold"))
botonfib.place(x=440, y=213)


def VentanaAcerca():
    ventana_principal.withdraw()
    ventanaAcerca = Toplevel()
    ventanaAcerca.title("Acerca el programador")
    ventanaAcerca.minsize(700, 900)
    ventanaAcerca.resizable(width=NO, height=NO)

    fondo = Canvas(ventanaAcerca, width=700, height=900, bg="#272822")
    fondo.place(x=0, y=0)

    label_1 = Label(ventanaAcerca, text="Nombre:", bg="#272822", fg="#F92672", font=("Courier", 18, "bold"))
    label_1.place(x=70, y=30)

    label_11 = Label(ventanaAcerca, text="Róger Andrés Valderrama Ordóñez", bg="#272822", fg="#A6E22E",
                     font=("Courier", 16))
    label_11.place(x=200, y=30)

    imagenNombre = cargarImagen("foto1.gif")
    LabelNombre = Label(ventanaAcerca, image=imagenNombre, bg="#272822")
    LabelNombre.place(x=327, y=57)

    imagenlabel_11 = cargarImagen("sp.gif")
    Label_111 = Label(ventanaAcerca, image=imagenlabel_11, bg="#272822")
    Label_111.place(x=47, y=30)

    label_2 = Label(ventanaAcerca, text="Carnet:", bg="#272822", fg="#F92672", font=("Courier", 18, "bold"))
    label_2.place(x=70, y=80)

    label_22 = Label(ventanaAcerca, text="2017113167", bg="#272822", fg="#A6E22E", font=("Courier", 16))
    label_22.place(x=200, y=80)

    imagenlabel_22 = cargarImagen("sp.gif")
    Label_222 = Label(ventanaAcerca, image=imagenlabel_22, bg="#272822")
    Label_222.place(x=47, y=80)

    label_3 = Label(ventanaAcerca, text="Género:", bg="#272822", fg="#F92672", font=("Courier", 18, "bold"))
    label_3.place(x=70, y=130)

    label_33 = Label(ventanaAcerca, text="Masculino.", bg="#272822", fg="#A6E22E", font=("Courier", 16))
    label_33.place(x=200, y=130)

    imagenlabel_33 = cargarImagen("sp.gif")
    Label_333 = Label(ventanaAcerca, image=imagenlabel_33, bg="#272822")
    Label_333.place(x=47, y=130)

    label_4 = Label(ventanaAcerca, text="Edad:", bg="#272822", fg="#F92672", font=("Courier", 18, "bold"))
    label_4.place(x=70, y=180)

    label_44 = Label(ventanaAcerca, text="17 años.", bg="#272822", fg="#A6E22E", font=("Courier", 16))
    label_44.place(x=200, y=180)

    imagenlabel_44 = cargarImagen("sp.gif")
    Label_444 = Label(ventanaAcerca, image=imagenlabel_44, bg="#272822")
    Label_444.place(x=47, y=180)

    label_5 = Label(ventanaAcerca, text="Dirección:", bg="#272822", fg="#F92672", font=("Courier", 18, "bold"))
    label_5.place(x=70, y=230)

    label_55 = Label(ventanaAcerca, text="200 metros Norte del mercado municipal.", bg="#272822", fg="#A6E22E",
                     font=("Courier", 16))
    label_55.place(x=200, y=230)

    imagenlabel_55 = cargarImagen("sp.gif")
    Label_555 = Label(ventanaAcerca, image=imagenlabel_55, bg="#272822")
    Label_555.place(x=47, y=230)

    label_6 = Label(ventanaAcerca, text="Mapa:", bg="#272822", fg="#F92672", font=("Courier", 18, "bold"))
    label_6.place(x=70, y=280)

    imagenMapa = cargarImagen("mapa.gif")
    LabelMapa = Label(ventanaAcerca, image=imagenMapa, bg="#272822")
    LabelMapa.place(x=200, y=280)

    imagenlabel_66 = cargarImagen("sp.gif")
    Label_666 = Label(ventanaAcerca, image=imagenlabel_66, bg="#272822")
    Label_666.place(x=47, y=280)

    label_7 = Label(ventanaAcerca, text="Artista:", bg="#272822", fg="#66D9EF", font=("Courier", 18, "bold"))
    label_7.place(x=70, y=550)

    label_77 = Label(ventanaAcerca, text="Savant", bg="#272822", fg="#A6E22E", font=("Courier", 16))
    label_77.place(x=200, y=550)

    imagenlabel_77 = cargarImagen("sp.gif")
    Label_777 = Label(ventanaAcerca, image=imagenlabel_77, bg="#272822")
    Label_777.place(x=47, y=550)

    label_8 = Label(ventanaAcerca, text="Género \n Musical:", bg="#272822", fg="#66D9EF", font=("Courier", 18, "bold"))
    label_8.place(x=70, y=600)

    label_88 = Label(ventanaAcerca, text="Dubstep", bg="#272822", fg="#A6E22E", font=("Courier", 16))
    label_88.place(x=200, y=620)

    imagenlabel_88 = cargarImagen("sp.gif")
    Label_888 = Label(ventanaAcerca, image=imagenlabel_88, bg="#272822")
    Label_888.place(x=50, y=600)

    def cancion():
        winsound.PlaySound('ism.wav', winsound.SND_ASYNC)

    imagenism = cargarImagen("ism.gif")
    button_ism = Button(ventanaAcerca, image=imagenism, width=280, height=280, command=cancion)
    button_ism.place(x=325, y=550)

    def regresar():
        ventanaAcerca.destroy()
        ventana_principal.deiconify()

    imagenvolverbk = cargarImagen("exitbk.gif")
    botonVolver = Button(fondo, image = imagenvolverbk, command=regresar, fg="#000000", bg="#0fa0aa")
    botonVolver.place(x=655, y=855)

    ventanaAcerca.mainloop()


botonAcerca = Button(contenedor_principal, text="Acerca del programador", command=VentanaAcerca, bg="#ffff66",
                     font=("Courier", 18, "bold"))
botonAcerca.place(x=270, y=350)

flag_cuadro = True


def VentanaRain():
    ventana_principal.withdraw()
    ventanaRain = Toplevel()
    ventanaRain.title("Rainbow Rain")
    ventanaRain.minsize(517, 600)
    ventanaRain.resizable(width=NO, height=NO)

    fondo = Canvas(ventanaRain, width=517, height=600, bg="#000000")
    fondo.place(x=0, y=0)

    imagencloud = cargarImagen("cld.gif")
    label_imgfib = Label(ventanaRain, image=imagencloud, bg="#000000")
    label_imgfib.place(x=0, y=0)

    imagencloud2 = cargarImagen("cld.gif")
    label_imgfib = Label(ventanaRain, image=imagencloud2, bg="#000000")
    label_imgfib.place(x=257, y=0)


    def color():
        lista_colores = ["#9400D3", "#4B0082", "#0000FF", "#00FF00", "#FFFF00", "#FF7F00", "#FF0000"]
        return lista_colores[random.randrange(0, 7)]

    def cuadro():
        x_cuadro = random.randrange(0, 507)
        y_cuadro = 150
        cuadro = Canvas(fondo, width=random.randrange(25, 35), height=random.randrange(25, 35), bg=color())
        while flag_cuadro:
            try:
                cuadro.place(x=x_cuadro, y=y_cuadro)
                if (y_cuadro == 540):
                    y_cuadro = 150
                    x_cuadro += 30
                elif (x_cuadro == 500):
                    x_cuadro = 0
                else:
                    y_cuadro += 30
                time.sleep(0.04)

            except Exception as errtxt:
                print("Error en hilo")

    def ver_cuadro():
        global flag_cuadro
        flag_cuadro = True
        a = Thread(target=cuadro, args=())

        a.start()

    def kill_cuadro():
        global flag_cuadro
        flag_cuadro = False

    def regresar():
        kill_cuadro()
        ventanaRain.destroy()
        ventana_principal.deiconify()


    imageniniciar = cargarImagen("plus.gif")
    botonIniciarHilo = Button(ventanaRain, image=imageniniciar, command=ver_cuadro, bg="#000000")
    botonIniciarHilo.place(x=50, y=555)

    imagendetener = cargarImagen("close.gif")
    botonDetenerHilos = Button(ventanaRain, image=imagendetener, command=kill_cuadro, bg="#000000")
    botonDetenerHilos.place(x=130, y=555)

    imagenvolverwh = cargarImagen("exitwh.gif")
    botonVolver = Button(ventanaRain, image=imagenvolverwh, command=regresar, bg="#000000")
    botonVolver.place(x=460, y=555)

    ventanaRain.mainloop()

botonRain = Button(contenedor_principal, text="Rainbow Rain", command=VentanaRain, bg="#ffff66",
                   font=("Courier", 18, "bold"))
botonRain.place(x= 327, y= 100)


ventana_principal.mainloop()
