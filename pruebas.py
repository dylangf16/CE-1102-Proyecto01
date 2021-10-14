about= """
Costa Rica
Tecnológico de Costa Rica
Ingeniería en Computadores
Taller de Programación
2021
Grupo 2
Profesor: Milton Villegas Lemus
Versión 0.17
Autor: Dylan Garbanzo Fallas
Autor de módulos editados: Jose Fernando
"""
intro = '''
Bienvenido al videojuego 
Moon to Mars
'''
Jefe= 'Vida del Jefe: '
from tkinter import *
from os import path
from threading import *
import time
import vlc
from PIL import ImageTk, Image
import random

reproductor = vlc.MediaPlayer()
FLAG = False #disparo jefes
FLAG2 = False #disparo nave
FLAG3 = False #cronómetro
vida_jugador = 50
vida_boss1 = 30
vida_boss2 = 40
vida_boss3 = 50
segundos = 0
puntaje = 0
puntaje_final = ''
nombre_usuario = ''
posicion = 0
puntaje = 0
nombres = ['Ocanji\n' ,'Tzalil\n', 'Boggismis\n', 'cersl0v3\n', 'pugblog\n']


#Ventana Principal (módulos editados)========================================================================================================
ventana = Tk()
ventana.title("Moon to Mars")
ventana.minsize(700,933) #Dimensiones de la ventana (x,y)
ventana.resizable(width=NO , height= NO) 
fuente_global =('Arial, 15')
fuente_vida = ('Arial, 35')


#Apartado de Música (Módulos editados)========================================================================================================
def cargarMP3(nombre):
    return path.join('assets//songs_and_effects//', nombre) #ruta de música

def reproducir_fx(MP3):
    vlc.MediaPlayer(MP3).play() #Función para efectos especiales
    
def detener_cancion():
    global reproductor
    if(isinstance(reproductor, vlc.MediaPlayer)): #Función para detener canciones
        reproductor.stop()

def reproducir_cancion(MP3): 
    global reproductor
    detener_cancion()
    reproductor = vlc.MediaPlayer(MP3)
    reproductor.audio_set_volume(30)  #Función para música
    reproductor.play()
    
def close():
    global ventana
    detener_cancion()
    print("Gracias por probar mi videojuego!")
    ventana.destroy()



#Apartado de imágenes y animación (Módulos editados)===========================================================================================
def cargar_img(nombre):
    ruta = path.join('assets//fondos//', nombre) #ruta de la imagen para el fondo
    img = ImageTk.PhotoImage(Image.open(ruta)) #Cargar imagen
    return img

def cargar_nave(nombre):
    ruta = path.join('assets//naves//', nombre) #ruta de la imagen para las naves
    img = ImageTk.PhotoImage(Image.open(ruta)) #Cargar imagen
    return img

def cargar_explosión(nombre):
    ruta = path.join('assets//explosiones//', nombre) #ruta de la imagen para la explosión
    img = ImageTk.PhotoImage(Image.open(ruta)) #Cargar imagen
    return img

def cargar_disparo(nombre):
    ruta = path.join('assets//disparos//', nombre) #ruta de la imagen para los disparos
    img = ImageTk.PhotoImage(Image.open(ruta)) #Cargar imagen
    return img

def cargar_icono(nombre):
    ruta = path.join('assets//icons//', nombre) #ruta de la imagen para los iconos
    img = PhotoImage(Image.open(ruta)) #Cargar imagen
    return img



#Apartado de Ranking ==============================================================================================================================
#Transformar de txt a lista ------------------------------------
def cont(conteo, lista, seek):
    global posicion
    MiArchi1= open('Ranking.txt', 'r+')
    posicion = 1
    if conteo < 5:
        MiArchi1.seek(seek)
        num = MiArchi1.readline()
        lista.append(int(num))
        conteo += 1
        seek += 5
        return cont(conteo, lista, seek)
    else:
        MiArchi1.close()
        return comparar(lista,[])

#Comparar la lista con el puntaje obtenido --------------------------
def comparar(lista,lista_completa):
    global posicion, puntaje, puntaje_final, nombres, nombre_usuario
    if lista == []:
        puntaje_final = 'No quedaste en el top 5 scores'
        return 0
    if puntaje < lista[0]:
        num_mayor = lista[0]
        posicion += 1
        lista_completa.append(num_mayor)
        return comparar(lista[1:],lista_completa)
    else:
        lista_completa.append(puntaje)
        tamaño = int(len(lista) - 1)
        lista_completa = lista_completa + lista[0:tamaño]
        nueva_posicion = posicion - 1
        nombres[nueva_posicion] = nombre_usuario + '\n'
        return insert_sort(lista_completa)

#Ordenar de menor a mayor la lista -------------------------------------
def insert_sort(Lista):
    return insert_sort_aux(Lista,1,len(Lista))

def insert_sort_aux(Lista,i,n):
    if i == n:
        return aux_invierta(Lista,[])
    Aux = Lista[i]
    j = incluye_orden(Lista,i,Aux)
    Lista[j] = Aux
    return insert_sort_aux(Lista,i+1,n)

def incluye_orden(Lista,j,Aux):
    if j <= 0 or Lista[j-1]<=Aux:
        return j
    Lista[j] = Lista[j-1]
    return incluye_orden(Lista,j-1,Aux)

#Invertir lista ------------------------------------------
def aux_invierta(lista,lista_final):
    if lista != []:
        num = lista[-1]
        lista_final.append(num)
        return aux_invierta(lista[:-1],lista_final)
    else:
        return nueva_lista(lista_final,0,0)

#Agregar nuevos elementos a la lista completa ----------
def nueva_lista(lista,num,seek):
    global posicion, puntaje_final
    MiArchi1= open('Ranking.txt', 'r+')
    if lista == []:
        MiArchi1.close()
        puntaje_final = 'Quedaste en la posición: '+ str(posicion)
        return 0
    else:
        MiArchi1.seek(seek)
        num = lista[0]
        num = str(num) + '\n'
        MiArchi1.write(num)
        seek += 5
        return nueva_lista(lista[1:],0,seek)

#Pantalla para escoger nivel ------------------------------------------------------------------------------------------------------------------------
def escoger_nivel():
    C_app = Canvas(ventana, width=700 ,height = 933)
    C_app.place(x=0,y=0)
    C_app.fondo = cargar_img('fondo_principal.png') 
    fondo = C_app.create_image(0,0,anchor=NW,image=C_app.fondo)

    Btn_boss1 = Button(ventana, text='Presiona para empezar  n// en el Primer Nivel' , font=fuente_global, command=pantalla_boss1).pack()
    Btn_boss1.place(x=500 , y=350)

    Btn_boss2 = Button(ventana, text='Presiona para empezar  n// en el Primer Segundo' , font=fuente_global, command=pantalla_boss2).pack()
    Btn_boss2.place(x=500 , y=400)

    Btn_boss3 = Button(ventana, text='Presiona para empezar  n// en el Tercer Nivel' , font=fuente_global, command=pantalla_boss3).pack()
    Btn_boss3.place(x=500 , y=450)

    Btn_normal = Button(ventana, text='Presiona para empezar normal' , font=fuente_global, command=pantalla_boss1).pack()
    Btn_normal.place(x=500 , y=550)



#Ventana Boss 1 ==============================================================================================================================
def pantalla_boss1():
    global vida_boss1, vida_jugador, segundos, FLAG2, FLAG3
    FLAG2 = True
    FLAG3 = True
    C_app = Canvas(ventana, width=700 ,height = 933)
    C_app.place(x=0,y=0)
    C_app.fondo = cargar_img('fondo_1.png') 
    fondo = C_app.create_image(0,0,anchor=NW,image=C_app.fondo)

    C_app2 = Canvas(ventana, width= 700, height= 600, bg='#1c1b1a')
    C_app2.place(x=0,y=855)

    C_app3 = Canvas(ventana, width= 700, height= 80, bg='#1c1b1a')
    C_app3.place(x=0,y=0)
    
    reproducir_cancion(cargarMP3('Boss_1.mp3'))
    
    img_Boss1 = cargar_nave('Boss_1.png')
    Boss1 = C_app.create_image(0, 75, anchor=NW, tags= ('Boss1'))


#Movimiento de izquierda a derecha------------------------------------------------------------------------
    def movi_izq_der(Boss1,img_Boss1,conteo,probabilidad):
        global vida_boss1, puntaje_final, puntaje, FLAG2, FLAG3, vida_jugador
        #Condiciones para que termine la partida ---------------------
        if vida_boss1 <= 0:
            FLAG2 = False
            FLAG3 = False
            vida_jugador = 50
            return pantalla_boss2()

        if vida_jugador < 0:
            FLAG2 = False
            FLAG3 = False
            time.sleep(5)
            return pantalla_resultados()


        current_coords = C_app.coords(Boss1)
        if current_coords[0]==258:
            return movi_der_izq(Boss1, img_Boss1,conteo,0)
        C_app.coords(Boss1, current_coords[0]+2, current_coords[1])
        C_app.itemconfig('Boss1', image=img_Boss1)
        conteo -= 1
        if conteo == 0:
            conteo = 200 #2 segundos entre posible envestida 
            probabilidad = random.randint(1,10)
            if probabilidad % 3 == 0:
                time.sleep(0.5)
                return arriba_abajo(Boss1, img_Boss1, conteo, nave)
            else:
                return movi_der_izq(Boss1, img_Boss1, conteo, 0)

        def callback():
            movi_izq_der(Boss1,img_Boss1,conteo,0) #Transisción entre fotogramas
        ventana.after(10, callback) #velocidad


#Movimiento de derecha a izquierda-------------------------------------------------------------------------
    def movi_der_izq(Boss1,img_Boss1,conteo,probabilidad):
        global vida_boss1, puntaje_final, puntaje, FLAG2, FLAG3, vida_jugador
        #Condiciones para que termine la partida ---------------------
        if vida_boss1 <= 0:
            FLAG2 = False
            FLAG3 = False
            vida_jugador = 50
            return pantalla_boss2()

        if vida_jugador < 0:
            FLAG2 = False
            FLAG3 = False
            time.sleep(5)
            return pantalla_resultados()

        current_coords = C_app.coords(Boss1)
        if current_coords[0]==0:
            return movi_izq_der(Boss1,img_Boss1,conteo,0)
        current_coords = C_app.coords(Boss1)
        C_app.coords(Boss1, current_coords[0]-1, current_coords[1]) #cantidad de espacios que se mueve
        C_app.itemconfig('Boss1', image=img_Boss1)
        conteo -= 1
        if conteo == 0:
            conteo = 200 #2 segundos entre posible envestida 
            probabilidad = random.randint(1,10)
            if probabilidad % 3 == 0:
                time.sleep(0.5)
                return arriba_abajo(Boss1, img_Boss1, conteo, nave)
            else:
                return movi_der_izq(Boss1, img_Boss1, conteo, 0)

        def callback():
            movi_der_izq(Boss1,img_Boss1,conteo,0) #Transisción entre fotogramas
        ventana.after(10, callback) #velocidad


#Embestida Boss 1 (módulo editado)-------------------------------------------------------------------------
    def arriba_abajo(Boss1, img_Boss1, conteo, nave):
        global vida_boss1, puntaje_final, puntaje, vida_jugador, FLAG3, FLAG2
        #Condiciones para que termine la partida ---------------------
        if vida_boss1 <= 0:
            FLAG2 = False
            FLAG3 = False
            vida_jugador = 50
            return pantalla_boss2()

        if vida_jugador < 0:
            FLAG2 = False
            FLAG3 = False
            time.sleep(5)
            return pantalla_resultados()

        current_coords = C_app.coords(Boss1)
        nave_coords = C_app.coords(nave)
        if (current_coords[1]==550):
            colision_boss1_nave(Boss1,nave)
            return abajo_arriba(Boss1, img_Boss1,conteo)
        current_coords = C_app.coords(Boss1)
        C_app.coords(Boss1, current_coords[0], current_coords[1]+1) #cantidad de espacios que se mueve
        C_app.itemconfig('Boss1', image=img_Boss1)


        def callback():
            arriba_abajo(Boss1, img_Boss1, conteo, nave) #Transisción entre fotogramas
        ventana.after(1, callback)


#Movimiento vertical Boss1 (módulo editado)----------------------------------------------------------------
    def abajo_arriba(Boss1, img_Boss1,conteo):
        global FLAG2, FLAG3, vida_jugador
        #Condiciones para que termine la partida ---------------------
        if vida_boss1 <= 0:
            FLAG2 = False
            FLAG3 = False
            vida_jugador = 50
            return pantalla_boss2()

        if vida_jugador <= 0:
            time.sleep(5)
            FLAG2 = False
            FLAG3 = False
            return pantalla_resultados()



        current_coords = C_app.coords(Boss1)
        if (current_coords[1]==75):
                if (current_coords[0]>50):
                    return movi_der_izq(Boss1, img_Boss1,conteo,0) #movimiento hacia la izquierda
                else:
                    return movi_izq_der(Boss1, img_Boss1,conteo,0) #movimiento hacia la derecha
        current_coords = C_app.coords(Boss1)
        C_app.coords(Boss1, current_coords[0], current_coords[1]-1) #cantidad de espacios que se mueve
        C_app.itemconfig('Boss1', image=img_Boss1)

        def callback():
            abajo_arriba(Boss1, img_Boss1,conteo) #Transisción entre fotogramas
        ventana.after(1, callback)


#Módulo de movimiento del personaje (módulos editado)-------------------------------------------------------  
    img_nave = cargar_nave('nave_personaje.png')
    nave = C_app.create_image(300, 650, anchor=NW, tags= ('nave'))

    def derecha(event):
        current_coords = C_app.coords(nave)
        if current_coords[0] != 570: #Límite
            C_app.coords(nave, current_coords[0]+15, current_coords[1])
            C_app.itemconfig('nave', image=img_nave)
        
    def izquierda(event):
        current_coords = C_app.coords(nave)
        if current_coords[0] != 30: #Límite
            C_app.coords(nave, current_coords[0]-15, current_coords[1])
            C_app.itemconfig('nave', image=img_nave)
        
    def arriba(event):
        current_coords = C_app.coords(nave)
        if current_coords[1] != 5: #Límite
            C_app.coords(nave, current_coords[0], current_coords[1]-15)
            C_app.itemconfig('nave', image=img_nave)
            
    def abajo(event):
        current_coords = C_app.coords(nave)
        if current_coords[1] != 680: #Límite
            C_app.coords(nave, current_coords[0], current_coords[1]+15)
            C_app.itemconfig('nave', image=img_nave)


#Sistema de colisiones (Pantalla Boss 1)---------------------------------------------------------
    def colision_boss1_nave(Boss1, nave):
        global vida_jugador, vida_boss1, FLAG2, FLAG3
        hitbox_boss1 = C_app.bbox(Boss1)
        hitbox_nave = C_app.bbox(nave)
        if vida_boss1 <= 0:
            FLAG2 = False
            FLAG3 = False
            vida_jugador = 50
            return pantalla_boss2()

        if hitbox_boss1[0] < hitbox_nave[0] and hitbox_boss1[2] > hitbox_nave[2]:
            if hitbox_boss1[1] < hitbox_nave[1] and hitbox_boss1[3] > hitbox_nave[3]:
                vida_boss1 -=1
                vida_jugador -= 10
                labeljefe.config(text = vida_boss1)
                labelplayer.config(text = vida_jugador)
            else:
                vida_boss1 -=1
                labeljefe.config(text = vida_boss1)  
        else:
            vida_boss1 -=1
            labeljefe.config(text = vida_boss1)  


#Módulo de disparo --------------------------------------------------------------------------------------------------------------------
    def disparo_nave(img_disparo, laser):
        global vida_boss1, puntaje, vida_jugador, segundos, FLAG3, FLAG2
        #Condiciones para que termine la partida ---------------------------------------------------
        if FLAG2 == True:
            if vida_jugador <= 0:
                time.sleep(5)
                return pantalla_resultados()

            #Detecta colision ----------------------------------------------------------------------------
            hitbox_laser= C_app.bbox(laser)
            hitbox_boss1 = C_app.bbox(Boss1)
            if vida_boss1 <= 0:
                FLAG2 = False
                FLAG3 = False
                if vida_jugador == 50:
                    puntaje += 10
                    label_puntaje.config(text = puntaje)
                    if segundos <= 30:
                        puntaje += 20
                        label_puntaje.config(text = puntaje)
                        return pantalla_boss2()
                    else:
                        return pantalla_boss2()
                else:
                    return pantalla_boss2()

            if hitbox_boss1[0] < hitbox_laser[0] and hitbox_boss1[2] > hitbox_laser[2]:
                if hitbox_boss1[1] < hitbox_laser[1] and hitbox_boss1[3] > hitbox_laser[3]:
                    vida_boss1 -= 1
                    puntaje += 1
                    label_puntaje.config(text= puntaje)
                    C_app.delete(laser)
                    FLAG2 == False
                    labeljefe.config(text = vida_boss1)
                    return 0

            #Movimiento del disparo ---------------------------------------------------------------------
            laser_coords = C_app.coords(laser)
            if (laser_coords[1]==0):
                C_app.delete(laser)
                FLAG2 == False
                return 0

            C_app.coords(laser, laser_coords[0], laser_coords[1] -5) #cantidad de espacios que se mueve
            C_app.itemconfig('laser', image=img_disparo)


            def callback():
                disparo_nave(img_disparo, laser) #Transisción entre fotogramas
            ventana.after(1, callback)

    def llamada_disparo(event):
        reproducir_fx(cargarMP3('disparo_jugador.mp3'))
        nave_coords = C_app.coords(nave)
        img_disparo = cargar_disparo('disparo_3.png')
        laser = C_app.create_image(nave_coords[0] + 37, nave_coords[1] + 30, anchor=NW, image=img_disparo, tag="laser")
        Thread(target = disparo_nave, args=(img_disparo, laser)).start()


#Controles -------------------------------------------------------------------------------------------------
   
    ventana.bind('<Right>', derecha)
    ventana.bind('<Left>', izquierda)
    ventana.bind('<Up>', arriba)
    ventana.bind('<Down>', abajo)
    ventana.bind ('<space><KeyRelease>', llamada_disparo)


#Resto de elementos visuales y botones -----------------------------------------------------------------------
    Btn_principal = Button(ventana, text='Presiona para volver a la pantalla principal' , font=fuente_global, command=pantalla_principal)
    Btn_principal.place(x=150 , y=800)


    labelpuntaje = Label(ventana, text = "Puntaje: ", bg='#1c1b1a', fg='#ad1fa9', font=fuente_global)
    labelpuntaje.place(x=0, y=10)

    label_puntaje = Label(ventana, text = puntaje , bg='#1c1b1a', fg='#ad1fa9', font=fuente_vida)
    label_puntaje.place(x=100, y=10)


#Vida del Jefe 1 ----------------------------------------------------------------------------------------------
    labeljefe = Label(ventana, text = vida_boss1, bg='#1c1b1a', fg='#ad1fa9', font=fuente_vida)
    labeljefe.place(x=200 , y=865)

    label_jefe = Label(ventana, text = 'Vida del Jefe 1:' , bg='#1c1b1a', fg='#ad1fa9', font=fuente_global)
    label_jefe.place(x=30 , y=875)
    
 
#Vida del jugador ----------------------------------------------------------------------------------------------
    labelplayer = Label(ventana, text = vida_jugador, bg='#1c1b1a', fg='#ad1fa9', font=fuente_vida)
    labelplayer.place(x=600 , y=865)

    label_player = Label(ventana, text = 'Vida de {x}'.format(x=nombre_usuario), bg='#1c1b1a', fg='#ad1fa9', font=fuente_global)
    label_player.place(x=380 , y=875)


#cronómetro ----------------------------------------------------------------------------------------------
    labelsegundos = Label(ventana, text = segundos , bg='#1c1b1a', fg='#ad1fa9', font=fuente_vida)
    labelsegundos.place(x=600 , y=10)

    label_segundos = Label(ventana, text = 'Cronometro:' , bg='#1c1b1a', fg='#ad1fa9', font=fuente_global)
    label_segundos.place(x=480 , y=10)
    

#Cronometro (módulo editado)--------------------------------------------------------------------------------------------------------------------------
    def iniciar():
        global segundos
        if FLAG3 == True:
            segundos +=1
            time.sleep(1)
            if segundos == 1000:
                segundos = 0
            labelsegundos.config(text = segundos)
            return iniciar()
        

#Llamado de los modulos ------------------------------------------------------------------------------------

    derecha('<Right>')
    movi_izq_der(Boss1, img_Boss1,95,0)
    Thread(target = iniciar).start()




#Ventana Boss 2 ==============================================================================================================================================
def pantalla_boss2():
    global vida_boss2, vida_jugador, FLAG2, FLAG3, segundos, FLAG
    FLAG2 = True
    FLAG3 = True
    vida_jugador = 50
    segundos = 0
    C_app = Canvas(ventana, width=700 ,height = 933)
    C_app.place(x=0,y=0)
    C_app.fondo = cargar_img('fondo_2.jpg') 
    fondo = C_app.create_image(0,0,anchor=NW,image=C_app.fondo)
    
    reproducir_cancion(cargarMP3('Boss_2.mp3'))

    C_app2 = Canvas(ventana, width= 700, height= 600, bg='#1c1b1a')
    C_app2.place(x=0,y=855)

    C_app3 = Canvas(ventana, width= 700, height= 80, bg='#1c1b1a')
    C_app3.place(x=0,y=0)

    img_Boss2 = cargar_nave('Boss_2.png')
    Boss2 = C_app.create_image(0, 75, anchor=NW, tags= ('Boss2'))


#Movimiento de horizontal del Jefe 2 -----------------------------------------------------------------------------
    def horizontal(Boss2,img_Boss2,conteo,teleport):
        global FLAG
        current_coords = C_app.coords(Boss2)
        conteo -= 1
        C_app.coords(Boss2, current_coords[0], current_coords[1]) #cantidad de espacios que se mueve
        C_app.itemconfig('Boss2', image=img_Boss2)
        #Condiciones para que termine la partida ---------------------
        if vida_boss2 <= 0:
            return pantalla_boss2

        if vida_jugador < 0:
            time.sleep(5)
            return pantalla_resultados()

        if conteo == 100:
            reproducir_fx(cargarMP3('disparo_boss2.mp3'))
            FLAG = True
            img_disparo_boss2_1 = cargar_disparo('disparo_2.png')
            laser_boss2_1 = C_app.create_image(current_coords[0] + 100, current_coords[1]+ 175, anchor=NW, image=img_disparo_boss2_1, tag="laser_boss2_1")
            Thread(target = disparo_boss2_1, args=(img_disparo_boss2_1, laser_boss2_1)).start()

            img_disparo_boss2_2 = cargar_disparo('disparo_2.png')
            laser_boss2_2 = C_app.create_image(current_coords[0] + 175, current_coords[1]+ 175, anchor=NW, image=img_disparo_boss2_2, tag="laser_boss2_2")
            Thread(target = disparo_boss2_2, args=(img_disparo_boss2_2, laser_boss2_2)).start()

            img_disparo_boss2_3 = cargar_disparo('disparo_2.png')
            laser_boss2_3 = C_app.create_image(current_coords[0] + 200, current_coords[1]+ 175, anchor=NW, image=img_disparo_boss2_3, tag="laser_boss2_3")
            Thread(target = disparo_boss2_3, args=(img_disparo_boss2_3, laser_boss2_3)).start()
            
            
        if conteo == 0:
            conteo = 200 #2 segundos entre posible envestida 
            teleport = random.randint(0,200)
            C_app.coords(Boss2, teleport, current_coords[1]) #cantidad de espacios que se mueve
            C_app.itemconfig('Boss2', image=img_Boss2)


        def callback():
            return horizontal(Boss2,img_Boss2,conteo,teleport) #Transisción entre fotogramas
        ventana.after(10, callback) #velocidad


#Módulo de movimiento del personaje (módulos editado)-------------------------------------------------------------- 
    img_nave = cargar_nave('nave_personaje.png')
    nave = C_app.create_image(300, 650, anchor=NW, tags= ('nave'))

    def derecha(event):
        current_coords = C_app.coords(nave)
        if current_coords[0] != 570: #Límite
            C_app.coords(nave, current_coords[0]+15, current_coords[1])
            C_app.itemconfig('nave', image=img_nave)
        
    def izquierda(event):
        current_coords = C_app.coords(nave)
        if current_coords[0] != 30: #Límite
            C_app.coords(nave, current_coords[0]-15, current_coords[1])
            C_app.itemconfig('nave', image=img_nave)
        
    def arriba(event):
        current_coords = C_app.coords(nave)
        if current_coords[1] != 5: #Límite
            C_app.coords(nave, current_coords[0], current_coords[1]-15)
            C_app.itemconfig('nave', image=img_nave)
            
    def abajo(event):
        current_coords = C_app.coords(nave)
        if current_coords[1] != 680: #Límite
            C_app.coords(nave, current_coords[0], current_coords[1]+15)
            C_app.itemconfig('nave', image=img_nave)


#Módulo de disparo del jefe -------------------------------------------------------------------------------------------
    #Primer proyectil --------------------------------------------------------
    def disparo_boss2_1(img_disparo_boss2_1, laser_boss2_1):
        global vida_jugador, FLAG
        if FLAG == True:
            #Condiciones para que termine la partida ---------------------------------------------------
            if vida_jugador < 0:
                time.sleep(5)
                return pantalla_resultados()

            #Detecta colision ----------------------------------------------------------------------------
            hitbox_laser_boss2 = C_app.bbox(laser_boss2_1)
            hitbox_nave = C_app.bbox(nave)
            if vida_jugador == 0:
                FLAG == False
                return pantalla_resultados()

            if hitbox_nave[0]-5 < hitbox_laser_boss2[0] and hitbox_nave[2]+5 > hitbox_laser_boss2[2]:
                if hitbox_nave[1]-5 < hitbox_laser_boss2[1] and hitbox_nave[3]+5 > hitbox_laser_boss2[3]:
                    vida_jugador -= 1
                    C_app.delete(laser_boss2_1)
                    FLAG == False
                    labelplayer.config(text = vida_jugador)
                    return 0

            #Movimiento del disparo ---------------------------------------------------------------------
            current_coords = C_app.coords(laser_boss2_1)
            if (current_coords[1]==700):
                C_app.delete(laser_boss2_1)
                FLAG == False
                return horizontal(Boss2,img_Boss2,0,0)

            C_app.coords(laser_boss2_1, current_coords[0], current_coords[1]+3) #cantidad de espacios que se mueve
            C_app.itemconfig('laser_boss2_1', image=img_disparo_boss2_1)

            def callback():
                disparo_boss2_1(img_disparo_boss2_1, laser_boss2_1) #Transisción entre fotogramas
            ventana.after(1, callback)



    #segundo proyectil --------------------------------------------------------
    def disparo_boss2_2(img_disparo_boss2_2, laser_boss2_2):
        global vida_jugador, FLAG
        if FLAG == True:
        #Condiciones para que termine la partida ---------------------------------------------------
            if vida_jugador < 0:
                time.sleep(5)
                FLAG == False
                return pantalla_resultados()


            #Detecta colision ----------------------------------------------------------------------------
            hitbox_laser_boss2 = C_app.bbox(laser_boss2_2)
            hitbox_nave = C_app.bbox(nave)
            if vida_jugador == 0:
                FLAG == False
                return pantalla_resultados()

            if hitbox_nave[0]-5 < hitbox_laser_boss2[0] and hitbox_nave[2]+5 > hitbox_laser_boss2[2]:
                if hitbox_nave[1]-5 < hitbox_laser_boss2[1] and hitbox_nave[3]+5 > hitbox_laser_boss2[3]:
                    vida_jugador -= 1
                    C_app.delete(laser_boss2_2)
                    FLAG == False
                    labelplayer.config(text = vida_jugador)
                    return 0

            #Movimiento del disparo ---------------------------------------------------------------------
            current_coords = C_app.coords(laser_boss2_2)
            if (current_coords[1]==700):
                C_app.delete(laser_boss2_2)
                FLAG == False
                return horizontal(Boss2,img_Boss2,0,0)

            C_app.coords(laser_boss2_2, current_coords[0], current_coords[1]+3) #cantidad de espacios que se mueve
            C_app.itemconfig('laser_boss2_2', image=img_disparo_boss2_2)

            def callback():
                disparo_boss2_2(img_disparo_boss2_2, laser_boss2_2) #Transisción entre fotogramas
            ventana.after(1, callback)

    #tercer proyectil --------------------------------------------------------
    def disparo_boss2_3(img_disparo_boss2_3, laser_boss2_3):
        global vida_jugador, FLAG
        if FLAG == True:
            #Condiciones para que termine la partida ---------------------------------------------------
            if vida_jugador < 0:
                FLAG == False
                time.sleep(5)
                return pantalla_resultados()


            #Detecta colision ----------------------------------------------------------------------------
            hitbox_laser_boss2 = C_app.bbox(laser_boss2_3)
            hitbox_nave = C_app.bbox(nave)
            if vida_jugador == 0:
                FLAG == False
                return pantalla_resultados()

            if hitbox_nave[0] < hitbox_laser_boss2[0] and hitbox_nave[2] > hitbox_laser_boss2[2]:
                if hitbox_nave[1] < hitbox_laser_boss2[1] and hitbox_nave[3] > hitbox_laser_boss2[3]:
                    vida_jugador -= 1
                    C_app.delete(laser_boss2_3)
                    FLAG == False
                    labelplayer.config(text = vida_jugador)
                    return 0

            #Movimiento del disparo ---------------------------------------------------------------------
            current_coords = C_app.coords(laser_boss2_3)
            if (current_coords[1]==700):
                C_app.delete(laser_boss2_3)
                FLAG == False
                return horizontal(Boss2,img_Boss2,0,0)

            C_app.coords(laser_boss2_3, current_coords[0], current_coords[1]+3) #cantidad de espacios que se mueve
            C_app.itemconfig('laser_boss2_3', image=img_disparo_boss2_3)

            def callback():
                disparo_boss2_3(img_disparo_boss2_3, laser_boss2_3) #Transisción entre fotogramas
            ventana.after(1, callback)


#Resto de elementos visuales y botones -----------------------------------------------------------------------------
    def devolver():
        global FLAG
        FLAG = False
        return pantalla_principal()

    Btn_principal = Button(ventana, text='Presiona para volver a la pantalla principal' , font=fuente_global, command=devolver)
    Btn_principal.place(x=150 , y=800)

    labelpuntaje = Label(ventana, text = "Puntaje: ", bg='#1c1b1a', fg='#ad1fa9', font=fuente_global)
    labelpuntaje.place(x=0, y=0)

    label_puntaje = Label(ventana, text = puntaje , bg='#1c1b1a', fg='#ad1fa9', font=fuente_vida)
    label_puntaje.place(x=100, y=0)


#Vida del Jefe 2 ----------------------------------------------------------------------------------------------
    labeljefe = Label(ventana, text = vida_boss2, bg='#1c1b1a', fg='#ad1fa9', font=fuente_vida)
    labeljefe.place(x=200 , y=865)

    label_jefe = Label(ventana, text = 'Vida del Jefe 2', bg='#1c1b1a', fg='#ad1fa9', font=fuente_global)
    label_jefe.place(x=30 , y=875)
    
 
#Vida del jugador ----------------------------------------------------------------------------------------------
    labelplayer = Label(ventana, text = vida_jugador, bg='#1c1b1a', fg='#ad1fa9', font=fuente_vida)
    labelplayer.place(x=600 , y=865)

    label_player = Label(ventana, text = 'Vida de {x}'.format(x=nombre_usuario), bg='#1c1b1a', fg='#ad1fa9', font=fuente_global)
    label_player.place(x=380 , y=875)


#Módulo de disparo --------------------------------------------------------------------------------------------------------------------
    def disparo_nave(img_disparo, laser):
        global vida_boss2, puntaje, vida_jugador, segundos
        #Condiciones para que termine la partida ---------------------------------------------------
        if FLAG2 == True:
            if vida_jugador <= 0:
                time.sleep(5)
                return pantalla_resultados()

            #Detecta colision ----------------------------------------------------------------------------
            hitbox_laser= C_app.bbox(laser)
            hitbox_boss2 = C_app.bbox(Boss2)
            if vida_boss2 <= 0:
                FLAG2 == False
                if vida_jugador == 50:
                    puntaje += 10
                    label_puntaje.config(text = puntaje)
                    if segundos <= 30:
                        puntaje += 20
                        label_puntaje.config(text = puntaje)
                        return pantalla_boss3()
                    else:
                        return pantalla_boss3()
                else:
                    return pantalla_boss3()

            if hitbox_boss2[0] < hitbox_laser[0] and hitbox_boss2[2] > hitbox_laser[2]:
                if hitbox_boss2[1] < hitbox_laser[1] and hitbox_boss2[3] > hitbox_laser[3]:
                    vida_boss2 -= 1
                    puntaje += 1
                    label_puntaje.config(text= puntaje)
                    C_app.delete(laser)
                    FLAG2 == False
                    labeljefe.config(text = vida_boss2)
                    return 0

            #Movimiento del disparo ---------------------------------------------------------------------
            laser_coords = C_app.coords(laser)
            if (laser_coords[1]==0):
                C_app.delete(laser)
                FLAG2 == False
                return 0

            C_app.coords(laser, laser_coords[0], laser_coords[1] -5) #cantidad de espacios que se mueve
            C_app.itemconfig('laser', image=img_disparo)


            def callback():
                disparo_nave(img_disparo, laser) #Transisción entre fotogramas
            ventana.after(1, callback)

    def llamada_disparo(event):
        if FLAG == True:
            reproducir_fx(cargarMP3('disparo_jugador.mp3'))
            nave_coords = C_app.coords(nave)
            img_disparo = cargar_disparo('disparo_3.png')
            laser = C_app.create_image(nave_coords[0] + 37, nave_coords[1] + 30, anchor=NW, image=img_disparo, tag="laser")
            Thread(target = disparo_nave, args=(img_disparo, laser)).start()


#cronómetro ----------------------------------------------------------------------------------------------
    labelsegundos = Label(ventana, text = segundos , bg='#1c1b1a', fg='#ad1fa9', font=fuente_vida)
    labelsegundos.place(x=600 , y=10)

    label_segundos = Label(ventana, text = 'Cronometro:' , bg='#1c1b1a', fg='#ad1fa9', font=fuente_global)
    label_segundos.place(x=480 , y=10)
    

#Cronometro --------------------------------------------------------------------------------------------------------------------------
    def iniciar():
        global segundos
        if FLAG3 == True:
            segundos +=1
            time.sleep(1)
            if segundos == 1000:
                segundos = 0
            labelsegundos.config(text = segundos)
            return iniciar()

            
        def callback():
            return iniciar()
        ventana.after(1000, callback)
        

#Controles -----------------------------------------------------------------------------------------------------------

    ventana.bind('<Right>', derecha)
    ventana.bind('<Left>', izquierda)
    ventana.bind('<Up>', arriba)
    ventana.bind('<Down>', abajo)
    ventana.bind ('<space><KeyRelease>', llamada_disparo)


#Llamado de los movimientos de las naves ------------------------------------------------------------------------------
    derecha('<Right>')
    horizontal(Boss2,img_Boss2,200,0)
    Thread(target = iniciar).start()
    








#Ventana Boss 3 =================================================================================================================================================
def pantalla_boss3():
    global vida_boss3, vida_jugador, FLAG3, segundos
    FLAG3 = TRUE
    vida_jugador = 50
    segundos = 0
    C_app = Canvas(ventana, width=700 ,height = 933)
    C_app.place(x=0,y=0)
    C_app.fondo = cargar_img('fondo_3.jpg') 
    fondo = C_app.create_image(0,0,anchor=NW,image=C_app.fondo)
    
    reproducir_cancion(cargarMP3('Boss_3.mp3'))
    
    C_app2 = Canvas(ventana, width= 700, height= 600, bg='#1c1b1a')
    C_app2.place(x=0,y=855)

    C_app3 = Canvas(ventana, width= 700, height= 80, bg='#1c1b1a')
    C_app3.place(x=0,y=0)

    img_Boss3 = cargar_nave('Boss_3.png')
    Boss3 = C_app.create_image(0, 75, anchor=NW, tags= ('Boss3'))


#Movimiento de izquierda a derecha--------------------------------------------------------------------------------------
    def movi_izq_der(Boss3,img_Boss3,conteo):
        #Condiciones para que termine la partida ---------------------
        global FLAG
        current_coords = C_app.coords(Boss3)
        if vida_boss3 < 0:
            time.sleep(5)
            return pantalla_resultados()

        if vida_jugador < 0:
            time.sleep(5)
            return pantalla_resultados()   
        
        if conteo == 500 or conteo == 200:
            reproducir_fx(cargarMP3('disparo_boss3.mp3'))
            FLAG = True
            img_disparo_boss3_1 = cargar_disparo('disparo_4.png')
            laser_boss3_1 = C_app.create_image(current_coords[0] + 100, current_coords[1]+ 175, anchor=NW, image=img_disparo_boss3_1, tag="laser_boss3_1")
            disparo_boss3_1(img_disparo_boss3_1, laser_boss3_1)

            img_disparo_boss3_2 = cargar_disparo('disparo_4.png')
            laser_boss3_2 = C_app.create_image(current_coords[0] + 175, current_coords[1]+ 175, anchor=NW, image=img_disparo_boss3_2, tag="laser_boss3_2")
            disparo_boss3_2(img_disparo_boss3_2, laser_boss3_2)

            img_disparo_boss3_3 = cargar_disparo('disparo_4.png')
            laser_boss3_3 = C_app.create_image(current_coords[0] + 200, current_coords[1]+ 175, anchor=NW, image=img_disparo_boss3_3, tag="laser_boss3_3")
            disparo_boss3_3(img_disparo_boss3_3, laser_boss3_3)


        current_coords = C_app.coords(Boss3)
        if (current_coords[0]>258):
            return movi_der_izq(Boss3, img_Boss3,conteo)
        C_app.coords(Boss3, current_coords[0]+2, current_coords[1]) #cantidad de espacios que se mueve
        C_app.itemconfig('Boss3', image=img_Boss3)
        conteo -= 1
        if conteo == 0:
            conteo = 600 #6 segundos entre posible envestida 
            time.sleep(0.5)
            return arriba_abajo(Boss3, img_Boss3, conteo, nave)

        def callback():
            movi_izq_der(Boss3, img_Boss3,conteo) #Transisción entre fotogramas
        ventana.after(10, callback) #velocidad


#Movimiento de derecha a izquierda--------------------------------------------------------------------------------------
    def movi_der_izq(Boss3,img_Boss3,conteo):
        #Condiciones para que termine la partida ---------------------
        current_coords = C_app.coords(Boss3)
        if vida_boss3 < 0:
            time.sleep(5)
            return pantalla_resultados()

        if vida_jugador < 0:
            time.sleep(5)
            return pantalla_resultados()

        if conteo == 500 or conteo == 200:
            reproducir_fx(cargarMP3('disparo_boss3.mp3'))
            FLAG = True
            img_disparo_boss3_1 = cargar_disparo('disparo_4.png')
            laser_boss3_1 = C_app.create_image(current_coords[0] + 100, current_coords[1]+ 175, anchor=NW, image=img_disparo_boss3_1, tag="laser_boss3_1")
            Thread(target = disparo_boss3_1, args=(img_disparo_boss3_1, laser_boss3_1)).start()

            img_disparo_boss3_2 = cargar_disparo('disparo_4.png')
            laser_boss3_2 = C_app.create_image(current_coords[0] + 175, current_coords[1]+ 175, anchor=NW, image=img_disparo_boss3_2, tag="laser_boss3_2")
            Thread(target = disparo_boss3_2, args=(img_disparo_boss3_2, laser_boss3_2)).start()

            img_disparo_boss3_3 = cargar_disparo('disparo_4.png')
            laser_boss3_3 = C_app.create_image(current_coords[0] + 200, current_coords[1]+ 175, anchor=NW, image=img_disparo_boss3_3, tag="laser_boss3_3")
            Thread(target = disparo_boss3_3, args=(img_disparo_boss3_3, laser_boss3_3)).start()



        current_coords = C_app.coords(Boss3)
        if (current_coords[0]==0):
            return movi_izq_der(Boss3,img_Boss3,conteo)
        current_coords = C_app.coords(Boss3)
        C_app.coords(Boss3, current_coords[0]-1, current_coords[1]) #cantidad de espacios que se mueve
        C_app.itemconfig('Boss3', image=img_Boss3)
        conteo -= 1
        if conteo == 0:
            conteo = 600 #6 segundos entre posible envestida 
            time.sleep(0.5)
            return arriba_abajo(Boss3, img_Boss3, conteo, nave)

        def callback():
            movi_der_izq(Boss3,img_Boss3,conteo) #Transisción entre fotogramas
        ventana.after(10, callback) #velocidad


#Embestida Boss 3 (módulo editado)--------------------------------------------------------------------------------------
    def arriba_abajo(Boss3, img_Boss3, conteo, nave):
        global vida_boss1, vida_jugador, segundo, minuto
        #Condiciones para que termine la partida ---------------------
        if vida_boss3 < 0:
            time.sleep(5)
            return pantalla_resultados()

        if vida_jugador < 0:
            time.sleep(5)
            return pantalla_resultados()


        current_coords = C_app.coords(Boss3)
        nave_coords = C_app.coords(nave)

        if (current_coords[1]==550):
            colision_boss3_nave(Boss3, nave)

            labeljefe.config(text = vida_boss1)
            labelplayer.config(text = vida_jugador)
            return abajo_arriba(Boss3, img_Boss3,conteo,0)
        
        current_coords = C_app.coords(Boss3)
        C_app.coords(Boss3, current_coords[0], current_coords[1]+1) #cantidad de espacios que se mueve
        C_app.itemconfig('Boss3', image=img_Boss3)


        def callback():
            arriba_abajo(Boss3, img_Boss3, conteo, nave) #Transisción entre fotogramas
        ventana.after(1, callback)


#Movimiento vertical  (módulo editado)---------------------------------------------------------------------------------
    def abajo_arriba(Boss3, img_Boss3,conteo,probabilidad):
        #Condiciones para que termine la partida ---------------------
        if vida_boss3 <= 0:
            time.sleep(5)
            return pantalla_resultados()

        if vida_jugador < 0:
            time.sleep(5)
            return pantalla_resultados()


        current_coords = C_app.coords(Boss3)
        if (current_coords[1]==75):
            probabilidad = random.randint(1,2)
            if probabilidad == 1:
                if (current_coords[0]>50):
                    return movi_der_izq(Boss3, img_Boss3,conteo) #movimiento hacia la izquierda
                else:
                    return movi_izq_der(Boss3, img_Boss3,conteo) #movimiento hacia la derecha
            if probabilidad == 2:
                teleport = random.randint(0,200)
                C_app.coords(Boss3, teleport, current_coords[1]) #cantidad de espacios que se mueve
                C_app.itemconfig('Boss3', image=img_Boss3)
                return arriba_abajo(Boss3, img_Boss3, conteo, nave)

        current_coords = C_app.coords(Boss3)
        C_app.coords(Boss3, current_coords[0], current_coords[1]-1) #cantidad de espacios que se mueve
        C_app.itemconfig('Boss3', image=img_Boss3)

        def callback():
            abajo_arriba(Boss3, img_Boss3,conteo,0) #Transisción entre fotogramas
        ventana.after(1, callback)


#Módulo de movimiento del personaje (módulos editado)--------------------------------------------------------------------  
    img_nave = cargar_nave('nave_personaje.png')
    nave = C_app.create_image(300, 650, anchor=NW, tags= ('nave'))

    def derecha(event):
        current_coords = C_app.coords(nave)
        if current_coords[0] != 570: #Límite
            C_app.coords(nave, current_coords[0]+15, current_coords[1])
            C_app.itemconfig('nave', image=img_nave)
        
    def izquierda(event):
        current_coords = C_app.coords(nave)
        if current_coords[0] != 30: #Límite
            C_app.coords(nave, current_coords[0]-15, current_coords[1])
            C_app.itemconfig('nave', image=img_nave)
        
    def arriba(event):
        current_coords = C_app.coords(nave)
        if current_coords[1] != 5: #Límite
            C_app.coords(nave, current_coords[0], current_coords[1]-15)
            C_app.itemconfig('nave', image=img_nave)
            
    def abajo(event):
        current_coords = C_app.coords(nave)
        if current_coords[1] != 680: #Límite
            C_app.coords(nave, current_coords[0], current_coords[1]+15)
            C_app.itemconfig('nave', image=img_nave)


#Sistema de colisiones y puntaje (Pantalla Boss 3)---------------------------------------------------------
    def colision_boss3_nave(Boss3, nave):
        global vida_jugador, vida_boss3, puntaje
        hitbox_boss3 = C_app.bbox(Boss3)
        hitbox_nave = C_app.bbox(nave)
        if vida_boss1 == 0:
            vida_jugador = 50
            return pantalla_boss2

        if hitbox_boss3[0] < hitbox_nave[0] and hitbox_boss3[2] > hitbox_nave[2]:
            if hitbox_boss3[1] < hitbox_nave[1] and hitbox_boss3[3] > hitbox_nave[3]:
                vida_jugador -= 10
                labelplayer.config(text = vida_jugador) 



    def llamada_disparo(event):
        reproducir_fx(cargarMP3('disparo_jugador.mp3'))


#Módulo de disparo --------------------------------------------------------------------------------------------------------------------
    def disparo_nave(img_disparo, laser):
        global vida_boss3, puntaje, vida_jugador, segundos
        #Condiciones para que termine la partida ---------------------------------------------------
        if FLAG2 == True:
            if vida_jugador <= 0:
                time.sleep(5)
                return pantalla_resultados()

            #Detecta colision ----------------------------------------------------------------------------
            hitbox_laser= C_app.bbox(laser)
            hitbox_boss3 = C_app.bbox(Boss3)
            if vida_boss3 < 0:
                FLAG2 == False
                if vida_jugador == 50:
                    puntaje += 10
                    label_puntaje.config(text = puntaje)
                    if segundos <= 30:
                        puntaje += 20
                        label_puntaje.config(text = puntaje)
                        return pantalla_resultados()
                    else:
                        return pantalla_resultados()
                else:
                    return pantalla_resultados()

            if hitbox_boss3[0] < hitbox_laser[0] and hitbox_boss3[2] > hitbox_laser[2]:
                if hitbox_boss3[1] < hitbox_laser[1] and hitbox_boss3[3] > hitbox_laser[3]:
                    vida_boss3 -= 1
                    puntaje += 1
                    label_puntaje.config(text= puntaje)
                    C_app.delete(laser)
                    FLAG2 == False
                    labeljefe.config(text = vida_boss3)
                    return 0

            #Movimiento del disparo ---------------------------------------------------------------------
            laser_coords = C_app.coords(laser)
            if (laser_coords[1]==0):
                C_app.delete(laser)
                FLAG2 == False
                return 0

            C_app.coords(laser, laser_coords[0], laser_coords[1] -5) #cantidad de espacios que se mueve
            C_app.itemconfig('laser', image=img_disparo)


            def callback():
                disparo_nave(img_disparo, laser) #Transisción entre fotogramas
            ventana.after(1, callback)

    def llamada_disparo(event):
        reproducir_fx(cargarMP3('disparo_jugador.mp3'))
        nave_coords = C_app.coords(nave)
        img_disparo = cargar_disparo('disparo_3.png')
        laser = C_app.create_image(nave_coords[0] + 37, nave_coords[1] + 30, anchor=NW, image=img_disparo, tag="laser")
        Thread(target = disparo_nave, args=(img_disparo, laser)).start()


#Módulo de disparo del jefe -------------------------------------------------------------------------------------------
    #Primer proyectil --------------------------------------------------------
    def disparo_boss3_1(img_disparo_boss2_1, laser_boss2_1):
        global vida_jugador, FLAG
        if FLAG == True:
            #Condiciones para que termine la partida ---------------------------------------------------
            if vida_jugador < 0:
                time.sleep(5)
                return pantalla_resultados()

            #Detecta colision ----------------------------------------------------------------------------
            hitbox_laser_boss2 = C_app.bbox(laser_boss2_1)
            hitbox_nave = C_app.bbox(nave)
            if vida_jugador == 0:
                FLAG == False
                return pantalla_resultados()

            if hitbox_nave[0]-5 < hitbox_laser_boss2[0] and hitbox_nave[2]+5 > hitbox_laser_boss2[2]:
                if hitbox_nave[1]-5 < hitbox_laser_boss2[1] and hitbox_nave[3]+5 > hitbox_laser_boss2[3]:
                    vida_jugador -= 1
                    C_app.delete(laser_boss2_1)
                    FLAG == False
                    labelplayer.config(text = vida_jugador)
                    return 0

            #Movimiento del disparo ---------------------------------------------------------------------
            current_coords = C_app.coords(laser_boss2_1)
            if (current_coords[1]==700):
                C_app.delete(laser_boss2_1)
                FLAG == False
                
                if (current_coords[0]>50):
                    return movi_der_izq(Boss3, img_Boss3,0) #movimiento hacia la izquierda
                else:
                    return movi_izq_der(Boss3, img_Boss3,0) #movimiento hacia la derecha

            C_app.coords(laser_boss2_1, current_coords[0], current_coords[1]+3) #cantidad de espacios que se mueve
            C_app.itemconfig('laser_boss2_1', image=img_disparo_boss2_1)

            def callback():
                disparo_boss3_1(img_disparo_boss2_1, laser_boss2_1) #Transisción entre fotogramas
            ventana.after(1, callback)



    #segundo proyectil --------------------------------------------------------
    def disparo_boss3_2(img_disparo_boss2_2, laser_boss2_2):
        global vida_jugador, FLAG
        if FLAG == True:
        #Condiciones para que termine la partida ---------------------------------------------------
            if vida_jugador < 0:
                time.sleep(5)
                FLAG == False
                return pantalla_resultados()


            #Detecta colision ----------------------------------------------------------------------------
            hitbox_laser_boss2 = C_app.bbox(laser_boss2_2)
            hitbox_nave = C_app.bbox(nave)
            if vida_jugador == 0:
                FLAG == False
                return pantalla_resultados()

            if hitbox_nave[0]-5 < hitbox_laser_boss2[0] and hitbox_nave[2]+5 > hitbox_laser_boss2[2]:
                if hitbox_nave[1]-5 < hitbox_laser_boss2[1] and hitbox_nave[3]+5 > hitbox_laser_boss2[3]:
                    vida_jugador -= 1
                    C_app.delete(laser_boss2_2)
                    FLAG == False
                    labelplayer.config(text = vida_jugador)
                    return 0

            #Movimiento del disparo ---------------------------------------------------------------------
            current_coords = C_app.coords(laser_boss2_2)
            if (current_coords[1]==700):
                C_app.delete(laser_boss2_2)
                FLAG == False
                return movi_izq_der(Boss3,img_Boss3,0)

            C_app.coords(laser_boss2_2, current_coords[0], current_coords[1]+3) #cantidad de espacios que se mueve
            C_app.itemconfig('laser_boss2_2', image=img_disparo_boss2_2)

            def callback():
                disparo_boss3_2(img_disparo_boss2_2, laser_boss2_2) #Transisción entre fotogramas
            ventana.after(1, callback)

    #tercer proyectil --------------------------------------------------------
    def disparo_boss3_3(img_disparo_boss2_3, laser_boss2_3):
        global vida_jugador, FLAG
        if FLAG == True:
            #Condiciones para que termine la partida ---------------------------------------------------
            if vida_jugador < 0:
                FLAG == False
                time.sleep(5)
                return pantalla_resultados()


            #Detecta colision ----------------------------------------------------------------------------
            hitbox_laser_boss2 = C_app.bbox(laser_boss2_3)
            hitbox_nave = C_app.bbox(nave)
            if vida_jugador == 0:
                FLAG == False
                return pantalla_resultados()

            if hitbox_nave[0] < hitbox_laser_boss2[0] and hitbox_nave[2] > hitbox_laser_boss2[2]:
                if hitbox_nave[1] < hitbox_laser_boss2[1] and hitbox_nave[3] > hitbox_laser_boss2[3]:
                    vida_jugador -= 1
                    C_app.delete(laser_boss2_3)
                    FLAG == False
                    labelplayer.config(text = vida_jugador)
                    return 0

            #Movimiento del disparo ---------------------------------------------------------------------
            current_coords = C_app.coords(laser_boss2_3)
            if (current_coords[1]==700):
                C_app.delete(laser_boss2_3)
                FLAG == False
                return movi_izq_der(Boss3,img_Boss3,0)

            C_app.coords(laser_boss2_3, current_coords[0], current_coords[1]+3) #cantidad de espacios que se mueve
            C_app.itemconfig('laser_boss2_3', image=img_disparo_boss2_3)

            def callback():
                disparo_boss3_3(img_disparo_boss2_3, laser_boss2_3) #Transisción entre fotogramas
            ventana.after(1, callback)


#Controles ---------------------------------------------------------------------------------------------------------------

    ventana.bind('<Right>', derecha)
    ventana.bind('<Left>', izquierda)
    ventana.bind('<Up>', arriba)
    ventana.bind('<Down>', abajo)
    ventana.bind ('<space><KeyRelease>', llamada_disparo)


#Resto de elementos visuales y botones ------------------------------------------------------------------------------------
    Btn_ranking = Button(ventana, text='Presiona para volver a la pantalla principal' , font=fuente_global, command=pantalla_principal)
    Btn_ranking.place(x=150 , y=800)

    labelpuntaje = Label(ventana, text = "Puntaje: ", bg='#1c1b1a', fg='#ad1fa9', font=fuente_global)
    labelpuntaje.place(x=0, y=10)

    label_puntaje = Label(ventana, text = puntaje , bg='#1c1b1a', fg='#ad1fa9', font=fuente_vida)
    label_puntaje.place(x=100, y=0)


#Vida del Jefe 3 ----------------------------------------------------------------------------------------------
    labeljefe = Label(ventana, text = vida_boss3, bg='#1c1b1a', fg='#ad1fa9', font=fuente_vida)
    labeljefe.place(x=200 , y=865)

    label_jefe = Label(ventana, text = 'Vida del Jefe 3', bg='#1c1b1a', fg='#ad1fa9', font=fuente_global)
    label_jefe.place(x=30 , y=875)
    
 
#Vida del jugador ----------------------------------------------------------------------------------------------
    labelplayer = Label(ventana, text = vida_jugador, bg='#1c1b1a', fg='#ad1fa9', font=fuente_vida)
    labelplayer.place(x=600 , y=865)

    label_player = Label(ventana, text = 'Vida de {x}'.format(x=nombre_usuario), bg='#1c1b1a', fg='#ad1fa9', font=fuente_global)
    label_player.place(x=380 , y=875)


#cronómetro ----------------------------------------------------------------------------------------------
    labelsegundos = Label(ventana, text = segundos , bg='#1c1b1a', fg='#ad1fa9', font=fuente_vida)
    labelsegundos.place(x=600 , y=10)

    label_segundos = Label(ventana, text = 'Cronometro:' , bg='#1c1b1a', fg='#ad1fa9', font=fuente_global)
    label_segundos.place(x=480 , y=10)
    

#Cronometro --------------------------------------------------------------------------------------------------------------------------
    def iniciar():
        global segundos
        if FLAG3 == True:
            segundos +=1
            time.sleep(1)
            if segundos == 1000:
                segundos = 0
            labelsegundos.config(text = segundos)
            return iniciar()

            
        def callback():
            return iniciar()
        ventana.after(1000, callback)


#Llamado de los movimientos de las naves --------------------------------------------------------------------------------- 
    derecha('<Right>')
    movi_izq_der(Boss3, img_Boss3,600)
    Thread(target = iniciar).start()



#Ventana de pantalla principal ====================================================================================================================================
def pantalla_principal():
    global MiArchi1, vida_boss1, vida_boss2, vida_boss3, vida_jugador, nombre_usuario, puntaje, segundos
    time.sleep(0.2)  
    vida_jugador = 50
    vida_boss1 = 30
    vida_boss2 = 40
    vida_boss3 = 50
    puntaje = 0
    segundos = 0
    ventana.minsize(700,933)

    C_app = Canvas(ventana, width=700 ,height = 933)
    C_app.place(x=0,y=0)
    C_app.fondo = cargar_img('fondo_principal.png') 
    fondo = C_app.create_image(0,0,anchor=NW,image=C_app.fondo)

    reproducir_cancion(cargarMP3('Menu.mp3'))

    L_intro = Label(ventana, font=(fuente_global), bg='#4b2775',     fg='#ad1fa9',     text=intro)
    L_intro.place(x=250, y=150)

    L_jugador = Label(ventana, font=(fuente_global), bg='#4b2775',     fg='#ad1fa9',     text='Hola {x}, listo para destruir unas naves alienígenas?'.format(x=nombre_usuario))
    L_jugador.place(x=50, y=300)

    Btn_new_game = Button(ventana, text='Presiona para jugar' ,  bg='#1c1b1b',     fg='#ad1fa9', font=fuente_global, command=pantalla_boss1)
    Btn_new_game.place(x=175 , y=400)

    Btn_boss1 = Button(ventana, text='Presiona para empezar en el Primer Nivel' ,  bg='#1c1b1b',     fg='#ad1fa9', font=fuente_global, command=pantalla_boss1)
    Btn_boss1.place(x=175 , y=450)

    Btn_boss2 = Button(ventana, text='Presiona para empezar en el Segundo Nivel' ,  bg='#1c1b1b',     fg='#ad1fa9', font=fuente_global, command=pantalla_boss2)
    Btn_boss2.place(x=175 , y=500)

    Btn_boss3 = Button(ventana, text='Presiona para empezar en el Tercer Nivel' ,  bg='#1c1b1b',     fg='#ad1fa9', font=fuente_global, command=pantalla_boss3)
    Btn_boss3.place(x=175, y=550)

    Btn_ranking = Button(ventana, text='Presiona para ver el ranking de calificaciones' ,  bg='#1e034d',     fg='#ad1fa9', font=fuente_global, command=pantalla_ranking)
    Btn_ranking.place(x=150 , y=800)

    Btn_about = Button(ventana, text='Presiona para ver la información complementaria' ,  bg='#1e034d',     fg='#ad1fa9', font=fuente_global, command=pantalla_about)
    Btn_about.place(x=135 , y=850)

# Ventana Ranking =================================================================================================================================================   
def pantalla_ranking():
    global MiArchi1, nombres
    MiArchi1= open('Ranking.txt','r')
    Ranking = MiArchi1.read()
    ventana.minsize(700,933)

    C_app = Canvas(ventana, width=700 ,height = 933)
    C_app.place(x=0,y=0)
    C_app.fondo = cargar_img('fondo_tabla.jpg') 
    fondo = C_app.create_image(0,0,anchor=NW,image=C_app.fondo)

    reproducir_cancion(cargarMP3('Ranking.mp3'))

    L_intro = Label(ventana, font=(fuente_global), bg='#4b2775',     fg='#ad1fa9',     text=Ranking)
    L_intro.place(x=220, y=300)

    L_intro2 = Label(ventana, font=(fuente_global), bg='#4b2775',     fg='#ad1fa9',     text='Top 5 runs')
    L_intro2.place(x=300, y=150)

    L_nombres = Label(ventana, font=(fuente_global), bg='#4b2775',     fg='#ad1fa9',     text=nombres)
    L_nombres.place(x=300, y=  300)

    Btn_ranking = Button(ventana, text='Presiona para volver a la pantalla principal' , font=fuente_global, command=pantalla_principal)
    Btn_ranking.place(x=150 , y=800)
    MiArchi1.close()    

# Ventana about ===================================================================================================================================================   
def pantalla_about():
    C_app = Canvas(ventana, width=700 ,height = 933)
    C_app.place(x=0,y=0)
    C_app.fondo = cargar_img('fondo_about.png') 
    fondo = C_app.create_image(0,0,anchor=NW,image=C_app.fondo)

    reproducir_cancion(cargarMP3('about.mp3'))

    L_intro = Label(ventana, font=(fuente_global), bg='#5e4b34',     fg='#91bf4d',     text=about)
    L_intro.place(x=150, y=150)

    Btn_ranking = Button(ventana, text='Presiona para volver a la pantalla principal' , font=fuente_global, command=pantalla_principal)
    Btn_ranking.place(x=150 , y=800)

# Ventana Resultados ==============================================================================================================================================
def pantalla_resultados():
    global vida_boss1, vida_boss2, vida_boss3, vida_jugador, nombre_usuario
    vida_jugador = 50
    vida_boss1 = 30
    vida_boss2 = 40
    vida_boss3 = 50
    ventana.minsize(500,666)

    C_app = Canvas(ventana, width=700 ,height = 933)
    C_app.place(x=0,y=0)
    C_app.fondo = cargar_img('fondo_about.png') 
    fondo = C_app.create_image(0,0,anchor=NW,image=C_app.fondo)
    cont(0, [], 0)

    reproducir_cancion(cargarMP3('resultados.mp3'))

    if puntaje_final == 'No quedaste en el top 5 scores':
        Label(ventana, text = puntaje_final, font=fuente_global, bg='#5e4b34',     fg='#91bf4d').place(x=100, y=150)
        Label2 = Label(ventana, text = 'Obtuviste: '+ str(puntaje) + ' puntos', font=fuente_global, bg='#5e4b34',     fg='#91bf4d').place(x=100, y=100)
    else:
        Label(ventana, text = puntaje_final + ' con: ' + str(puntaje) + ' puntos!', font=fuente_global, bg='#5e4b34',     fg='#91bf4d').place(x=100, y=150)

    Btn_ranking = Button(ventana, text='Presiona para volver a la pantalla principal' , font=fuente_global, command=pantalla_principal)
    Btn_ranking.place(x=75 , y=400)


#Pantalla donde se registra el nombre ==============================================================================================================================
C_app = Canvas(ventana, width=700 ,height = 933)
C_app.place(x=0,y=0)
C_app.fondo = cargar_img('fondo_principal.png') 
fondo = C_app.create_image(0,0,anchor=NW,image=C_app.fondo)

E_nombre = Entry(ventana, width= 20, font=fuente_global)
E_nombre.place(x=400,y=300)

L_intro = Label(ventana, font=(fuente_global), bg='#4b2775',     fg='#ad1fa9',     text=intro)
L_intro.place(x=250, y=150)

L_jugador = Label(ventana, font=(fuente_global), bg='#4b2775',     fg='#ad1fa9',     text='Ingresa tu nombre para continuar: ')
L_jugador.place(x=50, y=300)

def pantalla():
    global E_nombre, nombre_usuario
    nombre_usuario = E_nombre.get()
    if(nombre_usuario != ''):
        return pantalla_principal()

Btn_new_game = Button(ventana, text='Presiona para continuar' ,  bg='#1c1b1b',     fg='#ad1fa9', font=fuente_global, command=pantalla)
Btn_new_game.place(x=175 , y=400)


ventana.protocol('WM_DELETE_WINDOW', close)    
ventana.mainloop()
