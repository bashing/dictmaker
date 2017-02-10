#!/usr/bin/python
#Mariano Somoza
#2015
#
#Generador de diccionarios de seguridad informatica.
#Partiendo de una lista de palabras claves,como:
#-----------------------
#Nombre de empresa
#Direccion
#Nombre de tecnicos
#123
#Passw0rd
#Etcetera
#----------------------
#Se genera un diccionario de permutaciones que combina
#todas las palabras claves
#
#
#Ejemplo:
#--------------------------------------------------------
#----------- 1) Editar palabras clave -------------------
#--------------------------------------------------------
#cat lista_palabras_diccionario_password.txt 
#NombreEmpresa
#NombreEmpleado
#password
#Passw0rd
#123
#PASSW0RD
#test
#prueba
#t3st
#---------------------------------------------------------
#----------- 2) Ganerar permutatciones -------------------
#---------------------------------------------------------
#python generador_de_diccionario.py
#NombreEmpresaNombreEmpleado
#NombreEmpresapassword
#NombreEmpresaPassw0rd
#NombreEmpresa123
#NombreEmpresaPASSW0RD
#NombreEmpresatest
#NombreEmpresaprueba
#NombreEmpleadoNombreEmpresa
#NombreEmpleadopassword
#NombreEmpleadoPassw0rd
#NombreEmpleado123
#NombreEmpleadoPASSW0RD
#NombreEmpleadotest
###########################################################

import itertools
from pprint import pprint

s = [line.rstrip('\n') for line in open('lista_palabras_diccionario_password.txt')]

def generar_permutaciones(largo,dic_palabras):
	l=list(itertools.permutations(dic_palabras,largo))
	for index, item in enumerate(l):
		print ''.join(item)

generar_permutaciones(1,s)
generar_permutaciones(2,s)
generar_permutaciones(3,s)

