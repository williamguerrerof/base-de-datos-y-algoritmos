# -*- coding: utf-8 -*-
import csv
import codecs
import matplotlib.pyplot as plt

def CantidadDeRegistros():
	import csv
	graficar = []
	Apellido = []
	Genero = []
	fh = open('borrowers_test.csv')
	for line in fh:
		linea = line.split(',')
		apellido = linea[0]
		genero = linea[4]
		Apellido.append(apellido)
		Genero.append(genero)
	print "La cantidad de registros del genero Masculino es :",Genero.count('M')
	print "La cantidad de registros del genero Femenino es :",Genero.count('F')
	print "Cnatidad total de registros",len(Apellido)
	hombres = Genero.count('M')
	mujeres = Genero.count('F')
	graficar.append(hombres)
	graficar.append(mujeres)
	impr=['M','F']
	expl=(0,0.05,0,0)
	plt.pie(graficar,labels=impr,autopct='%1.1f%%',)
	plt.title("Cantidad de registros por genero", bbox={"facecolor":"0.8","pad":5})
	plt.legend()
	print plt.show()
def Busqueda():
	nombres = []
	apellidos = []
	fh = open('borrowers_test.csv')
	for line in fh:
		linea = line.split(',')
		nombre = linea[1]
		apellido = linea[0]
		nombres.append(nombre)
		apellidos.append(apellido)
		#print nombre,apellido
	#print nombres
	while True:
		print "Desea buscar Por nombre o apellido"
		print "A. Nombre"
		print "B. apellidos"
		try:
			opcion = str(raw_input("Ingrese su opcion :"))
		except:
			"Ingrese valor correspondiente"
		if opcion == 'A' or opcion == 'a':
			BuscarNombre= raw_input('Ingrese Nombres :')
			def LinearSearch(nombres,BuscarNombre):
				contar = 0
				for e in nombres:
					if e == BuscarNombre.lower() or e == BuscarNombre.upper():
						contar=contar+1
				print "Se repiten :",contar
			LinearSearch(nombres,BuscarNombre) 
		if opcion == 'B' or opcion == 'b':
			BuscarApellido= str(raw_input('Ingrese apellidos :'))
			def LinearSearch(apellidos,BuscarApellido):
				contar = 0
				for e in apellidos:
					if e == BuscarApellido.lower() or e == BuscarApellido.upper():
						contar=contar+1
				print "Se repiten :",contar
			LinearSearch(apellidos,BuscarApellido) 
		if opcion == 'C' or opcion == 'c':
			break
def MostrarCantidadCarreras():
	lista=[]	
	fh = open('borrowers_test.csv')
	for line in fh:
		linea = line.split(',')
		Carrera = linea[6]
		lista.append(Carrera)
		#print Carrera
	print lista
	print len(lista)
	print "La cantidad de estudiantes en la carrrera de Licenciatura en Sociología es :",lista.count('Licenciatura en Sociolog\xc3\xada\n')
	print "La cantidad de estudiantes en la carrrera de Licenciatura en Ciencias de la Educación en la Especialidad de Primero y Segundo Ciclo de Educación Básica es :",lista.count('Licenciatura en Ciencias de la Educaci\xc3\xb3n en la Especialidad de Primero y Segundo Ciclo de Educaci\xc3\xb3n B\xc3\xa1sica\n')
	print "La cantidad de estudiantes en la carrrera de Licenciatura en Anestesiología e Inhaloterapia es :",lista.count('Licenciatura en Anestesiolog\xc3\xada e Inhaloterapia\n')
	print "La cantidad de estudiantes en la carrrera de Licenciatura en Contaduria Publica es :",lista.count('Licenciatura en  Contadur\xc3\xada P\xc3\xbablica\n')
	print "La cantidad de estudiantes en la carrrera de Licenciatura en ciencias juridicas es :",lista.count('Licenciatura en Ciencias Jur\xc3\xaddicas\n')
	print "La cantidad de estudiantes en la carrrera de Licenciatura en laboratorioclinico es :",lista.count('Licenciatura en Laboratorio Cl\xc3\xadnico\n')
	print "La cantidad de estudiantes en la carrrera de Licenciatura en Lenguas Modernas Especialidad en Frances e Ingles es :",lista.count('Licenciatura en Lenguas Modernas Especialidad en Franc\xc3\xa9s e Ingl\xc3\xa9s\n')
	print "La cantidad de estudiantes en la carrrera de Licenciantura en Administracion de Empresas es :",lista.count('LICENCIATURA EN ADMINISTRACION DE EMPRESAS\n')
	print "La cantidad de estudiantes en la carrrera de Ingenieria civil es :",lista.count('INGENIERIA CIVIL\n')
	print "La cantidad de estudiantes en la carrrera de Ingenieria en Sistemas Informaticos es :",lista.count('Ingenier\xc3\xada de Sistemas Inform\xc3\xa1ticos\n')
	print "La cantidad de estudiantes en la carrrera de Ingeniería Agronómica es :",lista.count('Ingenier\xc3\xada Agron\xc3\xb3mica\n')
	print "La cantidad de estudiantes en la carrrera de Ingeniería Industrial es :",lista.count('Ingenier\xc3\xada Industrial\n')
	print "La cantidad de estudiantes en la carrrera de Arquitectura es :",lista.count('Arquitectura\n')	
	print "La cantidad de estudiantes en la carrrera de Maestría en Salud Pública es :",lista.count('Maestr\xc3\xada en Salud P\xc3\xbablica\n')
	print "\nLa cantidad de estudiantes en la carrrera de Doctorado en medicina es :",lista.count('Doctorado en Medicina\n')	
def MostrarCantidadDeErrores():
	lista = []
	lista2 = []
	listan=[]
	listaap=[]
	fh = open('borrowers_test.csv')
	for line in fh:
		linea = line.split(',')
		nombre = linea[1]
		genero = linea[4]
		lista.append(nombre)
		lista2.append(genero)
		#print nombre,apellido
	#print lista2
	print "Cantidad de errores Null es :",lista.count('NULL')
	print "Cantidad de errores Vacios es :",lista2.count('')
def AgregarRegistros():
	fh =codecs.open('borrowers_test.csv','a',encoding='utf-8')
	c1=str(raw_input('Ingrese apellido :'))
	c2=str(raw_input('Ingrese nombre :'))
	c3=str(raw_input('Ingrese codigo_categoria :'))
	c4=str(raw_input('Ingrese fecha_registro, :'))
	c5=str(raw_input('Ingrese sexo :'))
	c6=str(raw_input('Ingrese cod_carrera :'))
	c7=str(raw_input('Ingrese nombre_carrera :'))
	registro=c1+","+c2+","+c3+","+c4+","+c5+","+c6+","+c7
	fh.write(registro)
def OrdenarRegistroPorBurbuja():
	Ordenar=[]
	fh = open('borrowers_test.csv')
	for line in fh:
		linea = line.split(',')
		c1=linea[0]
		c2=linea[1]
		c3=linea[2]
		c4=linea[3]
		c5=linea[4]
		c6=linea[5]
		c7=linea[6]
		agregarlista=c1+","+c2+","+c3+","+c4+","+c5+","+c6+","+c7
		Ordenar.append(agregarlista)
	print len(Ordenar)
	#print l
	#l.remove('nombre')
	#while 'NULL' in l:
	#l.remove('NULL')
	#lista=['B', 'D', 'A', 'E', 'C','H','Z','W','D']
	def burbuja(Ordenar,tam):
		for i in range(1,tam):
			for j in range(0,tam-i):
				if(Ordenar[j] > Ordenar[j+1]):
					k = Ordenar[j+1]
					Ordenar[j+1] = Ordenar[j]
					Ordenar[j] = k;
	def imprimeLista(Ordenar,tam):
		for i in range(0,tam):
			print Ordenar[i]
	burbuja(Ordenar,len(Ordenar))
	imprimeLista(Ordenar,len(Ordenar))
def OrdenarRegistroPorQuicksort():
	Nombres = []
	Apellido=[]
	fh = codecs.open('borrowers_test.csv',encoding='utf-8')
	for line in fh:
		linea = line.split(',')
		c1=linea[0]
		c2=linea[1]
		c3=linea[2]
		c4=linea[3]
		c5=linea[4]
		c6=linea[5]
		c7=linea[6]
		agregarlistaN=c1+","+c2+","+c3+","+c4+","+c5+","+c6+","+c7
		agregarlistaA=c2+","+c1+","+c3+","+c4+","+c5+","+c6+","+c7
		Apellido.append(agregarlistaN)
		Nombres.append(agregarlistaA)
	while True:
		print "De que forma desea ordenar su registros"
		print "A. Por apellido"
		print "N. por nombre"
		print "S. salir"
		try:
			opcion = str(raw_input("Ingrese su opcion :"))
		except:
			print "Ingrese valor correspondiente"
		if opcion == "A" or opcion == "a":
			print len(Apellido)
			n=  Apellido[17200:17443]
			print len(n)
			def quicksort(n,izquierda,derecha):
				i=izquierda
				j=derecha
				x=n[(izquierda + derecha)/2]
				while( i <= j ):
					while n[i]<x and j<=derecha:
						i=i+1
					while x<n[j] and j>izquierda:
						j=j-1
					if i<=j:
						aux = n[i]; n[i] = n[j]; n[j] = aux;
						i=i+1;  j=j-1;
					if izquierda < j:
						quicksort( n, izquierda, j );
				if i < derecha:
					quicksort( n, i, derecha );
			def imprimeLista(n,tam):
				for i in range(0,tam):
					print n[i]
			quicksort(n,0,len(n)-1)
			imprimeLista(n,len(n))
		if opcion == "N" or opcion == "n":
			print len(Nombres)
			n=  Nombres[17200:17443]
			print len(n)
			def quicksort(n,izquierda,derecha):
				i=izquierda
				j=derecha
				x=n[(izquierda + derecha)/2]
				while( i <= j ):
					while n[i]<x and j<=derecha:
						i=i+1
					while x<n[j] and j>izquierda:
						j=j-1
					if i<=j:
						aux = n[i]; n[i] = n[j]; n[j] = aux;
						i=i+1;  j=j-1;
					if izquierda < j:
						quicksort( n, izquierda, j );
				if i < derecha:
					quicksort( n, i, derecha );
			def imprimeLista(n,tam):
				for i in range(0,tam):
					print n[i]
			quicksort(n,0,len(n)-1)
			imprimeLista(n,len(n))
		if opcion == "S" or opcion == "s":
			break
def OrdenarRegistroPorMeger_sort():	
	Nombre = []
	fh = codecs.open('borrowers_test.csv', encoding = 'utf-8')
	for line in fh:
		linea = line.split(',')
		c1=linea[0]
		c2=linea[1]
		c3=linea[2]
		c4=linea[3]
		c5=linea[4]
		c6=linea[5]
		c7=linea[6]
		agregarlista=c1+","+c2+","+c3+","+c4+","+c5+","+c6+","+c7
		Nombre.append(agregarlista)
		#print nombre,fruta
	#print Nombre
	print len(Nombre)
	lista = []
	def merge_sort(lista):
		if len(lista) < 2:
			return lista
		medio = len(lista) / 2
		izq = merge_sort(lista[:medio])
		der = merge_sort(lista[medio:])
		return merge(izq,der)
	def merge(lista1, lista2):
		i=0
		j=0
		resultado = []
		while i< len(lista1) and j< len(lista2):
			if lista1[i] < lista2[j]:
				resultado.append(lista1[i])
				i += 1
			else:
				resultado.append(lista2[j])
				j += 1
		resultado += lista1[i:]
		resultado += lista2[j:]	
		return resultado
	Ordenar= merge_sort(Nombre)
	for i in Ordenar:
		print i
while True:
	print "Ingrese una opcion"
	print "1. Mostrar cantidad de registros"
	print "2. Busqueda de por nombre o apellido y mostrar las coincidencias"
	print "3. Mostrar la cantidad de estudiantes agrupados por carrera"
	print "4. Mostrar cantidad de datos erroneos"
	print "5. Agregar registros al final del archivo"
	print "6. Registros por orden alfabético usando Burbuja"
	print "7. Ordene los registros por orden alfabético usando quicksort"
	print "8. Registros por orden alfabético usando Merge_sort"
	print "9. Salir"
	try:
		opcion = int(raw_input("Ingresar opcion :"))
	except:
		print "Ingrese datos correspondientes"
	if opcion == 1:
		CantidadDeRegistros()
	if opcion == 2:
		Busqueda()	
	if opcion == 3:
		MostrarCantidadCarreras()
	if opcion == 4:	
		MostrarCantidadDeErrores()
	if opcion == 5:
		AgregarRegistros()
	if opcion == 6:
		OrdenarRegistroPorBurbuja()
	if opcion == 7:
		OrdenarRegistroPorQuicksort()
	if opcion == 8:
		OrdenarRegistroPorMeger_sort()
	if opcion == 9:
		break
	
	
