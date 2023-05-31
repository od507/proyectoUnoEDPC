from menusProyectos import *
from operaConjuProy import *
from pantallaEspera import *

opc = True
cantConjuntos = 0
while(opc):
	menuPrincipal()
	try:
		elec = int(input("Digite su accion a realizar: "))
	except:
		elec = 1
		print("Introdujo una eleccion no valida")
		print("Seleccionamos crear un conjunto por defecto para usted")
		pausa()
	pantLimp()
	if elec == 1:
		variables = {} # Creacion de diccionario para manejar la creacion de variables
		try:
			cant = int(input("Digite la cantidad de conjuntos a crear: "))
		except:
			cant = 2
			print("No introdujo un numero")
			print("Seleccionamos 2 por defecto")

		cantConjuntos = cant

		for ele in range(cant): 
			#La llave de los diccionarios seran numeros enteros y los valores que albergaran son
			#los conjuntos vacios, los cuales procedemos a llenar de inmediato
			variables[ele] =set()
			elementos = int(input(f'Digite la cantidad de elementos a ingresar en el conjunto numero {ele+1}: '))
			for art in range(elementos):
				variables[ele].add(input("Ingrese el elemento deseado: "))
	elif elec == 2:
		contOpConj = True
		if cantConjuntos >1:
			
			while(contOpConj):
				menuOpConj()
				opConjunto = int(input("Introduzca su seleccion: "))
				pantLimp()
				if opConjunto == 1:
					primerConjunto = int(input("Digite el primer conjunto a seleccionar: "))
					segundoConjunto = int(input("Digite el segundo conjunto a seleccionar: "))
					unionConj(variables[primerConjunto-1],variables[segundoConjunto-1])
					pausa()

				elif opConjunto == 2:
					primerConjunto = int(input("Digite el primer conjunto a seleccionar: "))
					segundoConjunto = int(input("Digite el segundo conjunto a seleccionar: "))
					interseccionConj(variables[primerConjunto-1],variables[segundoConjunto-1])
					pausa()

				elif opConjunto == 3:
					primerConjunto = int(input("Digite el primer conjunto a seleccionar: "))
					segundoConjunto = int(input("Digite el segundo conjunto a seleccionar: "))
					diferConj(variables[primerConjunto-1],variables[segundoConjunto-1])
					pausa()

				elif opConjunto == 4:
					primerConjunto = int(input("Digite el primer conjunto a seleccionar: "))
					segundoConjunto = int(input("Digite el segundo conjunto a seleccionar: "))
					difSimCon(variables[primerConjunto-1],variables[segundoConjunto-1])
					pausa()
				
				elif opConjunto == 5:
					primerConjunto = int(input("Digite el primer conjunto a seleccionar: "))
					segundoConjunto = int(input("Digite el segundo conjunto a seleccionar: "))
					esMayorCon(variables[primerConjunto-1],variables[segundoConjunto-1])
					pausa()

				elif opConjunto == 6:
					primerConjunto = int(input("Digite el primer conjunto a seleccionar: "))
					segundoConjunto = int(input("Digite el segundo conjunto a seleccionar: "))
					esMenorCon(variables[primerConjunto-1],variables[segundoConjunto-1])
					pausa()

				elif opConjunto == 7:
					contOpConj = False
				else:
					continue
		else:
			print("Necesitas tener dos consjuntos como minimo para realizar operaciones")
			pausa()
			continue	

	elif elec == 3:
		#Agregamos la funcionalidad de imprimir los conjuntos todos juntos o de manera separada
		if cantConjuntos >= 1:
			menuImpr()
			impr = input("Digite la opcion seleccionada: ")
			pantLimp()

			if impr == "A" or impr == "a":
				for item in variables:
					print(variables[item])
				pausa()
			#Imprime todos los elementos de todos los conjuntos creados
			elif impr == "B" or impr == "b":
				print(f'Usted ha creado un total de {cant} conjuntos')
				conjun = int(input("Digite el numero del conjunto que desea imprimir: "))
				try:
					print(variables[conjun-1]) #evitamos que el programa se detenga
					pausa()
				except:
					print("No spuede imprimir un conjunto que no ha sido creado")
			else:
				print("No eligio una de las 2 opciones disponibles")
				print("Volvera a la pantalla principal")
		else:
			print("Necesitas 2 conjuntos como minimo para realizar operaciones")
	elif elec == 4:
		opc = False #centinela para salir del ciclo mientras
	else:
		print("No eligio una de las 4 opciones disponibles")
		print("Intente de nuevo")
	pantEsp()


		