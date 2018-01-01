# -*- coding: utf-8 -*-
#Sergio Alonso
#Helio Fernandez Abad
from __future__ import print_function

def selectorNivel(puntuaciones):    #Este método tiene como función preguntar al usuario cual de todos los niveles quiere jugar pidiendo que se introduzca el número del nivel. Devuelve el indicador del nivel a jugar.
    print ("Introduzca el nivel que desea jugar:") 
    i=1
    while i<=len(puntuaciones):
        if puntuaciones[i-1]==-1:print (i,".  ----")
        else: print (i,".  ",puntuaciones[i-1])
        i+=1
    nivel=int(raw_input())
    while nivel<1 or nivel>len(puntuaciones):
        nivel=int(raw_input("Opcion no existente, por favor, intentelo de nuevo: "))
    while True:
        if puntuaciones[nivel-2] != -1 or nivel==1: return nivel
        else: 
            nivel=int(raw_input("Aun no tiene acceso a este nivel.\nIntente jugar al nivel anterior."))
    return nivel

def iniciarPuntuaciones(puntuaciones):  #Este metodo se encarga de leer, si existe, el fichero de puntuaciones y pone dichas puntuaciones en la lista.
    '''PRE:si hay un fichero de puntuaciones esta correctamente escrito'''
    i=0
    try:
        f=open("puntuaciones.txt","r")
        while i<len(puntuaciones):
            linea=f.readline()
            if not linea: break
            puntuaciones[i]=int(linea)
            i+=1
        f.close()
    except(IOError):
        print ("No se encontro el archivo de puntuaciones")
    finally:return None
    
def guardarPuntuaciones(puntuaciones):  #Tiene como funcion guardar el contenido de la lista de puntuaciones en el fichero que contiene a las mismas.
    f=open("puntuaciones.txt","w")
    for i in range(len(puntuaciones)):   
        f.write(str(puntuaciones[i]))
        f.write("\n")
    f.close()
    return None

def generarPuntuaciones(numniveles):    #Este metodo se encarga de, si no hay puntuaciones previas, poner el valor de la puntuacion de cada nivel en -1, para asi indicar que el nivel no se ha completado.
    i=0
    puntuaciones=[]
    while i<numniveles:
        puntuaciones.append(-1)
        i+=1
    return puntuaciones

def actualizar(puntuaciones,nivel,pasos):   #Este es el metodo responsable de sustituir las puntuaciones almacenadas en el fichero, por las obtenidas durante la sesion de juego si y solo si, estas son puntuaciones mejores que las presentes en el fichero.
    if puntuaciones[nivel-1]==-1: puntuaciones[nivel-1]=pasos
    else:
        if puntuaciones[nivel-1]>pasos: puntuaciones[nivel-1]=pasos
    return None

def cargarNivel(nivel): #Este metodo se sirve del parametro nivel, obtenido en el selector de niveles, para devolver unicamente la informacion relativa al nivel que el usuario desea jugar.
    i,j=1,1
    infoNivel=[]
    try:
        f=open("niveles.txt","r")
        infoNivel=f.readlines()
        while i<nivel:
            j+=int(infoNivel[j])+1
            i+=1
        numcoches=int(infoNivel[j])
        infoNivel=infoNivel[j+1:j+1+numcoches]
        infoNivel=[Coche(i) for i in infoNivel]
        f.close()
    except(IOError):
        print ("No se encontro el archivo de niveles")
        raise
    finally:return infoNivel
    
def numeroLetra(indice):    #Este metodo asigna un valor numerico a cada letra.
    abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return abc[indice]

def mostrarTablero(infoNivel):  #Como su nombre indica, este metodo imprime en pantalla el tablero de juego.
    COE  = u'\u2500' # Ã¢â€�â‚¬ 
    CNS = u'\u2502' # Ã¢â€�â€š
    CES = u'\u250C' # Ã¢â€�Å’
    CSO = u'\u2510' # Ã¢â€�ï¿½
    CNE = u'\u2514' # Ã¢â€�â€�
    CON = u'\u2518' # Ã¢â€�Ëœ
    COES = u'\u252C' # Ã¢â€�Â¬
    CNES = u'\u251C' # Ã¢â€�Å“
    CONS = u'\u2524' # Ã¢â€�Â¤
    CONE = u'\u2534' # Ã¢â€�Â´
    CSOM = u'\u2593' # Ã¢â€“â€™
    #crear bordes del tablero
    tablero = [ [" "," "," "," "," ",CES, COES, COE, COE, COE, COE, COES, COE, COE, COE, COE, COES, COE, COE, COE, COE, COES, COE, COE, COE, COE, COES, COE, COE, COE, COE, COES, COE, COE, COE, COE, CSO," "," "," "," "," "] , [" "," "," "," "," ",CNES, " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", CONS," "," "," "," "," "], [" "," "," "," "," ",CNS, " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", CNS," "," "," "," "," "], [" "," "," "," "," ",CNS, " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", CNS," "," "," "," "," "], [" "," "," "," "," ",CNES, " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", CONS," "," "," "," "," "], [" "," "," "," "," ",CNS, " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", CNS," "," "," "," "," "], [" "," "," "," "," ",CNS, " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", CNS," "," "," "," "," "], [" "," "," "," "," ",CNES, " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", CSOM," "," "," "," "," "], [" "," "," "," "," ",CNS, " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", CSOM," "," "," "," "," "], [" "," "," "," "," ",CNS, " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", CSOM," "," "," "," "," "], [" "," "," "," "," ",CNES, " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", CONS," "," "," "," "," "], [" "," "," "," "," ",CNS, " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", CNS," "," "," "," "," "], [" "," "," "," "," ",CNS, " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", CNS," "," "," "," "," "], [" "," "," "," "," ",CNES, " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", CONS," "," "," "," "," "], [" "," "," "," "," ",CNS, " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", CNS," "," "," "," "," "], [" "," "," "," "," ",CNS, " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", CNS," "," "," "," "," "], [" "," "," "," "," ",CNES, " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", CONS," "," "," "," "," "], [" "," "," "," "," ",CNS, " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", CNS," "," "," "," "," "], [" "," "," "," "," ",CNS, " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", CNS," "," "," "," "," "], [" "," "," "," "," ",CNE, CONE, COE, COE, COE, COE, CONE, COE, COE, COE, COE, CONE, COE, COE, COE, COE, CONE, COE, COE, COE, COE, CONE, COE, COE, COE, COE, CONE, COE, COE, COE, COE, CON," "," "," "," "," "] ]
    #Insertar cocher en el tablero
    i=0
    while i<len(infoNivel):
        inicioX=1+5*(infoNivel[i].x-1)+5
        inicioY=1+3*(infoNivel[i].y-1)
        x=inicioX
        y=inicioY
        if infoNivel[i].orient=="H":
            tablero[y][x]=CES
            x+=1
            end=inicioX+infoNivel[i].len*5-1
            while x<end :
                tablero[y][x]=COE
                x+=1
            tablero[y][x]=CSO
            x=inicioX
            y+=1
            tablero[y][x]=CNS
            tablero[y][x+1]=numeroLetra(i)
            x=end
            tablero[y][x]=CNS
            tablero[y][x-1]=numeroLetra(i).lower()
            x=inicioX
            y+=1
            tablero[y][x]=CNE
            x+=1
            while x<end :
                tablero[y][x]=COE
                x+=1
            tablero[y][x]=CON
        else:
            tablero[y][x]=CES
            y+=1
            end=inicioY+infoNivel[i].len*3-1
            while y<end :
                tablero[y][x]=CNS
                y+=1
            tablero[y][x]=CNE
            y=inicioY
            x+=1
            tablero[y][x]=COE
            y=end
            tablero[y][x]=COE
            y=inicioY
            x+=1
            tablero[y][x]=COE
            tablero[y+1][x]=numeroLetra(i)
            y=end
            tablero[y][x]=COE
            tablero[y-1][x]=numeroLetra(i).lower()
            y=inicioY
            x+=1
            tablero[y][x]=COE
            y=end
            tablero[y][x]=COE
            y=inicioY
            x+=1
            tablero[y][x]=CSO
            y+=1
            while y<end :
                tablero[y][x]=CNS
                y+=1
            tablero[y][x]=CON
        i+=1
    i=0
    tablero[7][36]=CSOM
    tablero[9][36]=CSOM
    #imprimir tablero
    while i < len(tablero):
        j=0
        while j<len(tablero[i]):
            elemento=tablero [i][j]
            print (elemento, end="")
            j+=1
        print (" ")
        i+=1
        
def comprobarMovimiento(coche,infoNivel,direccion): #Este es el metodo encargado de comprobar si el movimiento que el usuario intenta hacer es posible o no.
    if coche.orient=="H":
        y=coche.y
        if direccion==1:
            x=coche.x+coche.len
        else: x=coche.x-1
    else:
        x=coche.x
        if direccion==1:
            y=coche.y+coche.len
        else: y=coche.y-1
    if x==7 and y==3: return True
    if x==0 or y==0 or x==7 or y==7: return False
    i=0
    while i<len(infoNivel):
        if not infoNivel[i].casillaLibre(x,y): return False
        i+=1
    return True

def obtenerDireccion(letra):    #Comprueba si la letra introducida es mayuscula o minuscula y, segun cual de las dos sea, le asigna un valor de -1 o 1 respectivamente.
    if (letra.isupper()==True):
        direccion=-1
    else:
        direccion=1
    return direccion

def obtenerIndice(letra):   #Permite selecionar el coche que se quiere mover.
    abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i=0
    while i<len(abc):
        if letra.upper()==abc[i]: return i
        i+=1
    print ("A mi eso no me parece una letra...")
    return -1 

def jugar(infoNivel):   #Este metodo es el que se encarga implementar el resto de metodos para posibilitar el jugar una partida.
    pasos=0
    while infoNivel[0].x!=6 :
        i=0
        mostrarTablero(infoNivel)
        movimientos=raw_input("Introduzca la secuencia de movimientos")
        print ("movimientos=",movimientos)
        while i<len(movimientos):
            if infoNivel[0].x==6: break
            indice=obtenerIndice(movimientos[i])
            if indice==-1 or indice>=len(infoNivel): 
                print("Movimiento",movimientos[i],"imposible")
                break
            direccion=obtenerDireccion(movimientos[i])
            if comprobarMovimiento(infoNivel[indice],infoNivel,direccion):
                infoNivel[indice].move(direccion)
                pasos+=1
            else: 
                print("Movimiento",movimientos[i],"imposible")
                break
            i+=1
    mostrarTablero(infoNivel)
    return pasos

def menuFinalPartida(nivel,puntuaciones,pasos): #Como su nombre indica, este metodo imprime en pantalla el menu que aparece al acabar la partida.
    while True:
        print ("ENHORABUENA, HA COMPLETADO EL NIVEL",nivel,"!")
        print ("Movimientos:",pasos)
        if puntuaciones[nivel-1]>pasos: print ("(NUEVO RECORD!)")
        s=raw_input("Desea pasar al siguiente nivel? [S/N]_ ").upper()
        if s=="N": break
        nivel+=1
        if nivel>20:
            print("No hay mas niveles disponibles")
            break
        infoNivel=cargarNivel(nivel)
        pasos=jugar(infoNivel)
        actualizar(puntuaciones,nivel,pasos)
    return None

def menuInicial(): #Este metodo imprime en pantalla un "menu de inicio" y devuelve la variable eleccion que luego el modulo principal usara para dirigir el flujo del prograna. 
    eleccion= int(raw_input("Bienvenido, que desea hacer?: \n1.Jugar.\n2.Borrar puntuaciones previas. \n3.Salir."))
    while eleccion<1 or 3<eleccion:
        eleccion= int(raw_input("Esa no es una opcion valida, vuelve a intentarlo."))
    return eleccion

class Coche:    #Aqui queda definida la clase coche.
    def __init__(self,info):    #Constructor de la clase Coche info es la informacion de cada coche en el formato de l fichero niveles.txt
        self.orient =info[0]
        self.x=int(info[1])
        self.y=int(info[2])
        self.len=int(info[3])
        return None
    def move(self,direccion):   #Mueve el objeto coche en lña direccion indicada
        if self.orient=="H": self.x+=direccion
        else:self.y+=direccion
        return None
    def casillaLibre(self,x,y): #compruba si alguna de las casillas ocupadas por el coche es la casilla x,y
        cx,cy=self.x,self.y
        i=0
        while i<self.len: 
            if x==cx and y==cy:return False
            if self.orient=="H":cx+=1
            else:cy+=1
            i+=1
        return True
        
        
        
        
    