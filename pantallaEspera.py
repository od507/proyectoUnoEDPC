import time
import os
import sys

'''
Importamos los modulos que nos permitiran medir el tiempoy y limpiar la pantalla
'''	

def pantEsp():
	for faltando in range(3,0,-1):
		sys.stdout.write("\r")
		sys.stdout.write("faltan {:2d} segundos para la siguiente pantalla".format(faltando))
		sys.stdout.flush()
		time.sleep(1)
	os.system('cls')

def pantLimp():
	os.system('cls')

def pausa():
	entrada = input("Click a enter para continuar")
	pantLimp()