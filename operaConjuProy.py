def unionConj(conjuA, conjuB):
	print(f'La union del conjunto {conjuA} y {conjuB} resulta en: {conjuA.union(conjuB)}')

def interseccionConj(conjuA, conjuB):
	print(f'La interseccion del conjunto {conjuA} y {conjuB} resulta en: {conjuA.intersection(conjuB)}')

def diferConj(conjuA, conjuB):
	print(f'La diferencia del conjunto {conjuA} y {conjuB} resulta en: {conjuA.difference(conjuB)}')

def difSimCon(conjuA, conjuB):
	print(f'La diferencia simetrica del conjunto {conjuA} y {conjuB} resulta en: {conjuA.symmetric_difference(conjuB)}')

def esMayorCon(conjuA, conjuB):
	if conjuA.issuperset(conjuB):
		print(f'El conjunto {conjuA} contiene al conjunto {conjuB}')
	else:
		print(f'El conjunto {conjuA} no contiene al conjunto {conjuB}')
	
def esMenorCon(conjuA, conjuB):
	if conjuA.issubset(conjuB):
		print(f'El conjunto {conjuA} esta contenido en el conjunto {conjuB}')
	else:
		print(f'El conjunto {conjuA} no esta contenido en el conjunto {conjuB}')
	