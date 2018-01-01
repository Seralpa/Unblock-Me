# -*- coding: utf-8 -*-
#Sergio Alonso
#Helio Fernandez Abad
'''
@author: sergalo
@author: helfern
'''
from metodos import *
try:
    fniveles=open("niveles.txt","r")
    numniveles=int(fniveles.readline())
    fniveles.close()
except(IOError):
    print("No se encontro el fichero de niveles")
    raise 
puntuaciones=generarPuntuaciones(numniveles)
iniciarPuntuaciones(puntuaciones)
while True:
    eleccion=menuInicial()
    if(eleccion==1):
        nivel=selectorNivel(puntuaciones)
        infoNivel=cargarNivel(nivel)
        pasos=jugar(infoNivel)
        actualizar(puntuaciones,nivel,pasos)
        menuFinalPartida(nivel,puntuaciones,pasos)
    elif(eleccion==2):
        s=raw_input("Esta seguro de que desea borrar las puntuaciones?\n[S/N]_").upper()
        if s=="S":
            puntuaciones=generarPuntuaciones(numniveles)
            print("puntuaciones borradas")
    else: 
        guardarPuntuaciones(puntuaciones)
        break
    
    
      
        