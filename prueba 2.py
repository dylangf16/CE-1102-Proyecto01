lista = []
lista_nombres_completados = []
posicion = 1
puntaje = 600
entry = 'JDMaster03'
puntaje_final = ''


def cont(conteo, lista, seek):
    global posicion
    MiArchi1= open('Ranking.txt', 'r')
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
        #nombres[nueva_posicion] = nombre_usuario + '\n'
        return quick_sort(lista_completa)


#Ordenar de menor a mayor la lista -------------------------------------
def quick_sort(Lista):
    Menores = []
    Iguales = []
    Mayores = []
    if len(Lista) <= 1:
        return Lista
    Pivote = Lista[-1]
    partir(Lista,0,len(Lista),Pivote,Menores,Iguales,Mayores)
    Ret=quick_sort(Menores)
    Ret.extend(Iguales)
    Ret.extend(quick_sort(Mayores))
    return Ret

def partir(Lista,i,n,Pivote,Menores,Iguales,Mayores):
    if i == n:
        lista = Menores + Iguales + Mayores
        return aux_invierta(lista,[])
    if Lista[i] < Pivote:
        Menores.append(Lista[i])
    elif Lista[i] > Pivote:
        Mayores.append(Lista[i])
    elif Lista[i] == Pivote:
        Iguales.append(Lista[i])
    return partir(Lista,i+1,n,Pivote,Menores,Iguales,Mayores)




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
        return print('Se terminó el programa')
    else:
        MiArchi1.seek(seek)
        num = lista[0]
        num = str(num) + '\n'
        MiArchi1.write(num)
        seek += 5
        return nueva_lista(lista[1:],0,seek)



    '''
with open('Ranking.txt', 'r') as f:
    size_to_read = 4
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)'''


        
