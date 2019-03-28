# -*- coding: utf-8 -*-

#AUTORES:
#BENITEZ BARROSO BRANDON RAUL
#MARTINEZ NAREDO NOE


#DESCRIPCION:
#PROGRAMA GENERADOR PSEUDOALEATORIO DE NUMEROS X POR EL ALGORITMO BLUM BLUM SHUB

#BIBLIOTECAS:
# import numpy
# import math
# import numbers
# import string
# from sympy import *
# import importlib

# #SE DEFINE EL ALFABETO Y SU LONGITUD
# mayus = list((string.ascii_uppercase).replace("NO","NÑO"))
# minus = list((string.ascii_lowercase).replace("no","nño"))
# alfa = []
# for x,y in zip(mayus,minus):
# 	alfa.append(x + y)
# alfa = list(''.join(alfa) + string.digits)
# #print(alfa)
# tamano_alfa = len(alfa)
# #print(tamano_alfa)

def parity(cadena):
	arr = list(cadena)
	conteo = 0
	paridad = 0
	for i in arr:
		if(i == '1'):
			conteo += 1
	if (conteo % 2 == 0):
		return 1
	else:
		return 0

seed = 100
pq = 133

x = []
x.append(seed)

for i in range(1 ,pq):
	x.append( ( x[i - 1] ** 2 ) % pq )

print(x)

binary = []
for j in range(1, 6):
	binary.append(str(bin(x[j])).replace("0b",""))

for g in binary:
	print(g)

less_signifcant_bit = []
for k in range( 0 , 5 ):
	less_signifcant_bit.append((binary[k])[-1])

parity_bit = []
for h in range( 0 , 5 ):
	parity_bit.append(str(parity(binary[h])))

print(''.join(less_signifcant_bit))

print(''.join(parity_bit))

