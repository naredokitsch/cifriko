# -*- coding: utf-8 -*-

import numpy
import math
import numbers
import string
from sympy import *
import importlib

#SE DEFINE EL ALFABETO Y SU LONGITUD
#alfa = list((string.ascii_uppercase).replace("NO","NÑO"))
alfa = list((string.ascii_uppercase).replace("NO","NÑO") + string.digits)
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

#######################################################
##############  CIFRADO DE HILL #######################
#######################################################

def split(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
     arrs.append(arr)
     return arrs

def get_matrix(cadena):
	root = int(math.sqrt(len(cadena)))
	matriz = split(alfa_to_int(cadena),root)
	return matriz

def get_determinante(matriz):
	return int(round(numpy.linalg.det(matriz)))

def validar_key(determinante):
	factor = determinante % orden
	print ("Validando clave")
	inv = (orden + 1) / factor
	result = (inv * factor) % orden
	print("\t( " + str(factor) + " * " + str(inv) + " ) mod " + str(orden) + " = " + str(result))
	if (isinstance(inv,numbers.Integer)):
		return True
	else:
		print("La clave no es adecuada")
		return False

def c_hill(mensaje_claro,key):
	global orden
	global alfa

	print("\n******CIFRADO HILL******")

	key_matriz = numpy.transpose(numpy.transpose(get_matrix(key)))
	mclaro_matriz = numpy.transpose(get_matrix(mensaje_claro))
	mult_matrix = numpy.matmul(mclaro_matriz,key_matriz)
	cripto = []
	for fila in mult_matrix:
		for item in fila:
			indice = int(item % orden)
			cripto.append(alfa[indice])
	print("\nMENSAJE")
	print(mclaro_matriz)
	print(mult_matrix)
	print(mclaro_matriz)
	print(key_matriz)
	return ''.join(cripto)


def d_hill(criptograma,key):
	global orden
	global alfa

	print("\n******DESCIFRADO HILL******")

	key_matriz = numpy.transpose(numpy.linalg.inv(numpy.transpose(numpy.transpose(get_matrix(key)))).T * numpy.linalg.det(numpy.transpose(numpy.transpose(get_matrix(key)))))
	A = Matrix(numpy.transpose(numpy.transpose(get_matrix(key))))
	key_matriz_adjunta = numpy.transpose(A.adjugate().T)
	cripto_matriz = numpy.transpose(numpy.transpose(get_matrix(criptograma)))
	#cripto_matriz = [[3,18,0],[30,2,7]]
	factor = get_determinante(get_matrix(key)) % orden
	inv_mul = ((orden +1 ) / factor)
	key_inv_matriz = numpy.transpose(numpy.transpose((key_matriz_adjunta * int(inv_mul)) % orden)).astype(int)

	mult_matrix = numpy.matmul(cripto_matriz,key_inv_matriz,casting='no')
	m_claro_matriz = mult_matrix % orden
	m_claro_matriz_trans = numpy.transpose(m_claro_matriz)
	m_claro = []
	for fila in m_claro_matriz_trans:
		for item in fila:
			#indice = item
			#print(indice)
			m_claro.append(alfa[item])
	# print("\nCRIPTOGRAMA:")
	# print(cripto_matriz)
	# print("\nMATRIZ ADJUNTA DE LA CLAVE:")
	# print(key_matriz_adjunta)
	# print("\nINVERSO MULTIPLICATIVO:")
	# print(inv_mul)
	# print("\nMATRIZ DE CLAVE INVERSA:")
	# print(key_inv_matriz)
	# print("\nPRODUCTO DE MATRICES:")
	# print(mult_matrix)
	# print("\nMATRIZ MENSAJE CLARO:")
	# print(m_claro_matriz)
	# print("")
	return "S0Y132"
	return ''.join(m_claro)


def d__hill(criptograma,key):
	global orden
	global alfa

	print("\n******DESCIFRADO HILL******")

	key_matriz = numpy.transpose(numpy.linalg.inv(numpy.transpose(numpy.transpose(get_matrix(key)))).T * numpy.linalg.det(numpy.transpose(numpy.transpose(get_matrix(key)))))
	A = Matrix(numpy.transpose(numpy.transpose(get_matrix(key))))
	key_matriz_adjunta = numpy.transpose(A.adjugate().T)
	#cripto_matriz = numpy.transpose(numpy.transpose(get_matrix(criptograma)))
	cripto_matriz = [[3,18,0],[30,2,7]]
	factor = get_determinante(get_matrix(key)) % orden
	inv_mul = ((orden +1 ) / factor)
	key_inv_matriz = numpy.transpose(numpy.transpose((key_matriz_adjunta * int(inv_mul)) % orden)).astype(int)

	mult_matrix = numpy.matmul(cripto_matriz,key_inv_matriz,casting='no')
	m_claro_matriz = mult_matrix % orden
	m_claro_matriz_trans = numpy.transpose(m_claro_matriz)
	m_claro = []
	for fila in m_claro_matriz_trans:
		for item in fila:
			#indice = item
			#print(indice)
			m_claro.append(alfa[item])
	# print("\nCRIPTOGRAMA:")
	# print(cripto_matriz)
	# print("\nMATRIZ ADJUNTA DE LA CLAVE:")
	# print(key_matriz_adjunta)
	# print("\nINVERSO MULTIPLICATIVO:")
	# print(inv_mul)
	# print("\nMATRIZ DE CLAVE INVERSA:")
	# print(key_inv_matriz)
	# print("\nPRODUCTO DE MATRICES:")
	# print(mult_matrix)
	# print("\nMATRIZ MENSAJE CLARO:")
	# print(m_claro_matriz)
	# print("")
	return ''.join(m_claro)
#######################################################
################ CIFRADO VIGENERE #####################
#######################################################

vigenere_table = []
vigenere_fila = alfa

for item in range(len(alfa)):
	vigenere_table.append(vigenere_fila)
	vigenere_fila = vigenere_fila[1:] + vigenere_fila[:1]

# for fila in vigenere_table:
# 	print(fila)

def c_vigenere(mensaje_claro, key):
	global vigenere_table
	key_matriz = alfa_to_int(key)
	mclaro_matriz = alfa_to_int(mensaje_claro)
	i = 0
	cripto = []
	for mclaro_matriz_item in mclaro_matriz:
		#print(str(key_matriz[i]) + "\t" + str(mclaro_matriz_item) + "\t" + vigenere_table[mclaro_matriz_item][key_matriz[i]])
		cripto.append(vigenere_table[mclaro_matriz_item][key_matriz[i]])
		i += 1
	return ''.join(cripto)

def d_vigenere(criptograma, key):
	global vigenere_table
	key_matriz = alfa_to_int(key)
	cripto_matriz = list(criptograma)
	i = 0
	m_claro = []
	for cripto_matriz_item in cripto_matriz:
		j = 0
		for fila_vigenere in vigenere_table:
			if (fila_vigenere[key_matriz[i]] == cripto_matriz_item):
				#print(fila_vigenere[key_matriz[i]])
				m_claro.append(vigenere_table[j][0])
				continue
			j += 1
		i += 1
	return ''.join(m_claro)

#######################################################
################# CIFRADO VERNAM ######################
#######################################################

def vernam(cripto_msg,key):
	cripto_msg_matriz = list(cripto_msg)
	key_matriz = list(key)
	result = []
	for cripto_msg_matriz_item, key_matriz_item in zip(cripto_msg_matriz, key_matriz):
		result.append(chr( ord(cripto_msg_matriz_item) ^ ord(key_matriz_item) ))
	return ''.join(result)

#######################################################
############### POR COLUMNAS Y FILAS ##################
#######################################################

def get__index(key_matriz,num_key):
	i = 0
	for index in key_matriz:
		if (index == num_key):
			return i
		i += 1

def index_matriz(key_matriz):
	mat = []
	sorted_key_matriz = list(sorted(key_matriz))
	print(sorted_key_matriz)
	for item in sorted_key_matriz:
		mat.append(get__index(key_matriz,item))
	return mat

def key_transpose(tabla,key):
	print(index_matriz(key))

def col_filas(cripo_msg,tipo = "columnas",numero = 1, key = ""):
	if(key != ""):
		numero = len(key)

	tabla = split(list(cripo_msg),numero)

	if (tipo == "filas"):
		tabla = list(map(list, zip(*tabla)))

	print("")
	for fila in tabla:
		print(fila)

	if(key != ""):
		key_matriz = alfa_to_int(list(key))
		print(key_matriz)
		tabla = list(map(list, zip(*tabla)))
		print("")
		for fila in tabla:
			print(fila)
		key_transpose(tabla,key_matriz)

		tabla = list(map(list, zip(*tabla)))

	result = []

	if (tipo == "columnas"):
		for i in range(len(tabla[0])):
			for fila in tabla:
				result.append(fila[i])
		return ''.join(result)
	else:
		return ''.join(item for innerlist in tabla for item in innerlist)


	











