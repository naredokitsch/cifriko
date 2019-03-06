# -*- coding: utf-8 -*-

import numpy
import math
import string

#SE DEFINE EL ALFABETO Y SU LONGITUD
alfa = list((string.ascii_uppercase).replace("NO","NÑO"))
#alfa = list((string.ascii_uppercase).replace("NO","NÑO") + string.digits)
orden = len(alfa)

#OBTIENE EL INDICE DE UNA LETRA
def get_index(letra_m_claro):
	global alfa
	i = 0
	for index in alfa:
		if (index == letra_m_claro):
			return i
		i += 1

#CONVIERTE UNA CADENA A SU CORRESPONDIENTE ARREGLO DE INDICES
def alfa_to_int(cadena):
	arreglo = []
	for letra in cadena:
		arreglo.append(get_index(letra))
	return arreglo

#ENCUENTRA EL INVERSO MULTIPLICATIVO DE UN NUMERO
# EN ARITMETICA MODULAR DE ACUERDO AL ORDEN DEL ALFABETO
def inverse(numero):
	global orden
	i = 0
	while(((numero * i) % orden) != 1 ):
		i += 1
	return i

#CIFRA UN MENSAJE USANDO EL CIFRADO AFIN.
#CONTIENE PARAMETROS POR DEFAULT
def c_afin(mensaje_claro, decimacion = 1, desplazamiento = 0, key = ""):
	global alfa
	global orden
	numeros_mensaje_claro = alfa_to_int(mensaje_claro)
	cripto = []
	if (key == ""):
		for m_claro in numeros_mensaje_claro:
			cripto.append(alfa[(((m_claro * decimacion) + desplazamiento) % orden)])
	else:
		numeros_key = alfa_to_int(key)
		i = 0
		for m_claro in numeros_mensaje_claro:
			cripto.append(alfa[(((m_claro * decimacion) + numeros_key[i % (len(numeros_key))]) % orden)])
			i += 1
	return ''.join(cripto)

#DESCIFRA UN MENSAJE USANDO EL CIFRADO AFIN.
#CONTIENE PARAMETROS POR DEFAULT
def d_afin(criptograma, decimacion = 1, desplazamiento = 0, key = ""):
	global alfa
	global orden
	numeros_criptograma = alfa_to_int(criptograma)
	mensaje_claro = []
	inv_decimacion = inverse(decimacion)
	if (key == ""):
		for cripto in numeros_criptograma:
			mensaje_claro.append(alfa[(((cripto - desplazamiento) * inv_decimacion) % orden )])
	else:
		numeros_key = alfa_to_int(key)
		i = 0
		for cripto in numeros_criptograma:
			mensaje_claro.append(alfa[(((cripto - numeros_key[i % (len(numeros_key))]) * inv_decimacion) % orden )])
			i += 1

	return ''.join(mensaje_claro)

def split(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
     arrs.append(arr)
     return arrs

def validar_key(cadena):
	root = int(math.sqrt(len(cadena)))
	matriz = split(alfa_to_int(cadena),root)
	determinante = int(round(numpy.linalg.det(matriz)))
	factor = determinante % orden
	print(factor)



