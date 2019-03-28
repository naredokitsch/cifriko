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

def parity_bits(cadena):
	arr = list(cadena)
	conteo = 0
	paridad = 0
	for i in arr:
		if(i == '1'):
			conteo += 1
	if (conteo % 2 == 0):
		return str(1)
	else:
		return str(0)

def less_significant_bits(cadena):
	return str(cadena[-1])

seed = 317
pq = 151 * 199

x = []
#x.append((seed ** 2) % pq)
x.append(seed)

for i in range(1 ,pq):
	x.append( ( x[i - 1] ** 2 ) % pq )

binary = []
for j in range(1, 21):
	binary.append(str(bin(x[j])).replace("0b",""))

print("")

for g in binary:
	print(str(int(g,2)) + "\t" + g)

print("\nCLAVE CRIPTOGRAFICA")
print(''.join(list(map(less_significant_bits,binary))))
#print(''.join(list(map(parity_bits,binary))))

