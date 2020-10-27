import math
import sys, os
import ctypes #GetSystemMetrics
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PyQt5 import uic
from PyQt5.QtCore import Qt
from pygame import mixer
from PyQt5.QtGui import QIcon,QFont,QPixmap,QPalette
from PyQt5.QtCore import QCoreApplication, Qt,QBasicTimer, QTimer,QPoint
from PyQt5.QtCore import *
from PyQt5.QtGui import * 
from PyQt5 import QtGui, QtCore
import sched, time
from PyQt5 import QtWidgets
from threading import Timer
import random
from tkinter import *
import tkinter
import decimal
import tkinter
from tkinter import messagebox
import datetime
from win32com import client
import smtplib
import threading
import multiprocessing
from threading import Thread
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

ENTRADAS=0
CANTESTRELLAS=0
NOMBREUSUARIO=""
SEXOUSER=""
NOMBREPROFESOR=""
SEXOPROFESOR=""
PASSWORD=""
SEXOPROFESOR=""
CORREOPROFESOR=""
SEXOUSER=""
TEORIAMATEMATICA1=""
TEORIAMATEMATICA2=""
TEORIASUMA1=""
TEORIASUMA2=""
TEORIAmultiplicación1=""
TEORIAmultiplicación2=""
TEORIAmultiplicación3=""
PRACTICASUMATORIA=0
PRACTICAmultiplicación1=0
PRACTICAmultiplicación2=0
PRACTICAmultiplicación3=0
PRACTICACUADROMULTIPLICATIVO=0
all_processes = []


def tiempo(self):
	indicador = 0
	while indicador==100 :
		self.Time.setValue(indicador)
		indicador = indicador +1
		time.sleep(0.08)
		QApplication.processEvents()

	

def CargarDatos():
	global ENTRADAS
	global NOMBREUSUARIO
	global SEXOUSER
	global NOMBREPROFESOR
	global CANTESTRELLAS
	global SEXOPROFESOR
	global PASSWORD
	global CORREOPROFESOR
	global TEORIAMATEMATICA1
	global TEORIAMATEMATICA2	
	global TEORIASUMA1
	global TEORIASUMA2
	global PRACTICASUMATORIA
	global TEORIAmultiplicación1
	global TEORIAmultiplicación2
	global TEORIAmultiplicación3
	global PRACTICAmultiplicación1
	global PRACTICAmultiplicación2
	global PRACTICAmultiplicación3
	global PRACTICACUADROMULTIPLICATIVO


	f = open ('files/Datos.txt','r')
	read = f.readline()
	ENTRADAS =  int(read[8:len(read)-1])
	read = f.readline()
	NOMBREUSUARIO = read[11:len(read)-1]
	read = f.readline()
	SEXOUSER = read[9:len(read)-1]	
	read = f.readline()
	CANTESTRELLAS = int(read[6:len(read)-1])
	read = f.readline()
	NOMBREPROFESOR = read[16:len(read)-1]
	read = f.readline()
	SEXOPROFESOR= read[13:len(read)-1]
	read = f.readline()
	CORREOPROFESOR= read[15:len(read)-1]
	read = f.readline()
	PASSWORD = read[9:len(read)-1]
	read = f.readline()
	TEORIAMATEMATICA1 = read[17:len(read)-1]
	read = f.readline()
	TEORIAMATEMATICA2 = read[17:len(read)-1]
	read = f.readline()
	TEORIASUMA1 = read[17:len(read)-1]
	read = f.readline()
	TEORIASUMA2 = read[17:len(read)-1]
	read = f.readline()
	PRACTICASUMATORIA = int(read[18:len(read)-1])
	read = f.readline()
	TEORIAmultiplicación1 = read[22:len(read)-1]
	read = f.readline()
	TEORIAmultiplicación2 = read[22:len(read)-1]
	read = f.readline()
	TEORIAmultiplicación3 = read[22:len(read)-1]
	read = f.readline()
	PRACTICAmultiplicación1 = int(read[24:len(read)-1])
	read = f.readline()
	PRACTICAmultiplicación2 = int(read[24:len(read)-1])
	read = f.readline()
	PRACTICAmultiplicación3 = int(read[24:len(read)-1])
	read = f.readline()
	PRACTICACUADROMULTIPLICATIVO = int(read[28:len(read)-1])	



def CrearArchivi():
	file = open("files/Datos.txt", "w")
	file.write("Primera=\n" )
	file.write("NombreUser=\n")
	file.write("SexoUser=\n")
	file.write("Stars=\n")
	file.write("NombreProfesora=\n")
	file.write("SexoProfesor=\n")
	file.write("CorreoProfesor=\n")
	file.write("Password=\n")	
	file.write("teoriaMateatica1=\n")
	file.write("teoriaMateatica2=\n")	
	file.write("teoriaSumatoria1=\n")
	file.write("teoriaSumatoria2=\n")
	file.write("practicaSumatoria=\n")
	file.write("teoriamultiplicación1=\n")
	file.write("teoriamultiplicación2=\n")
	file.write("teoriamultiplicación3=\n")
	file.write("practicamultiplicación1=\n")
	file.write("practicamultiplicación2=\n")
	file.write("practicamultiplicación3=\n")
	file.write("practicaCuadroMultipicativo=\n")

	file.close()

def ModificarArchivo():
	global ENTRADAS
	global NOMBREUSUARIO
	global SEXOUSER
	global CANTESTRELLAS
	global NOMBREPROFESOR
	global SEXOPROFESOR
	global PASSWORD
	global CORREOPROFESOR
	global TEORIAMATEMATICA1
	global TEORIAMATEMATICA2	
	global TEORIASUMA1
	global TEORIASUMA2
	global PRACTICASUMATORIA
	global TEORIAmultiplicación1
	global TEORIAmultiplicación2
	global TEORIAmultiplicación3
	global PRACTICAmultiplicación1
	global PRACTICAmultiplicación2
	global PRACTICAmultiplicación3
	global PRACTICACUADROMULTIPLICATIVO
	file = open("files/Datos.txt", "w")
	file.write("Primera="+str(ENTRADAS)+"\n" )
	file.write("NombreUser="+NOMBREUSUARIO+"\n")
	file.write("SexoUser="+SEXOUSER+"\n")
	file.write("Stars="+str(CANTESTRELLAS)+"\n")
	file.write("NombreProfesora="+NOMBREPROFESOR+"\n")
	file.write("SexoProfesor="+SEXOPROFESOR+"\n")
	file.write("CorreoProfesor="+CORREOPROFESOR+"\n")
	file.write("Password="+PASSWORD+"\n")	
	file.write("teoriaMateatica1="+TEORIAMATEMATICA1+"\n")
	file.write("teoriaMateatica2="+TEORIAMATEMATICA2+"\n")	
	file.write("teoriaSumatoria1="+TEORIASUMA1+"\n")
	file.write("teoriaSumatoria2="+TEORIASUMA2+"\n")
	file.write("practicaSumatoria="+str(PRACTICASUMATORIA)+"\n")
	file.write("teoriamultiplicacion1="+TEORIAmultiplicación1+"\n")
	file.write("teoriamultiplicacion2="+TEORIAmultiplicación2+"\n")
	file.write("teoriamultiplicacion3="+TEORIAmultiplicación3+"\n")
	file.write("practicamultiplicacion1="+str(PRACTICAmultiplicación1)+"\n")
	file.write("practicamultiplicacion2="+str(PRACTICAmultiplicación2)+"\n")
	file.write("practicamultiplicacion3="+str(PRACTICAmultiplicación3)+"\n")
	file.write("practicaCuadroMultipicativo="+str(PRACTICACUADROMULTIPLICATIVO)+"\n")

	file.close()


def crearmulti1():
	file = open("files/multiplicacion1.txt", "w")

def crearmulti2():
	file = open("files/multiplicacion2.txt", "w")

def crearmulti3():
	file = open("files/multiplicacion3.txt", "w")


def modimulti1(ejercicio):
	
	file = open("files/multiplicacion1.txt", "r")
	contenido = open("files/multiplicacion11.txt", "a")
	dt = datetime.datetime.now()
	contenido.write(ejercicio+"/"+dt.strftime("%d %m %y")+"\n")
	linea = file.readline()
	while linea != "":
		contenido.write(linea)
		linea = file.readline()
	file.close()
	contenido.close()	
	os.remove("files/multiplicacion1.txt")
	os.rename("files/multiplicacion11.txt", "files/multiplicacion1.txt")


def modimulti2(ejercicio):
	file = open("files/multiplicacion2.txt", "r")
	contenido = open("files/multiplicacion22.txt", "a")
	dt = datetime.datetime.now()
	contenido.write(ejercicio+"/"+dt.strftime("%d %m %y")+"\n")
	linea = file.readline()
	while linea != "":
		contenido.write(linea)
		linea = file.readline()
	file.close()
	contenido.close()
	os.remove("files/multiplicacion2.txt")
	os.rename("files/multiplicacion22.txt", "files/multiplicacion2.txt")

def modimulti3(ejercicio):
	file = open("files/multiplicacion3.txt", "r")
	contenido = open("files/multiplicacion33.txt", "a")
	dt = datetime.datetime.now()
	contenido.write(ejercicio+"/"+dt.strftime("%d %m %y")+"\n")
	linea = file.readline()
	while linea != "":
		contenido.write(linea)
		linea = file.readline()
	file.close()
	contenido.close()	
	os.remove("files/multiplicacion3.txt")
	os.rename("files/multiplicacion33.txt", "files/multiplicacion3.txt")

def hablar(self,text):

	indice = 0
	oracion2=""
	oracion = text# colocar texto real XD
	root = tkinter.Tk()
	while indice < len(oracion):
		letra = oracion[indice]
		oracion2= oracion2 + letra
		root.withdraw()
		root.update()
		if ((len(oracion2) > 65 ) and (letra==" ")):
			self.dialogo.setText(oracion2)
			oracion2=""
			time.sleep(1)	
		else:	
			self.dialogo.setText(oracion2)	
		time.sleep(0.1)
		indice= indice+1



class buscaamigos(QMainWindow):
	def __init__(self,name =None):
		super(buscaamigos, self).__init__()
		uic.loadUi("tabladidactica.ui",self)
		lista=[]
		lista2=[]
		count=0
		self.salir.setEnabled(False)
		self.terminar.setEnabled(False)

		self.iniciar.setEnabled(False)
		self.salir.clicked.connect(self.cancelar) 
		self.terminar.clicked.connect(self.sigue)	
		self.iniciar.clicked.connect(self.Tiempo2)
		global SEXOUSER
		global NOMBREUSUARIO
		global CANTESTRELLAS

		self.totalEstrellas.setText(str(CANTESTRELLAS))
		if(SEXOUSER == "chico"):
			self.nombre.setText("Explorador: "+NOMBREUSUARIO)
		else:
			self.nombre.setText("Exploradora: "+NOMBREUSUARIO)
		while(count < 7):
			lista.insert(count, random.randint(0,9))
			lista2.insert(count, random.randint(0,9))
			count=count+1

		self.step = 0

		self.t00.setEnabled(False)
		self.t01.setEnabled(False)
		self.t02.setEnabled(False)
		self.t03.setEnabled(False)

		self.t10.setEnabled(False)
		self.t11.setEnabled(False)
		self.t12.setEnabled(False)
		self.t13.setEnabled(False)

		self.t20.setEnabled(False)
		self.t21.setEnabled(False)
		self.t22.setEnabled(False)
		self.t23.setEnabled(False)

		self.t30.setEnabled(False)
		self.t31.setEnabled(False)
		self.t32.setEnabled(False)
		self.t33.setEnabled(False)
		
		self.dato0.setText(str(lista[0]))
		self.dato1.setText(str(lista[1]))
		self.dato2.setText(str(lista[2]))
		self.dato3.setText(str(lista[3]))
		
		self.dato00.setText(str(lista2[0]))
		self.dato11.setText(str(lista2[1]))
		self.dato22.setText(str(lista2[2]))
		self.dato33.setText(str(lista2[3]))


		regex = QRegExp("[0-9_]+")
		validator = QRegExpValidator(regex)
		self.t00.setValidator(validator)
		self.t01.setValidator(validator)
		self.t02.setValidator(validator)
		self.t03.setValidator(validator)


		self.t10.setValidator(validator)
		self.t11.setValidator(validator)
		self.t12.setValidator(validator)
		self.t13.setValidator(validator)


		self.t20.setValidator(validator)
		self.t21.setValidator(validator)
		self.t22.setValidator(validator)
		self.t23.setValidator(validator)


		self.t30.setValidator(validator)
		self.t31.setValidator(validator)
		self.t32.setValidator(validator)
		self.t33.setValidator(validator)
		self.step = 900
		self.cronometro.display("%d:%02d" % (self.step/60,self.step % 60))
		self.stop = False
		self.children = []

		self.show()

		self.t2 = Timer(905, self.seacabo )
		mixer.music.load('music/cuadroaventuraabrir.mp3')
		mixer.music.play(1)
		hablar(self,"Bienvenido al cuadro de aventura, completar este cuadro de multiplicaciones te dará una cantidad de estrellas mientras más rápido lo hagas mayor será el premio")
		self.salir.setEnabled(True)
		self.terminar.setEnabled(True)
		self.iniciar.setEnabled(True)


	def seacabo(self):
		self.close()
		self = VentanaPrincipal()
		self.children.append(child)


	def Tiempo2(self):
		self.t00.setEnabled(True)
		self.t01.setEnabled(True)
		self.t02.setEnabled(True)
		self.t03.setEnabled(True)

		self.t10.setEnabled(True)
		self.t11.setEnabled(True)
		self.t12.setEnabled(True)
		self.t13.setEnabled(True)

		self.t20.setEnabled(True)
		self.t21.setEnabled(True)
		self.t22.setEnabled(True)
		self.t23.setEnabled(True)

		self.t30.setEnabled(True)
		self.t31.setEnabled(True)
		self.t32.setEnabled(True)
		self.t33.setEnabled(True)
		self.step = 900
		root = tkinter.Tk()
		self.iniciar.setEnabled(False)
		while self.step >= 0 and self.stop == False : 
			#self.QApplication.sendPostedEvents()
			self.cronometro.display("%d:%02d" % (self.step/60,self.step % 60))
			root.withdraw()
			root.update()
			time.sleep(1)
			self.step = self.step - 1
			if(self.step == 0):
				self.stop == True
				print("entro")
				self.t00.setEnabled(False)
				self.t01.setEnabled(False)
				self.t02.setEnabled(False)
				self.t03.setEnabled(False)

				self.t10.setEnabled(False)
				self.t11.setEnabled(False)
				self.t12.setEnabled(False)
				self.t13.setEnabled(False)

				self.t20.setEnabled(False)
				self.t21.setEnabled(False)
				self.t22.setEnabled(False)
				self.t23.setEnabled(False)

				self.t30.setEnabled(False)
				self.t31.setEnabled(False)
				self.t32.setEnabled(False)
				self.t33.setEnabled(False)
				mixer.music.load('music/seacabo.mp3')
				mixer.music.play(1)
				hablar(self, "se acabo el tiempo, sera la próxima ves")
				time.sleep(2)

	def sigue(self):
		bueno=True
		global CANTESTRELLAS
		if("" !=self.t00.text()):
			if ( int(self.t00.text()) != (int(self.dato0.text())*int(self.dato00.text()))):
				bueno=False
				self.t00.setStyleSheet ( "background-color: #d95030;")	
			else:
				self.t00.setStyleSheet ( "background-color: #FFFFFF;")		
		else:
			bueno=False
			self.t00.setStyleSheet ( "background-color: #d95030;" )

		if("" !=self.t10.text()):
			if ( int(self.t10.text()) != (int(self.dato0.text())*int(self.dato11.text()))):
				bueno=False
				self.t10.setStyleSheet ( "background-color: #d95030;")	
			else:
				self.t10.setStyleSheet ( "background-color: #FFFFFF;")
		else:
			bueno=False
			self.t10.setStyleSheet ( "background-color: #d95030;" )

		if("" !=self.t20.text()):
			if ( int(self.t20.text()) != (int(self.dato0.text())*int(self.dato22.text()))):
				bueno=False
				self.t20.setStyleSheet ( "background-color: #d95030;")
			else:
				self.t20.setStyleSheet ( "background-color: #FFFFFF;")	
		else:
			bueno=False
			self.t20.setStyleSheet ( "background-color: #d95030;" )

		if("" !=self.t30.text()):
			if ( int(self.t30.text()) != (int(self.dato0.text())*int(self.dato33.text()))):
				bueno=False
				self.t30.setStyleSheet ( "background-color: #d95030;")	
			else:
				self.t30.setStyleSheet ( "background-color: #FFFFFF;")
		else:
			bueno=False 
			self.t30.setStyleSheet ( "background-color: #d95030;" )



		#############################################	

		if (""!=self.t01.text()):
			if ( int(self.t01.text()) != (int(self.dato1.text())*int(self.dato00.text()))):
				bueno=False
				self.t01.setStyleSheet ( "background-color: #d95030;" )	
			else:
				self.t01.setStyleSheet ( "background-color: #FFFFFF;")
		else: 
			bueno=False
			self.t01.setStyleSheet ( "background-color: #d95030;" )	
		
		if (""!=self.t11.text()):
			if ( int(self.t11.text()) != (int(self.dato1.text())*int(self.dato11.text()))):
				bueno=False
				self.t11.setStyleSheet ( "background-color: #d95030;" )	
			else:
				self.t11.setStyleSheet ( "background-color: #FFFFFF;")	
		else:
			bueno=False
			self.t11.setStyleSheet ( "background-color: #d95030;" )	
		
		if (""!=self.t21.text()):
			if ( int(self.t21.text()) != (int(self.dato1.text())*int(self.dato22.text()))):
				bueno=False
				self.t21.setStyleSheet ( "background-color: #d95030;" )	
			else:
				self.t21.setStyleSheet ( "background-color: #FFFFFF;")	
		else:
			bueno=False
			self.t21.setStyleSheet ( "background-color: #d95030;" )
		
		if (""!=self.t31.text()):
			if ( int(self.t31.text()) != (int(self.dato1.text())*int(self.dato33.text()))):
				bueno=False
				self.t31.setStyleSheet ( "background-color: #d95030;" )	
			else:
				self.t31.setStyleSheet ( "background-color: #FFFFFF;")
		else:
			bueno=False
			self.t31.setStyleSheet ( "background-color: #d95030;" )	
		

		
		##############################################
		if("" != self.t02.text()):
			if ( int(self.t02.text()) != (int(self.dato2.text())*int(self.dato00.text()))):
				bueno=False
				self.t02.setStyleSheet ( "background-color: #d95030;" )	
			else:
				self.t02.setStyleSheet ( "background-color: #FFFFFF;")	
		else:
			bueno=False 
			self.t02.setStyleSheet ( "background-color: #d95030;" )

		if("" != self.t12.text()):
			if ( int(self.t12.text()) != (int(self.dato2.text())*int(self.dato11.text()))):
				bueno=False
				self.t12.setStyleSheet ( "background-color: #d95030;" )		
			else:
				self.t12.setStyleSheet ( "background-color: #FFFFFF;")	
		else: 
			bueno=False
			self.t12.setStyleSheet ( "background-color: #d95030;" )

		if("" != self.t22.text()):
			if ( int(self.t22.text()) != (int(self.dato2.text())*int(self.dato22.text()))):
				bueno=False
				self.t22.setStyleSheet ( "background-color: #d95030;" )	
			else:
				self.t22.setStyleSheet ( "background-color: #FFFFFF;")	
		else: 
			bueno=False
			self.t22.setStyleSheet ( "background-color: #d95030;" )

		if("" != self.t32.text()):
			if ( int(self.t32.text()) != (int(self.dato2.text())*int(self.dato33.text()))):
				bueno=False
				self.t32.setStyleSheet ( "background-color: #d95030;" )	
			else:
				self.t32.setStyleSheet ( "background-color: #FFFFFF;")	
		else: 
			bueno=False
			self.t32.setStyleSheet ( "background-color: #d95030;" )


		
		#############################################

		if("" != self.t03.text()):
			if ( int(self.t03.text()) != (int(self.dato3.text())*int(self.dato00.text()))):
				bueno=False
				self.t03.setStyleSheet ( "background-color: #d95030;" )
			else:
				self.t03.setStyleSheet ( "background-color: #FFFFFF;")		
		else: 
			bueno=False
			self.t03.setStyleSheet ( "background-color: #d95030;" )
		
		if("" != self.t13.text()):
			if ( int(self.t13.text()) != (int(self.dato3.text())*int(self.dato11.text()))):
				bueno=False
				self.t13.setStyleSheet ( "background-color: #d95030;" )	
			else:
				self.t13.setStyleSheet ( "background-color: #FFFFFF;")	
		else: 
			bueno=False
			self.t13.setStyleSheet ( "background-color: #d95030;" )
		
		if("" != self.t23.text()):		
			if ( int(self.t23.text()) != (int(self.dato3.text())*int(self.dato22.text()))):
				bueno=False 
				self.t23.setStyleSheet ( "background-color: #d95030;" )	
			else:
				self.t23.setStyleSheet ( "background-color: #FFFFFF;")	
		else: 
			bueno=False
			self.t23.setStyleSheet ( "background-color: #d95030;" )
		
		if("" != self.t33.text()):		
			if ( int(self.t33.text()) != (int(self.dato3.text())*int(self.dato33.text()))):
				bueno=False
				self.t33.setStyleSheet ( "background-color: #d95030;" )	
			else:
				self.t33.setStyleSheet ( "background-color: #FFFFFF;")		
		else: 
			bueno=False
			self.t33.setStyleSheet ( "background-color: #d95030;" )
		


		#############################################

		if(bueno==True):
			agregar=0
			if self.step >= 600 :
				CANTESTRELLAS=CANTESTRELLAS+20
				agregar =20
			else:	
				if self.step >= 300:
					CANTESTRELLAS=CANTESTRELLAS+15
					agregar =15
				else:
					CANTESTRELLAS=CANTESTRELLAS+10
					agregar =10
			ModificarArchivo()	
			hablar(self,"Muy bien lo conseguiste, completaste el cuadro, y conseguiste "+str(agregar)+" de mis amigos intentemos conseguir mas luego")
			time.sleep(3)
			print("bueno")
			self.close()
			child=VentanaPrincipal()	
			self.children.append(child)
		else:
			hablar(self,"Los cuadros en color rojo no concuerdan con la solucion o estan vacios revisalos")	

	def cancelar(self):	
		self.close()
		child=VentanaPrincipal()	
		self.children.append(child)	
"""
	def ayuda(self):

		if ( int(self.t00.text()) != (int(self.dato0.text())*int(self.dato00.text()))):
			self.t00.setStyleSheet ( "background-color: #d95030;" ) #colocar en rojo

		if ( int(self.t01.text()) != (int(self.dato1.text())*int(self.dato00.text()))):
			self.t01.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo
		
		if ( int(self.t02.text()) != (int(self.dato2.text())*int(self.dato00.text()))):
			self.t02.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo
		
		if ( int(self.t03.text()) != (int(self.dato3.text())*int(self.dato00.text()))):
			self.t03.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo
		
		if ( int(self.t04.text()) != (int(self.dato4.text())*int(self.dato00.text()))):
			self.t04.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo
		
		if ( int(self.t05.text()) != (int(self.dato5.text())*int(self.dato00.text()))):
			self.t05.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo
		


		#############################################	
		
		if ( int(self.t10.text()) != (int(self.dato0.text())*int(self.dato11.text()))):
			self.t10.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo

		if ( int(self.t11.text()) != (int(self.dato1.text())*int(self.dato11.text()))):
			self.t11.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo
		
		if ( int(self.t12.text()) != (int(self.dato2.text())*int(self.dato11.text()))):
			self.t12.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo
		
		if ( int(self.t13.text()) != (int(self.dato3.text())*int(self.dato11.text()))):
			self.t13.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo
		
		if ( int(self.t14.text()) != (int(self.dato4.text())*int(self.dato11.text()))):
			self.t14.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo
		
		if ( int(self.t15.text()) != (int(self.dato5.text())*int(self.dato11.text()))):
			self.t15.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo
		

		
		##############################################

		if ( int(self.t20.text()) != (int(self.dato0.text())*int(self.dato22.text()))):
			self.t20.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo

		if ( int(self.t21.text()) != (int(self.dato1.text())*int(self.dato22.text()))):
			self.t21.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo
		
		if ( int(self.t22.text()) != (int(self.dato2.text())*int(self.dato22.text()))):
			self.t22.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo
		
		if ( int(self.t23.text()) != (int(self.dato3.text())*int(self.dato22.text()))):
			self.t23.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo
		
		if ( int(self.t24.text()) != (int(self.dato4.text())*int(self.dato22.text()))):
			self.t24.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo
		
		if ( int(self.t25.text()) != (int(self.dato5.text())*int(self.dato22.text()))):
			self.t25.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo
		

		
		#############################################


		if ( int(self.t30.text()) != (int(self.dato0.text())*int(self.dato33.text()))):
			self.t30.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo

		if ( int(self.t31.text()) != (int(self.dato1.text())*int(self.dato33.text()))):
			self.t31.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo
		
		if ( int(self.t32.text()) != (int(self.dato2.text())*int(self.dato33.text()))):
			self.t32.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo
		
		if ( int(self.t33.text()) != (int(self.dato3.text())*int(self.dato33.text()))):
			self.t33.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo
		
		if ( int(self.t34.text()) != (int(self.dato4.text())*int(self.dato33.text()))):
			self.t34.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo
		
		if ( int(self.t35.text()) != (int(self.dato5.text())*int(self.dato33.text()))):
			self.t35.setStyleSheet ( "background-color: #d95030;" )#colocar en rojo
	"""	


class amigosm1(QMainWindow):
	def __init__(self,intento,nivel):
		super(amigosm1, self).__init__()
		uic.loadUi("amigosMultiples.ui",self)

		self.children = []
		print(str(intento))
		self.intentos.setText(str(intento))
		self.salir.clicked.connect(self.cancelar) 
		self.siguiente.clicked.connect(self.Siguiente)	
		self.numero1.setText(str(random.randint(0,9)))#random de 2 digito
		self.numero2.setText(str(random.randint(0,9)))#random de 2 digito	
		self.labelnivel.setText(str(nivel))	#crear este label
		self.movie = QMovie("images/shakehabla.gif", QByteArray(), self)
		self.movie.setCacheMode(QMovie.CacheAll) 
		self.movie.setSpeed(100)
		self.shake.setMovie(self.movie)
		self.movie.start()
		regex = QRegExp("[0-9_]+")
		validator = QRegExpValidator(regex)
		self.resultado.setValidator(validator)
		self.show()
		global SEXOUSER
		global NOMBREUSUARIO
		global CANTESTRELLAS
		self.totalEstrellas.setText(str(CANTESTRELLAS))
		if(SEXOUSER == "chico"):
			self.nombre.setText("Explorador: "+NOMBREUSUARIO)
		else:
			self.nombre.setText("Exploradora: "+NOMBREUSUARIO)
		if nivel==10 :
			hablar(self,"Estamos en el último nivel sé que puedes lograrlo y obtener el máximo de amigos posible!")
		else:
			hablar(self,"Estamos en el nivel "+str(nivel)+" sé que puedes llegar al último y obtener el máximo de amigos posible!")
		self.movie.stop()


	def Siguiente(self):

		global CANTESTRELLAS 
		res=int(self.resultado.text())
		num1=int(self.numero1.text())
		num2 =int(self.numero2.text())
		if(int (self.labelnivel.text()) != 10):
			if(res==(num1*num2)):
				mixer.music.load('music/originalcelebracionkarina.mp3')
				mixer.music.play(1)
				hablar(self," Sí, así se hace. Ahora pasemos al siguiente cuadrante")
				ints=int(self.intentos.text())
				modimulti1(str(num1)+" X "+str(num2))
				print(str(ints))
				time.sleep(2)
				child = amigosm1(ints,int(self.labelnivel.text())+1)
				self.close()
				self.children.append(child)
					
			else:
				intentos = int(self.intentos.text())
				intentos = intentos - 1
				self.intentos.setText(str(intentos))
				if intentos == 0 :
					mixer.music.load('music/seralaproximavesPerder.mp3')
					mixer.music.play(1)						
					hablar(self,"Se terminaron los intentos. Aun así tu esfuerzo por llegar hasta aquí, nos ayudo a encontrar "+str(int (self.labelnivel.text())-1)+" de mis amigos")
					CANTESTRELLAS = CANTESTRELLAS + int (self.labelnivel.text())-1
					ModificarArchivo()
					child = menu2(self)
					self.close()
					self.children.append(child)
				else:
					mixer.music.load('music/auntequedanintentos.mp3')
					mixer.music.play(1)	
					hablar(self,"Será al próximo intento no te rindas yo sé que puedes lograrlo")		
		else: 
			if(res==(num1*num2)):
				#mixer.music.load('music/llegaral10.mp3')
				#mixer.music.play(1)
				hablar(self," Sí, así se hace. Sabia que podías lograrlo, llegaste al nivel 10 y lo superaste")
				time.sleep(1)
				hablar(self," Este logro nos ayuda a obtener 10 amigos extra")
				CANTESTRELLAS = CANTESTRELLAS + int (self.labelnivel.text()) +10
				ModificarArchivo()
				modimulti1(str(num1)+" X "+str(num2))
				child = menu2(self)
				self.close()
				self.children.append(child)
			else:
				intentos = int(self.intentos.text())
				intentos = intentos - 1
				if intentos == 0 :
					mixer.music.load('music/seralaproximavesPerder.mp3')
					mixer.music.play(1)	
					hablar(self,"Se terminaron los intento. Aun así tu esfuerzo por llegar hasta aquí, nos ayudo a encontrar "+str(int (self.labelnivel.text())-1)+" de mis amigos")
					CANTESTRELLAS = CANTESTRELLAS + int (self.labelnivel.text())-1
					ModificarArchivo()
					self.close()
					child=VentanaPrincipal()	
					self.children.append(child)
				else:
					mixer.music.load('music/auntequedanintentos.mp3')
					mixer.music.play(1)	
					hablar(self,"Será al próximo intento no te rindas yo se que puedes lograrlo")
					self.intentos.setText(str(intentos))


	def cancelar(self):	
		global CANTESTRELLAS 
		if(int (self.labelnivel.text()) == 1):
			child = menu2(self)
			self.close()
			self.children.append(child)
		else:
			mixer.music.load('music/seralaproximavesPerder.mp3')
			mixer.music.play(1)				
			hablar(self,"Aun así tu esfuerzo por llegar hasta aquí, nos ayudo a encontrar "+str(int (self.labelnivel.text())-1)+" de mis amigos")
			CANTESTRELLAS = CANTESTRELLAS + int (self.labelnivel.text())-1
			ModificarArchivo()
			child = menu2(self)
			self.close()
			self.children.append(child)

class amigosm2(QMainWindow):
	def __init__(self,intento,nivel):
		super(amigosm2, self).__init__()
		uic.loadUi("amigosMultiplesIntermedio.ui",self)
		self.children = []
		self.intentos.setText(str(intento))
		self.salir.clicked.connect(self.cancelar) 
		self.siguiente.clicked.connect(self.Siguiente)	
		self.numero1.setText(str(random.randint(100,999)))#random de 2 digito
		self.numero2.setText(str(random.randint(1,9)))#random de 2 digito
		self.labelnivel.setText(str(nivel))	#crear este label
		self.movie = QMovie("images/shakehabla.gif", QByteArray(), self)
		regex = QRegExp("[0-9_]+")
		validator = QRegExpValidator(regex)
		self.resultado.setValidator(validator)
		self.movie.setCacheMode(QMovie.CacheAll) 
		self.movie.setSpeed(100)
		self.shake.setMovie(self.movie)
		self.movie.start()
		global SEXOUSER
		global NOMBREUSUARIO
		global CANTESTRELLAS
		self.totalEstrellas.setText(str(CANTESTRELLAS))
		if(SEXOUSER == "chico"):
			self.nombre.setText("Explorador: "+NOMBREUSUARIO)
		else:
			self.nombre.setText("Exploradora: "+NOMBREUSUARIO)
		self.show()
		if nivel==10 :
			hablar(self,"Estamos en el último nivel sé que puedes lograrlo y obtener el máximo de amigos posible!")
		else:
			hablar(self,"Estamos en el nivel "+str(nivel)+" sé que puedes llegar al último y obtener el máximo de amigos posible!")


	def Siguiente(self):
		global CANTESTRELLAS 
		res=int(self.resultado.text())
		num1=int(self.numero1.text())
		num2 =int(self.numero2.text())
		if(int (self.labelnivel.text()) != 10):
			if(res==(num1*num2)):
				mixer.music.load('music/originalcelebracionkarina.mp3')
				mixer.music.play(1)
				hablar(self," Siii, así se hace, sabia que podías lograrlo sigamos al siguiente cuadrante ")
				ints=int(self.intentos.text())
				modimulti2(str(num1)+" X "+str(num2))
				print(str(ints))
				time.sleep(6)
				child = amigosm2(ints,int(self.labelnivel.text())+1)
				self.close()
				self.children.append(child)
					
			else:
				intentos = int(self.intentos.text())
				intentos = intentos - 1
				self.intentos.setText(str(intentos))
				if intentos == 0 :
					mixer.music.load('music/seralaproximavesPerder.mp3')
					mixer.music.play(1)	
					hablar(self,"Se terminaron los intentos, intentemoslo desde el inicio de nuevo ")
					time.sleep(2)
					hablar(self,"Aun así tu esfuerzo por llegar hasta aquí, nos ayudo a encontrar "+str(int (self.labelnivel.text())-1)+" de mis amigos ")
					CANTESTRELLAS = CANTESTRELLAS + int (self.labelnivel.text())-1
					ModificarArchivo()
					child = menu2(self)
					self.close()
					self.children.append(child)
				else:
					mixer.music.load('music/auntequedanintentos.mp3')
					mixer.music.play(1)	
					hablar(self,"Será al próximo intento no te rindas yo se que puedes lograrlo ")
					self.intentos.setText(str(intentos))
		else: 
			if(res==(num1*num2)):
				#mixer.music.load('music/llegaral10.mp3')
				#mixer.music.play(1)
				hablar(self," Sí, así se hace. Sabia que podías lograrlo, llegaste al nivel 10 y lo superaste ")
				hablar(self," Este logro nos ayuda a obtener 20 amigos extra ")
				CANTESTRELLAS = CANTESTRELLAS + int (self.labelnivel.text()) +20
				modimulti2(str(num1)+" X "+str(num2))
				ModificarArchivo()
				child = menu2(self)
				self.close()
				self.children.append(child)
			else:
				intentos = int(self.intentos.text())
				intentos = intentos - 1
				if intentos == 0 :
					mixer.music.load('music/seralaproximavesPerder.mp3')
					mixer.music.play(1)					
					hablar(self,"Se terminaron los intentos, intentemoslo desde el inicio de nuevo ")
					time.sleep(2)
					hablar(self,"Aun así tu esfuerzo por llegar hasta aquí, nos ayudo a encontrar "+str(int(self.labelnivel.text())-1)+" de mis amigos ")
					CANTESTRELLAS = CANTESTRELLAS + int (self.labelnivel.text())-1
					ModificarArchivo()
					child = menu2(self)
					self.close()
					self.children.append(child)
				else:
					mixer.music.load('music/auntequedanintentos.mp3')
					mixer.music.play(1)					
					hablar(self,"Será al próximo intento no te rindas yo se que puedes lograrlo ")
					self.intentos.setText(str(intentos))

	def cancelar(self):	
		global CANTESTRELLAS 
		if(int (self.labelnivel.text()) == 1):
			child = menu2(self)
			self.close()
			self.children.append(child)		
		else:
			mixer.music.load('music/seralaproximavesPerder.mp3')
			mixer.music.play(1)			
			hablar(self,"Aun así tu esfuerzo por llegar hasta aquí, nos ayudo a encontrar "+str(int(self.labelnivel.text())-1)+" de mis amigos ")
			CANTESTRELLAS = CANTESTRELLAS + int (self.labelnivel.text())-1
			ModificarArchivo()
			child = menu2(self)
			self.close()
			self.children.append(child)

class amigosm3(QMainWindow):
	def __init__(self,intento,nivel):
		super(amigosm3, self).__init__()
		uic.loadUi("amigosMultiplesAvanzado.ui",self)
		self.children = []
		self.intentos.setText(str(intento))
		self.salir.clicked.connect(self.cancelar) 
		self.siguiente.clicked.connect(self.Siguiente)	
		self.numero1.setText(str(random.randint(100,999)))#random de 2 digito
		self.numero2.setText(str(random.randint(10,99)))#random de 2 digito
		self.labelnivel.setText(str(nivel))	#crear este label
		self.movie = QMovie("images/shakehabla.gif", QByteArray(), self)
		self.movie.setCacheMode(QMovie.CacheAll) 
		self.movie.setSpeed(100)
		self.shake.setMovie(self.movie)
		self.movie.start()
		global SEXOUSER
		global NOMBREUSUARIO
		global CANTESTRELLAS
		regex = QRegExp("[0-9_]+")
		validator = QRegExpValidator(regex)
		self.resultado1.setValidator(validator)
		self.resultado2.setValidator(validator)
		self.resultado4.setValidator(validator)
		self.totalEstrellas.setText(str(CANTESTRELLAS))
		if(SEXOUSER == "chico"):
			self.nombre.setText("Explorador: "+NOMBREUSUARIO)
		else:
			self.nombre.setText("Exploradora: "+NOMBREUSUARIO)
		self.show()
		if nivel==10 :
			hablar(self,"Estamos en el último nivel sé que puedes lograrlo y obtener el máximo de amigos posible! ")
		else:
			hablar(self,"Estamos en el nivel "+str(nivel)+" sé que puedes llegar al último y obtener el máximo de amigos posible! ")
		self.movie.stop()

	def Siguiente(self):
		mixer.init()
		if(int (self.labelnivel.text()) != 10):
			res=int(self.resultado4.text())
			num1=int(self.numero1.text())
			num2 =int(self.numero2.text())
			b1=False
			b2=False
			b3=False
			b4=False
			cade = self.numero2.text()
			n1 = cade[0]
			n2 = cade[1]
			print (n1,n2)
			if(int(self.resultado1.text())==(int(n2)*num1)):
				print("true"+self.resultado1.text()+"x"+str((int(n2)*num1)))
				b1=True
			else:
				hablar(self,"Revisa la 1 multiplicación")
				b1=False

			if(int(self.resultado2.text())==(int(n1)*num1)):
				print("true"+self.resultado2.text()+"x"+str((int(n1)*num1)))	
				b2=True
			else:
				#self.resultado.setStyle()#pintar de rojo
				hablar(self,"Revisa la 2 multiplicación")
				b2=False	

			if(res==(num1*num2)):	
				b4=True
			else:
				#self.resultado.setStyle()#pintar de rojo
				hablar(self,"Revisa el resultado")
				b4=False		

			if((b1==True) and (b2==True) and (b4==True)):
				mixer.music.load('music/originalcelebracionkarina.mp3')
				mixer.music.play(1)
				hablar(self," Siii, así se hace. Sabia que podías lograrlo ")
				ints=int(self.intentos.text())
				modimulti3(str(num1)+" X "+str(num2))
				time.sleep(2)
				child = amigosm3(ints,int(self.labelnivel.text())+1)
				self.close()
				self.children.append(child)
			else:	
				intentos =int(self.intentos.text())
				intentos = intentos - 1
				self.intentos.setText(str(intentos))
				if intentos == 0 :
					if(int(self.labelnivel.text()) > 1 ):
						mixer.music.load('music/seralaproximavesPerder.mp3')
						mixer.music.play(1)				
						hablar(self,"Se acabaron tus intentos pero, tu esfuerzo por llegar hasta aquí será recompenzado ganaste un total de "+str(int(self.labelnivel.text())-1)+" Estrellas " )
						CANTESTRELLAS = CANTESTRELLAS + int(self.labelnivel.text())-1
						time.sleep(2)
						ModificarArchivo()
						child = menu2(self)
						self.close()
						self.children.append(child)
					else:
						child = menu2(self)
						self.close()
						self.children.append(child)
				else:
					mixer.music.load('music/auntequedanintentos.mp3')
					mixer.music.play(1)
					hablar(self," Será al próximo intento, aun te quedan "+self.intentos.text()+" no te rindas yo se que puedes lograrlo ")
		else:
			res=int(self.resultado4.text())
			num1=int(self.numero1.text())
			num2 =int(self.numero2.text())
			b1=False
			b2=False
			b3=False
			b4=False
			cade = self.numero2.text()
			n1 = cade[0]
			n2 = cade[1]
			print (n1,n2,n3)
			if(int(self.resultado1.text())==(int(n2)*num1)):
				print("true"+self.resultado1.text()+"x"+str((int(n2)*num1)))
				b1=True
			else:
				b1=False

			if(int(self.resultado2.text())==(int(n1)*num1)):
				print("true"+self.resultado2.text()+"x"+str((int(n1)*num1)))	
				b2=True
			else:
				#self.resultado.setStyle()#pintar de rojo
				b2=False	

			if(res==(num1*num2)):	
				b4=True
			else:
				#self.resultado.setStyle()#pintar de rojo
				b4=False		

			if((b1==True) and (b2==True) and (b4==True)):
				#mixer.music.load('music/llegaral10.mp3')
				#mixer.music.play(1)				
				hablar(self," Siii, así se hace. Sabia que podías lograrlo, llegaste al nivel 10 y lo superaste ")
				hablar(self," Este logro nos ayuda a obtener 30 amigos extra ")
				CANTESTRELLAS = CANTESTRELLAS + int (self.labelnivel.text())+30
				modimulti3(str(num1)+" X "+str(num2))
				ModificarArchivo()
				child = menu2(self)
				self.close()
				self.children.append(child)

			else:	
				intentos =int(self.intentos.text())
				intentos = intentos - 1
				self.intentos.setText(str(intentos))
				if intentos == 0 :
					mixer.music.load('music/seralaproximavesPerder.mp3')
					mixer.music.play(1)
					hablar(self,"Se terminaron los intentos, intentemoslo desde el inicio de nuevo ")
					hablar(self,"Aun así tu esfuerzo por llegar hasta aquí, nos ayudo a encontrar "+str(int(self.labelnivel.text())-1)+" de mis amigos ")
					CANTESTRELLAS = CANTESTRELLAS + int (self.labelnivel.text())-1
					ModificarArchivo()
					child = menu2(self)
					self.close()
					self.children.append(child)
				else:
					mixer.music.load('music/auntequedanintentos.mp3')
					mixer.music.play(1)
					hablar(self," Será al próximo intento, aun te quedan "+self.intentos.text()+" no te rindas yo se que puedes lograrlo ")

	def cancelar(self):
		mixer.init()
		global CANTESTRELLAS 
		if(int (self.labelnivel.text()) == 1):
			child = menu2(self)
			self.close()
			self.children.append(child)
		else:
			mixer.music.load('music/seralaproximavesPerder.mp3')
			mixer.music.play(1)
			hablar(self,"Aun así tu esfuerzo por llegar hasta aquí, nos ayudo a encontrar "+str(int (self.labelnivel.text())-1)+" de mis amigos ")
			CANTESTRELLAS = CANTESTRELLAS + int (self.labelnivel.text())-1
			ModificarArchivo()
			child = menu2(self)
			self.close()
			self.children.append(child)


class menu2(QMainWindow):
	def __init__(self,name =None):
		super(menu2, self).__init__()
		uic.loadUi("amigosMultiplesmenu.ui",self)
		self.children = []
		self.AmigosMulti1.clicked.connect(self.amigos1) 
		self.AmigosMulti2.clicked.connect(self.amigos2)
		self.AmigosMulti3.clicked.connect(self.amigos3)
		self.salir.clicked.connect(self.cancelar)
		self.movie = QMovie("images/shakehabla.gif", QByteArray(), self)
		self.movie.setCacheMode(QMovie.CacheAll) 
		self.movie.setSpeed(100)
		self.shake.setMovie(self.movie)
		self.movie.start()
		global SEXOUSER
		global NOMBREUSUARIO
		global CANTESTRELLAS
		self.totalEstrellas.setText(str(CANTESTRELLAS))
		if(SEXOUSER == "chico"):
			self.nombre.setText("Explorador: "+NOMBREUSUARIO)
		else:
			self.nombre.setText("Exploradora: "+NOMBREUSUARIO)
		self.show()
		hablar(self,"Elije un nivel de amigos multiples. y comencemos la aventura")
		self.movie.stop()

	def amigos1(self):	
		child = amigosm1(3,1)
		self.children.append(child)
		self.close()

	def amigos2(self):	
		child = amigosm2(3,1)
		self.children.append(child)
		self.close()

	def amigos3(self):
		child = amigosm3(3,1)
		self.children.append(child)
		self.close()

	def cancelar(self):	
		self.close()
		child=VentanaPrincipal()	
		self.children.append(child)



class CSuma(QMainWindow):
	def __init__(self,intento,nivel):
		super(CSuma, self).__init__()
		uic.loadUi("sumassusesivas.ui",self)
		self.children = []
		regex = QRegExp("[0-9_]+")
		validator = QRegExpValidator(regex)		
		mixer.init()
		#mixer.music.load('music/ejerciciomultiplicacion.mp3')
		self.resultado.setValidator(validator)
		self.numero1.setText(str(random.randint(2,20)))
		self.numero2.setText(str(random.randint(1,20)))
		self.numero2aux.show()
		self.numero2aux.setText(self.numero2.text())
		self.labelnivel.setText(str(nivel))
		self.intentos.setText(str(intento))
		self.salir.clicked.connect(self.cancelar)
		self.mas.clicked.connect(self.fmas)
		self.menos.clicked.connect(self.fmenos)
		self.siguiente.clicked.connect(self.Siguiente)
		self.salir.setEnabled(False)
		self.mas.setEnabled(False)
		self.menos.setEnabled(False)
		regex = QRegExp("[0-9_]+")
		validator = QRegExpValidator(regex)
		self.resultado.setValidator(validator)
		self.siguiente.setEnabled(False)
		self.movie = QMovie("images/shakehabla.gif", QByteArray(), self)
		self.movie.setCacheMode(QMovie.CacheAll) 
		self.movie.setSpeed(100)
		self.shake.setMovie(self.movie)
		self.movie.start()
		self.nivel=1
		self.ves =0
		global SEXOUSER
		global NOMBREUSUARIO
		global CANTESTRELLAS
		self.totalEstrellas.setText(str(CANTESTRELLAS))
		if(SEXOUSER == "chico"):
			self.nombre.setText("Explorador: "+NOMBREUSUARIO)
		else:
			self.nombre.setText("Exploradora: "+NOMBREUSUARIO)
		self.show()
		if nivel==10 :
			hablar(self,"Estamos en el último cuadrante se que puedes lograrlo y obtener el máximo de amigos posible!")
		else:
			hablar(self,"Estamos en el cuadrante "+self.labelnivel.text()+" se que puedes llegar al último y obtener el máximo de amigos posible!")
		self.movie.stop()
		self.salir.setEnabled(True)
		self.mas.setEnabled(True)
		self.menos.setEnabled(True)
		self.siguiente.setEnabled(True)		

	def fmas(self):
		if self.ves <= 0 :
			self.representa.setPlainText(self.numero2.text())
			self.ves= self.ves + 1
		else:
			cadena1 = self.representa.toPlainText()
			cadena1 = cadena1+"+"+self.numero2.text()
			self.representa.setPlainText(cadena1)
			self.ves= self.ves + 1

	def fmenos(self):
		if self.ves <= 1 :
			self.representa.setPlainText("")
			self.ves = self.ves = 0
		else:
			cadena1 = self.representa.toPlainText()
			if(len(self.numero2.text()) < 2 ):
				cadena1 = cadena1[0:len(cadena1)-2]
			else: 
				cadena1 = cadena1[0:len(cadena1)-3]
			self.representa.setPlainText(cadena1)
			self.ves = self.ves - 1	

	def Siguiente(self):
		global CANTESTRELLAS
		mixer.init()
		res=int(self.resultado.text())#resultado de la suma sucesiva
		repre=str(self.representa.toPlainText())#escribir la suma sucesiva
		num1=int(self.numero1.text())
		num2 =int(self.numero2.text())
		par1=False
		par2=False
		count=0
		cadena=""
		while(count<num1):
			if(count==0 ):
				cadena=cadena + str(num2)
			else:
				cadena= cadena + "+"+str(num2)
			count=count+1	
		print(cadena)
		print(repre)
		if(res==((num1*num2) ) and (cadena == repre)):			
			if(int(self.labelnivel.text()) == 10):
				#mixer.music.load('music/llegar10.mp3')
				#mixer.music.play(1)
				hablar(self,"Sí, así se hace. Sabia que podias lograrlo superaste todos los cuadrantes y consegimos un total de 15 de mis amigos ")
				CANTESTRELLAS = CANTESTRELLAS + 5
				ModificarArchivo()
				self.close()
				child=VentanaPrincipal()	
				self.children.append(child)
			else:
				mixer.music.load('music/originalcelebracionkarina.mp3')
				mixer.music.play(1)
				hablar(self,"Sí, así se hace. Sabia que podias lograrlo pasemos al siguiente cuadrante ")		
				self.movie.stop()
				time.sleep(2)
				child = CSuma(int(self.intentos.text()),int(self.labelnivel.text())+1)
				self.children.append(child)
				self.close()

		else:
			self.intentos.setText(str(int(self.intentos.text())-1))
			if(int(self.intentos.text())==0):
				if(int(self.labelnivel.text()) > 1 ):
					mixer.music.load('music/seralaproximavesPerder.mp3')
					mixer.music.play(1)				
					hablar(self,"Se acabaron tus intentos pero, tu esfuerzo por llegar hasta aquí será recompenzado ganaste un total de "+str(int(self.labelnivel.text())-1)+" Estrellas " )
					CANTESTRELLAS = CANTESTRELLAS + int(self.labelnivel.text())-1
					time.sleep(2)
					self.close()
					child=VentanaPrincipal()	
					self.children.append(child)
				else:
					self.close()
					child=VentanaPrincipal()	
					self.children.append(child)
			else:	
				mixer.music.load('music/auntequedanintentos.mp3')
				mixer.music.play(1)
				hablar(self," Será al próximo intento, aun te quedan "+self.intentos.text()+" no te rindas yo se que puedes lograrlo ")

	def cancelar(self):	
		global CANTESTRELLAS 
		mixer.init()
		if(int (self.labelnivel.text()) == 1):
			self.close()
			child=VentanaPrincipal()	
			self.children.append(child)		
		else:
			hablar(self,"Aun así tu esfuerzo por llegar hasta aquí, nos ayudo a encontrar "+str(int(self.labelnivel.text())-1)+" de mis amigos ")
			mixer.music.load('music/seralaproximavesPerder.mp3')
			mixer.music.play(1)	
			CANTESTRELLAS = CANTESTRELLAS + int (self.labelnivel.text())-1
			ModificarArchivo()
			self.close()
			child=VentanaPrincipal()	
			self.children.append(child)

###modulos aprendiedo
def ocultar(self):
	self.ejer11.hide()
	self.ejer12.hide()
	self.ejer13.hide()
	self.ejer21.hide()
	self.ejer22.hide()
	self.ejer23.hide()
	self.resul11.hide()
	self.resul12.hide()
	self.resul13.hide()
	self.resul14.hide()
	self.resul21.hide()
	self.resul22.hide()
	self.resul23.hide()
	self.resul24.hide()
	self.resul31.hide()
	self.resul32.hide()
	self.resul33.hide()
	self.resul34.hide()
	self.resul41.hide()
	self.resul42.hide()
	self.resul43.hide()
	self.resul44.hide()
	self.resul45.hide()
	self.resul46.hide()
	self.resul47.hide()
	self.flecha11.hide()
	self.flecha12.hide()
	self.flecha13.hide()
	self.flecha21.hide()
	self.flecha22.hide()
	self.flecha23.hide()
	self.flechare11.hide()
	self.flechare12.hide()
	self.flechare13.hide()
	self.flechare14.hide()
	self.flechare21.hide()
	self.flechare22.hide()
	self.flechare23.hide()
	self.flechare24.hide()
	self.flechare31.hide()
	self.flechare32.hide()
	self.flechare33.hide()
	self.flechare34.hide()
	self.resulaux1.hide()
	self.resulaux2.hide()
	self.flechareaux2.hide()
	self.flechareaux1.hide()
	self.flechareaux2.hide()
	self.flechare41.hide()
	self.flechare42.hide()
	self.flechare43.hide()
	self.flechare44.hide()
	self.flechare45.hide()
	self.flechare46.hide()
	self.flechare47.hide()
	self.resulaux0.hide()
	self.linea2.hide()
	self.linea1.hide()
	self.simboloX.hide()
	self.simbolomas.hide()
	self.flechareaux0.hide()
	self.lleva2.hide()
	self.lleva3.hide()

	
def ocultarSuma(self):
	self.num1.hide()
	self.num2.hide()
	self.simboloigual1.hide()
	self.simboloigual2.hide()
	self.resultado.hide()
	self.veces.hide()


class CaprendiendoSumatoria(QMainWindow):
	def __init__(self,name =None):
		super(CaprendiendoSumatoria, self).__init__()
		uic.loadUi("aprendiendoSumaSucesiva.ui",self)
		self.children = []
		self.num1.setText(str(random.randint(2,9)))
		self.num2.setText(str(random.randint(1,9)))
		self.iteraciones= int(self.num1.text())
		self.resol.clicked.connect(self.resolver)
		self.salir.clicked.connect(self.Fsalir)
		self.nuevo.clicked.connect(self.Fnuevo)
		global SEXOUSER
		global NOMBREUSUARIO
		global CANTESTRELLAS
		self.totalEstrellas.setText(str(CANTESTRELLAS))
		if(SEXOUSER == "chico"):
			self.nombre.setText("Explorador: "+NOMBREUSUARIO)
		else:
			self.nombre.setText("Exploradora: "+NOMBREUSUARIO)
		ocultarSuma(self)
		self.show()
		mixer.init()
		mixer.music.load('music/precionanuevoejercicio.mp3')
		mixer.music.play(1)
		hablar(self,"Presiona nuevo ejercicio y observa el resultado")
		self.num1.show()
		self.num2.show()
		self.veces.show()


	def Fsalir(self):
		self.close()
		child=MenuAprender()
		self.children.append(child)	

	
	def Fnuevo (self):
		ocultarSuma(self)
		self.num1.setText(str(random.randint(2,9)))
		self.num2.setText(str(random.randint(1,9)))
		self.Tresolver.setText("")
		self.num1.show()
		self.num2.show()
		self.veces.show()
		

	def resolver (self):
		i=0
		self.resol.setEnabled(False)
		self.nuevo.setEnabled(False)
		self.salir.setEnabled(False)
		self.iteraciones= int(self.num1.text())
		n2=self.num2.text()
		self.simboloigual1.show()
		root = tkinter.Tk()
		cadena = ""
		while i < self.iteraciones:
			root.withdraw()
			root.update()
			hablar(self,"Agregamos por "+ str(i+1)+" ves el número a sumar ")
			if i == 0 :
				cadena = n2
				self.Tresolver.setText(cadena)
			else:
				cadena = cadena +"+"+n2
				self.Tresolver.setText(cadena)
			i = i +1 
		self.simboloigual2.show()
		self.resultado.setText(str(int(self.num1.text())*int(self.num2.text())))
		self.resultado.show()
		hablar(self,"luego de sumarlos todos el resultado es: "+self.resultado.text()+" ")
		self.resol.setEnabled(True)
		self.nuevo.setEnabled(True)
		self.salir.setEnabled(True)


def paso2(self,res) :
	numero=""
	if(self.paso == 1):
		if (res >= 10):
			numero = str(res)
			hablar(self, "como el numero es "+str(res)+" es una decena se guarda el numero "+numero[0]+" para sumarlo a la siguiente multiplicación " )
			hablar(self,"Es así como el numero que se queda para colocar en el resultado es "+numero[1]+" ")
			time.sleep(1)
			self.lleva2.setText(numero[0])
			self.lleva2.show()
			self.resul11.show()
			self.resul11.setText(numero[1])
			return int (numero[0])
		else:		
			hablar(self, "se coloca el numero "+str(res)+" en el resultado " )
			self.resul11.show()
			self.resul11.setText(str(res))
			return int (0)
	if(self.paso == 2):
		if (res >= 10):
			numero = str(res)
			hablar(self, "como el numero es "+str(res)+" es una decena se guarda el numero "+numero[0]+" para sumarlo a la siguiente multiplicación " )
			hablar(self,"Es así como el numero que se queda para colocar en el resultado es "+numero[1]+" ")
			time.sleep(1)
			self.resul12.show()
			self.resul12.setText(numero[1])
			self.lleva3.show()
			self.lleva3.setText(numero[0])
			return int (numero[0])
		else:		
			hablar(self, "se coloca el numero "+str(res)+" en el resultado " )
			self.resul12.show()
			self.resul12.setText(str(res))
			return 0
	
	if(self.paso == 3):
		if (res >= 10):
			numero = str(res)
			self.flechare13.show()
			hablar(self, "Al ser el último número multiplicado se coloca completo en el resultado ")
			self.resul13.show()
			self.resul14.show()
			self.resul13.setText(numero[1])
			self.resul14.setText(numero[0])
			self.flechare13.hide()
			self.flechare14.hide()

			return 0
		else:		
			hablar(self, "se coloca el numero "+str(res)+" en el resultado " )
			self.resul13.show()
			self.resul13.setText(str(res))

			return 0
		numero=""
	if(self.paso == 4):
		if (res >= 10):
			numero = str(res)
			hablar(self, "como el numero es "+str(res)+" es una decena se guarda el numero "+numero[0]+" para sumarlo a la siguiente multiplicación " )
			hablar(self,"Es así como el numero que se queda para colocar en el resultado es "+numero[1]+" ")
			time.sleep(1)
			self.resul21.show()
			self.resul21.setText(numero[1])
			self.lleva2.show()
			self.lleva2.setText(numero[0])
			return int (numero[0])
		else:		
			hablar(self, "se coloca el numero "+str(res)+" en el resultado" )
			self.resul21.show()
			self.resul21.setText(str(res))
			return int (0)
	if(self.paso == 5):
		if (res >= 10):
			numero = str(res)
			hablar(self, "como el numero es "+str(res)+" es una decena se guarda el numero "+numero[0]+" para sumarlo a la siguiente multiplicación " )
			hablar(self,"Es así como el numero que se queda para colocar en el resultado es "+numero[1]+" ")
			time.sleep(1)
			self.resul22.show()
			self.resul22.setText(numero[1])
			self.lleva3.show()
			self.lleva3.setText(numero[0])
			return int (numero[0])
		else:		
			hablar(self, "se coloca el numero "+str(res)+" en el resultado " )
			self.resul22.show()
			self.resul22.setText(str(res))
			return 0
	
	if(self.paso == 6):
		if (res >= 10):
			numero = str(res)
			self.flechare23.show()
			hablar(self, "Al ser el último número multiplicado se coloca completo en el resultado ")
			self.resul23.show()
			self.resul24.show()
			self.resul23.setText(numero[1])
			self.resul24.setText(numero[0])
			self.flechare23.hide()
			return 0
		else:		
			hablar(self, "se coloca el numero "+str(res)+" en el resultado " )
			self.resul23.show()
			self.resul23.setText(str(res))
			return 0		
	if(self.paso == 7):
		if (res >= 10):
			numero = str(res)
			hablar(self, "como el numero es "+str(res)+" es una decena se guarda el numero "+numero[0]+" para sumarlo a la siguiente multiplicación " )
			hablar(self,"Es así como el numero que se queda para colocar en el resultado es "+numero[1])
			self.resul31.show()
			self.resul31.setText(numero[1])
			return int (numero[0])
		else:		
			hablar(self, "se coloca el numero "+str(res)+" en el resultado " )
			self.resul31.show()
			self.resul31.setText(str(res))
			return 0	
	if(self.paso == 8):
		if (res >= 10):
			numero = str(res)
			hablar(self, "como el numero es "+str(res)+" es una decena se guarda el numero "+numero[0]+" para sumarlo a la siguiente multiplicación " )
			hablar(self,"Es así como el numero que se queda para colocar en el resultado es "+numero[1])
			self.resul32.show()
			self.resul32.setText(numero[1])
			return int (numero[0])
		else:		
			hablar(self, "se coloca el numero "+str(res)+" en el resultado" )
			self.resul32.show()
			self.resul32.setText(str(res))
			return 0
	if(self.paso == 9):
		if (res >= 10):
			numero = str(res)
			hablar(self, "Al ser el último número multiplicado se coloca completo en el resultado")
			self.resul33.show()
			self.resul34.show()
			self.resul33.setText(numero[1])
			self.resul34.setText(numero[0])
			return 0
		else:		
			hablar(self, "se coloca el numero "+str(res)+" en el resultado" )
			self.resul33.show()
			self.resul33.setText(str(res))
			return 0						



def paso1(self):
	if(self.paso == 1):
		if(self.tipo == 1):
			res = int(self.ejer21.text()) * int(self.ejer11.text()) 
			self.flecha21.show()
			self.flecha11.show()
			hablar(self, "Multiplicamos los números señalados por las flechas y su resultado es "+str(res)+" ")
			if res >= 10 :
				numero = str(res)
				self.resul11.show()
				self.resul12.show()
				self.resul12.setText(numero[0])
				self.resul11.setText(numero[1])
			else:
				self.resul11.show()
				self.resul11.setText(str(res))
			self.flecha21.hide()
			self.flecha11.hide()
			print("blockear")
		else:
			res = int(self.ejer21.text()) * int(self.ejer11.text()) 
			self.flecha21.show()
			self.flecha11.show()
			hablar(self, "Multiplicamos los números señalados por las flechas y su resultado es "+str(res)+" ")
			if (self.lleva == 0):
				self.lleva = paso2(self,res)

			else: 
				hablar(self, "le sumamos a el resultado de la multiplicación lo que llevamos que es "+str(self.lleva)+" dando como resultado "+str(res+self.lleva)+" ")	
				self.lleva = paso2(self,paso,res+self.lleva)
			self.flecha21.hide()
			self.flecha11.hide()


	if(self.paso == 2):
		res = int(self.ejer21.text()) * int(self.ejer12.text())
		self.flecha21.show()
		self.flecha12.show()
		hablar(self, "Multiplicamos los números señalados por las flechas y su resultado es "+str(res)+" ")
		if (self.lleva == 0):
			self.lleva = paso2(self,res)	
		else: 
			hablar(self, " le sumamos a el resultado de la multiplicación lo que llevamos que es "+str(self.lleva)+" dando como resultado "+str(res+self.lleva)+" ")	
			self.lleva = paso2(self,res+self.lleva)	
		self.flecha21.hide()
		self.flecha12.hide()
	if(self.paso == 3):
		res = int(self.ejer21.text()) * int(self.ejer13.text())
		self.flecha21.show()
		self.flecha13.show()
		hablar(self, "Multiplicamos los números señalados por las flechas y su resultado es"+str(res)+" ")
		if (self.lleva == 0):
			self.lleva = paso2(self,res)	
		else: 
			hablar(self, " le sumamos a el resultado de la multiplicación lo que llevamos que es "+str(self.lleva)+" dando como resultado "+str(res+self.lleva)+" ")	
			self.lleva = paso2(self,res+self.lleva)	
		self.flecha21.hide()
		self.flecha13.hide()
		if(self.tipo == 2):
			print("detener sig")
	if(self.paso == 4):
		res = int(self.ejer22.text()) * int(self.ejer11.text()) 
		self.flecha22.show()
		self.flecha11.show()
		hablar(self, "Multiplicamos los números señalados por las flechas y su resultado es "+str(res)+" ")
		if (self.lleva == 0):
			self.lleva = paso2(self,res)	
		else: 
			hablar(self, " le sumamos a el resultado de la multiplicación lo que llevamos que es "+str(self.lleva)+" dando como resultado "+str(res+self.lleva)+" ")	
			self.lleva = paso2(self,paso,res+self.lleva)
		self.flecha22.hide()
		self.flecha11.hide()
				
	if(self.paso == 5):
		res = int(self.ejer22.text()) * int(self.ejer12.text())
		self.flecha22.show()
		self.flecha12.show()
		hablar(self, "Multiplicamos los números señalados por las flechas y su resultado es "+str(res)+" ")
		if (self.lleva == 0):
			self.lleva = paso2(self,res)	
		else: 
			hablar(self, " le sumamos a el resultado de la multiplicación lo que llevamos que es"+str(self.lleva)+" dando como resultado "+str(res+self.lleva)+" ")	
			self.lleva = paso2(self,res+self.lleva)	
		self.flecha22.hide()
		self.flecha12.hide()
	if(self.paso == 6):
		res = int(self.ejer22.text()) * int(self.ejer13.text())
		self.flecha22.show()
		self.flecha13.show()
		hablar(self, "Multiplicamos los números señalados por las flechas y su resultado es "+str(res)+" ")
		if (self.lleva == 0):
			self.lleva = paso2(self,res)	
		else: 
			hablar(self, " le sumamos a el resultado de la multiplicación lo que llevamos que es"+str(self.lleva)+" dando como resultado "+str(res+self.lleva)+" ")	
			self.lleva = paso2(self,res+self.lleva)	
		self.flecha22.hide()
		self.flecha13.hide()
	if(self.paso == 7):
		if (self.tipo == 3):
			num1 = int(self.ejer13.text()+self.ejer12.text()+self.ejer11.text()) * int (self.ejer21.text())
			num2 = int(self.ejer13.text()+self.ejer12.text()+self.ejer11.text()) * int (self.ejer22.text()+"0")
			hablar(self, "entonces sumamos los resultados de la multiplicaciónes ")
			self.flechareaux0.show()
			self.linea2.show()
			self.simbolomas.show()
			self.resulaux0.show()
			self.resulaux0.setText("0")
			hablar(self, "Pero al segundo resultado se se agrega un 0 al final.")
			self.flechareaux0.hide()
			resu= num1 + num2
			cadena= str(resu)
			largo = len(cadena)
			print (str(largo))
			self.resulaux1.show()
			self.resulaux1.setText(cadena[largo-1])
			self.resulaux2.show()
			self.resulaux2.setText(cadena[largo-2])
			self.resul31.show()
			self.resul31.setText(cadena[largo-3])
			self.resul32.show()
			self.resul32.setText(cadena[largo-4])
			if    (largo - 5) >= 0:
				self.resul33.show()
				self.resul33.setText(cadena[largo-5])

			if    (largo - 6) >= 0 :
				print(str(largo - 6))
				self.resul34.show()
				self.resul34.setText(cadena[largo-6])
			hablar(self, "Obteniendo así el resultado de la multiplicación que es: "+cadena+" ")		

		else:
			res = int(self.ejer23.text()) * int(self.ejer11.text())
			self.flecha23.show()
			self.flecha11.show()
			hablar(self, "Multiplicamos los números señalados por las flechas y su resultado es "+str(res))
			if (self.lleva == 0):
				self.lleva = paso2(self,res)	
			else: 
				hablar(self, " le sumamos a el resultado de la multiplicación lo que llevamos que es"+str(self.lleva)+" dando como resultado "+str(res+self.lleva))	
				self.lleva = paso2(self,res+self.lleva)	
			self.flecha23.hide()
			self.flecha11.hide()
	if(self.paso == 8):
		res = int(self.ejer23.text()) * int(self.ejer12.text())
		self.flecha23.show()
		self.flecha12.show()
		hablar(self, "Multiplicamos los números señalados por las flechas y su resultado es "+str(res))
		if (self.lleva == 0):
			self.lleva = paso2(self,res)	
		else: 
			hablar(self, " le sumamos a el resultado de la multiplicación lo que llevamos que es"+str(self.lleva)+" dando como resultado "+str(res+self.lleva))	
			self.lleva = paso2(self,res+self.lleva)	
		self.flecha23.hide()
		self.flecha12.hide()
	if(self.paso == 9):
		res = int(self.ejer23.text()) * int(self.ejer13.text())
		self.flecha23.show()
		self.flecha13.show()
		hablar(self, "Multiplicamos los números señalados por las flechas y su resultado es "+str(res))
		if (self.lleva == 0):
			self.lleva = paso2(self,res)	
		else: 
			hablar(self, " le sumamos a el resultado de la multiplicación lo que llevamos que es"+str(self.lleva)+" dando como resultado "+str(res+self.lleva))	
			self.lleva = paso2(self,res+self.lleva)	
		self.flecha23.hide()
		self.flecha13.hide()
	if(self.paso == 10):
		print("hacer suma")
		num1 = int(self.ejer13.text()+self.ejer12.text()+self.ejer11.text()) * int (self.ejer21.text())
		num2 = int(self.ejer13.text()+self.ejer12.text()+self.ejer11.text()) * int (self.ejer22.text()+"0")
		num3 = int(self.ejer13.text()+self.ejer12.text()+self.ejer11.text()) * int (self.ejer23.text()+"00")
		hablar(self, "entonces procedemos a sumar los  resultados de la multiplicación")
		self.flechareaux0.show()
		self.flechareaux1.show()
		self.flechareaux2.show()
		self.resulaux0.show()
		self.resulaux0.setText("0")
		self.resulaux1.show()
		self.resulaux1.setText("0")
		self.resulaux2.show()
		self.resulaux2.setText("0")
		hablar(self, "Llenamos los espacios vacíos con 0 y sumamos los resultados")
		resu= num1 + num2 + num3
		self.resulaux0.hide()
		self.resulaux1.hide()
		self.resulaux2.hide()
		self.flechareaux0.hide()
		self.flechareaux1.hide()
		self.flechareaux2.hide()
		cadena= str(resu)
		largo = len(cadena)
		self.resul41.show()
		self.resul41.setText(cadena[largo-1])
		self.resul42.show()
		self.resul42.setText(cadena[largo-2])
		self.resul43.show()
		self.resul43.setText(cadena[largo-3])
		self.resul44.show()
		self.resul44.setText(cadena[largo-4])
		self.resul45.show()
		self.resul45.setText(cadena[largo-5])
		self.resul46.show()
		self.resul46.setText(cadena[largo-6])
		if   -1 !=  (largo - 7):
			self.resul47.show()
			self.resul47.setText(cadena[largo-7])


	self.paso=self.paso +1

class CAprendiendoMultiplicar2(QMainWindow):
	def __init__(self,name =None):
		super(CAprendiendoMultiplicar2, self).__init__()
		uic.loadUi("AprendiendoMultiplicar.ui",self)
		self.children = []
		mixer.init()
		mixer.music.load('music/ejerciciosmultiplicaion.mp3')
		self.num1 = []
		self.num2 = []
		self.res = []
		self.paso=1
		self.lleva=0
		self.tipo =4
		self.salir.clicked.connect(self.Fsalir)
		self.seguir.clicked.connect(self.Fseguir)
		self.nv1.clicked.connect(self.Fnv1)
		self.nv2.clicked.connect(self.Fnv2)
		self.nv3.clicked.connect(self.Fnv3)
		num2 = [int(self.ejer21.text())]
		ocultar(self)
		global SEXOUSER
		global NOMBREUSUARIO
		global CANTESTRELLAS
		self.totalEstrellas.setText(str(CANTESTRELLAS))
		if(SEXOUSER == "chico"):
			self.nombre.setText("Explorador: "+NOMBREUSUARIO)
		else:
			self.nombre.setText("Exploradora: "+NOMBREUSUARIO)
		self.show()
		#mostrar lo que lleva
		mixer.music.play(1)
		hablar(self,"Veamos un ejercicio de multiplicación, selecciona un tipo de ejercicio y observa el procedimiento para solucionarlo.")
		
	def Fnv1(self):
		ocultar(self)
		self.linea1.show()
		self.simboloX.show()
		self.ejer13.hide()
		self.ejer12.hide()
		self.ejer23.hide()
		self.ejer22.hide()
		self.ejer11.setText(str(random.randint(0,9)))
		self.ejer11.show()
		self.ejer21.setText(str(random.randint(0,9)))
		self.ejer21.show()
		self.tipo=1


	def Fnv2 (self):
		ocultar(self)
		self.linea1.show()
		self.simboloX.show()
		self.ejer11.setText(str(random.randint(0,9)))
		self.ejer12.setText(str(random.randint(0,9)))
		self.ejer13.setText(str(random.randint(1,9)))
		self.ejer11.show()
		self.ejer12.show()
		self.ejer13.show()
		self.ejer23.hide()
		self.ejer22.hide()
		self.ejer21.setText(str(random.randint(0,9)))
		self.ejer21.show()
		self.tipo=2

	def Fnv3(self):	
		ocultar(self)
		self.linea1.show()
		self.simboloX.show()
		self.ejer11.setText(str(random.randint(0,9)))
		self.ejer12.setText(str(random.randint(0,9)))
		self.ejer13.setText(str(random.randint(1,9)))
		self.ejer11.show()
		self.ejer12.show()
		self.ejer13.show()
		"""if int(self.ejer13.text()) == 0 :
			self.ejer13.hide()
			res = self.ejer12.text() + self.ejer11.text()
			num1 = [int(self.ejer12.text()), int(self.ejer11.text())]
		else:
			res = self.ejer13.text() + self.ejer12.text() + self.ejer11.text()
			num1 = [int(self.ejer13.text()), int(self.ejer12.text()), int(self.ejer11.text())]
		"""
		self.ejer21.setText(str(random.randint(0,9)))
		self.ejer22.setText(str(random.randint(1,9)))
		self.ejer21.show()
		self.ejer22.show()
		self.tipo=3

	def Fseguir(self):
		cant = 0 
		itera =0 
		self.paso=1
		if(self.tipo == 3):
			itera= 7
		if(self.tipo == 2):
			itera= 3
		if(self.tipo == 1):
			itera= 1
		self.salir.setEnabled(False)
		self.seguir.setEnabled(False)
		self.nv1.setEnabled(False)
		self.nv2.setEnabled(False)
		self.nv3.setEnabled(False)
		while (cant < itera ):
			time.sleep(3)
			paso1(self)
			cant=cant+1
		self.salir.setEnabled(True)
		self.seguir.setEnabled(True)
		self.nv1.setEnabled(True)
		self.nv2.setEnabled(True)
		self.nv3.setEnabled(True)

	def Fsalir(self):
		self.close()
		child=MenuAprender()
		self.children.append(child)	
		
class CUsosMatematica(QMainWindow):

	def __init__(self,name =None):
		super(CUsosMatematica, self).__init__()
		uic.loadUi("UsosMatematica.ui",self) 
		self.children = []
		mixer.init()
		mixer.music.load('music/usosmultiplicaciones.mp3')
		
		self.salir.clicked.connect(self.Fsalir)
		self.construccion.clicked.connect(self.Construccion)
		self.dinero.clicked.connect(self.Dinero)
		self.tecnologia.clicked.connect(self.Tecnologia)
		self.medicina.clicked.connect(self.Medicina)
		self.astronautica.clicked.connect(self.Astronauta)	
		global SEXOUSER
		global NOMBREUSUARIO
		global CANTESTRELLAS
		self.totalEstrellas.setText(str(CANTESTRELLAS))
		if(SEXOUSER == "chico"):
			self.nombre.setText("Explorador: "+NOMBREUSUARIO)
		else:
			self.nombre.setText("Exploradora: "+NOMBREUSUARIO)
		self.dinero.setEnabled(False)
		self.tecnologia.setEnabled(False)
		self.medicina.setEnabled(False)
		self.construccion.setEnabled(False)
		self.astronautica.setEnabled(False)
		self.show()
		mixer.music.play(1)

		hablar(self,"Te mostraré los distintos usos de las multiplicaciónes")
		self.dinero.setEnabled(True)
		self.tecnologia.setEnabled(True)
		self.medicina.setEnabled(True)
		self.construccion.setEnabled(True)
		self.astronautica.setEnabled(True)

	def Construccion(self):
		self.dinero.setEnabled(False)
		self.tecnologia.setEnabled(False)
		self.medicina.setEnabled(False)
		self.construccion.setEnabled(False)
		self.astronautica.setEnabled(False)	
		self.movie = QMovie("images/uso1.jpg", QByteArray(), self)
		self.movie.setCacheMode(QMovie.CacheAll) 
		self.movie.setSpeed(100)
		self.imagen.setMovie(self.movie)
		self.movie.start()
		mixer.init()
		mixer.music.load('music/constructores.mp3')
		mixer.music.play(1)		
		hablar(self,"Los Constructores la utilizan para poder saber cantidad de materiales que necesitan y las medidas necesarias para seguir los planos que el arquitecto realiza de forma minuciosa utilizando cálculos con la finalidad de crear una casa o edificio seguro")				
		self.movie.stop()
		self.dinero.setEnabled(True)
		self.tecnologia.setEnabled(True)
		self.medicina.setEnabled(True)
		self.construccion.setEnabled(True)
		self.astronautica.setEnabled(True)

	def Tecnologia(self):
		self.dinero.setEnabled(False)
		self.tecnologia.setEnabled(False)
		self.medicina.setEnabled(False)
		self.construccion.setEnabled(False)
		self.astronautica.setEnabled(False)	
		self.movie = QMovie("images/uso2.jpg", QByteArray(), self)
		self.movie.setCacheMode(QMovie.CacheAll)
		self.movie.setSpeed(100)
		self.imagen.setMovie(self.movie)
		self.movie.start() 
		mixer.init()
		mixer.music.load('music/tecnologia.mp3')
		mixer.music.play(1)
		hablar(self,"En la Tecnología se utilizan calculando qué tipo de materiales y qué cantidad de éstos son necesarios para construir las piezas del funcionamiento interno de las computadoras, teléfonos, tablets entre otros. Luego personas como los informáticos son capaces de usar estas tecnologías y comunicarse con ellas y crear páginas web, juegos, aplicaciones utilizando sus conocimientos junto con la matemática para lograr esto y más.")		
		self.movie.stop()
		self.dinero.setEnabled(True)
		self.tecnologia.setEnabled(True)
		self.medicina.setEnabled(True)
		self.construccion.setEnabled(True)
		self.astronautica.setEnabled(True)

	def Medicina(self):	
		self.dinero.setEnabled(False)
		self.tecnologia.setEnabled(False)
		self.medicina.setEnabled(False)
		self.construccion.setEnabled(False)
		self.astronautica.setEnabled(False)
		self.movie = QMovie("images/uso3.jpg", QByteArray(), self)
		self.movie.setCacheMode(QMovie.CacheAll) 
		self.movie.setSpeed(100)
		self.imagen.setMovie(self.movie)
		self.movie.start()
		mixer.init()
		mixer.music.load('music/medicina.mp3')
		mixer.music.play(1)
		hablar(self,"En la medicina, se utilizan las matemáticas en especialidades como la farmacéutica con la finalidad de poder crear los medicamentos controlando las cantidades de 1 vitamina o más que posea el medicamento y de esta manera pueda curar las enfermedades sin afectar al cuerpo.")			
		self.movie.stop()
		self.dinero.setEnabled(True)
		self.tecnologia.setEnabled(True)
		self.medicina.setEnabled(True)
		self.construccion.setEnabled(True)
		self.astronautica.setEnabled(True)

	def Astronauta(self):	
		self.dinero.setEnabled(False)
		self.tecnologia.setEnabled(False)
		self.medicina.setEnabled(False)
		self.construccion.setEnabled(False)
		self.astronautica.setEnabled(False)
		self.movie = QMovie("images/uso4.jpg", QByteArray(), self)
		self.movie.setCacheMode(QMovie.CacheAll) 
		self.movie.setSpeed(100)
		self.imagen.setMovie(self.movie)
		self.movie.start()	
		mixer.init()
		mixer.music.load('music/astronautica.mp3')
		mixer.music.play(1)
		hablar(self,"En la astronáutica utilizan las matemáticas con el fin de realizar los cálculos que permitan al cohete llegar al espacio y volver de él, también estos cálculos les permiten mantener seguros a los  astronautas en el espacio y que puedan vivir en éste.")	
		self.movie.stop()
		self.dinero.setEnabled(True)
		self.tecnologia.setEnabled(True)
		self.medicina.setEnabled(True)
		self.construccion.setEnabled(True)
		self.astronautica.setEnabled(True)

	def Dinero(self):
		self.dinero.setEnabled(False)
		self.tecnologia.setEnabled(False)
		self.medicina.setEnabled(False)
		self.construccion.setEnabled(False)
		self.astronautica.setEnabled(False)
		self.movie = QMovie("images/uso5.jpg", QByteArray(), self)
		self.movie.setCacheMode(QMovie.CacheAll) 
		self.movie.setSpeed(100)
		self.imagen.setMovie(self.movie)
		self.movie.start()
		mixer.init()
		mixer.music.load('music/administracion.mp3')
		mixer.music.play(1)		
		hablar(self,"En la vida diaria puedes utilizarlo para administrar tus ahorros, gastos, compras, entre otros")
		self.movie.stop()
		self.dinero.setEnabled(True)
		self.tecnologia.setEnabled(True)
		self.medicina.setEnabled(True)
		self.construccion.setEnabled(True)
		self.astronautica.setEnabled(True)

	def Fsalir(self):
		self.close()
		child=MenuAprender()
		self.children.append(child)	


class tablasdemultiplicar(QMainWindow):
	def __init__(self,name =None):
		super(tablasdemultiplicar, self).__init__()
		uic.loadUi("TablasDeMultiplicar.ui",self)
		self.children = []
		self.salir.clicked.connect(self.Fsalir)
		self.btabla0.clicked.connect(self.Ftabla0)
		self.btabla1.clicked.connect(self.Ftabla1)
		self.btabla2.clicked.connect(self.Ftabla2)
		self.btabla3.clicked.connect(self.Ftabla3)
		self.btabla4.clicked.connect(self.Ftabla4)
		self.btabla5.clicked.connect(self.Ftabla5)
		self.btabla6.clicked.connect(self.Ftabla6)
		self.btabla7.clicked.connect(self.Ftabla7)
		self.btabla8.clicked.connect(self.Ftabla8)
		self.btabla9.clicked.connect(self.Ftabla9)
		self.btabla10.clicked.connect(self.Ftabla9)
		global SEXOUSER
		global NOMBREUSUARIO
		global CANTESTRELLAS
		self.totalEstrellas.setText(str(CANTESTRELLAS))
		if(SEXOUSER == "chico"):
			self.nombre.setText("Explorador: "+NOMBREUSUARIO)
		else:
			self.nombre.setText("Exploradora: "+NOMBREUSUARIO)
		self.show()
		mixer.init()
		mixer.music.load('music/tablasbasicasdelamultiplicacion.mp3')
		mixer.music.play(1)
		hablar(self,"Te mostraré tablas básicas de multiplicación selecciona 1, observa y escucha ")

	def Fsalir(self):
		self.close()
		child=MenuAprender()
		self.children.append(child)	

	def Ftabla0(self):
		mixer.init()
		mixer.music.load('music/tabladel0.mp3')
		mixer.music.play(1)
		self.multi1.setText("0 x 0 = 0")
		self.multi2.setText("0 x 1 = 0")
		self.multi3.setText("0 x 2 = 0")
		self.multi4.setText("0 x 3 = 0")
		self.multi5.setText("0 x 4 = 0")
		self.multi6.setText("0 x 5 = 0")
		self.multi7.setText("0 x 6 = 0")
		self.multi8.setText("0 x 7 = 0")
		self.multi9.setText("0 x 8 = 0")
		self.multi10.setText("0 x 9 = 0")
		self.multi11.setText("0 x 10 = 0")


	def Ftabla1(self):
		mixer.init()
		mixer.music.load('music/tabla1.mp3')
		mixer.music.play(1)
		self.multi1.setText("1 x 0 = 0")
		self.multi2.setText("1 x 1 = 1")
		self.multi3.setText("1 x 2 = 2")
		self.multi4.setText("1 x 3 = 3")
		self.multi5.setText("1 x 4 = 4")
		self.multi6.setText("1 x 5 = 5")
		self.multi7.setText("1 x 6 = 6")
		self.multi8.setText("1 x 7 = 7")
		self.multi9.setText("1 x 8 = 8")
		self.multi10.setText("1 x 9 = 9")	
		self.multi11.setText("1 x 10 = 100")


	def Ftabla2(self):
		mixer.init()
		mixer.music.load('music/tabla2.mp3')
		mixer.music.play(1)
		self.multi1.setText("2 x 0 = 0")
		self.multi2.setText("2 x 1 = 2")
		self.multi3.setText("2 x 2 = 4")
		self.multi4.setText("2 x 3 = 6")
		self.multi5.setText("2 x 4 = 8")
		self.multi6.setText("2 x 5 = 10")
		self.multi7.setText("2 x 6 = 12")
		self.multi8.setText("2 x 7 = 14")
		self.multi9.setText("2 x 8 = 16")
		self.multi10.setText("2 x 9 = 18")
		self.multi11.setText("2 x 10 = 20")



	def Ftabla3(self):
		mixer.init()
		mixer.music.load('music/tabla3.mp3')
		mixer.music.play(1)
		self.multi1.setText("3 x 0 = 0")
		self.multi2.setText("3 x 1 = 3")
		self.multi3.setText("3 x 2 = 6")
		self.multi4.setText("3 x 3 = 9")
		self.multi5.setText("3 x 4 = 12")
		self.multi6.setText("3 x 5 = 15")
		self.multi7.setText("3 x 6 = 18")
		self.multi8.setText("3 x 7 = 21")
		self.multi9.setText("3 x 8 = 24")
		self.multi10.setText("3 x 9 = 27")
		self.multi11.setText("3 x 10 = 30")


	def Ftabla4(self):
		mixer.init()
		mixer.music.load('music/tabla4.mp3')
		mixer.music.play(1)
		self.multi1.setText("4 x 0 = 0")
		self.multi2.setText("4 x 1 = 4")
		self.multi3.setText("4 x 2 = 8")
		self.multi4.setText("4 x 3 = 12")
		self.multi5.setText("4 x 4 = 16")
		self.multi6.setText("4 x 5 = 20")
		self.multi7.setText("4 x 6 = 24")
		self.multi8.setText("4 x 7 = 28")
		self.multi9.setText("4 x 8 = 32")
		self.multi10.setText("4 x 9 = 36")
		self.multi11.setText("4 x 10 = 40")



	def Ftabla5(self):
		mixer.init()
		mixer.music.load('music/tabla5.mp3')
		mixer.music.play(1)
		self.multi1.setText("5 x 0 = 0")
		self.multi2.setText("5 x 1 = 5")
		self.multi3.setText("5 x 2 = 10")
		self.multi4.setText("5 x 3 = 15")
		self.multi5.setText("5 x 4 = 20")
		self.multi6.setText("5 x 5 = 25")
		self.multi7.setText("5 x 6 = 30")
		self.multi8.setText("5 x 7 = 35")
		self.multi9.setText("5 x 8 = 40")
		self.multi10.setText("5 x 9 = 45")
		self.multi11.setText("5 x 10 = 50")



	def Ftabla6(self):
		mixer.init()
		mixer.music.load('music/tabla6.mp3')
		mixer.music.play(1)
		self.multi1.setText("6 x 0 = 0")
		self.multi2.setText("6 x 1 = 6")
		self.multi3.setText("6 x 2 = 12")
		self.multi4.setText("6 x 3 = 18")
		self.multi5.setText("6 x 4 = 24")
		self.multi6.setText("6 x 5 = 30")
		self.multi7.setText("6 x 6 = 36")
		self.multi8.setText("6 x 7 = 42")
		self.multi9.setText("6 x 8 = 48")
		self.multi10.setText("6 x 9 = 54")
		self.multi11.setText("6 x 10 = 60")
	


	def Ftabla7(self):
		mixer.init()
		mixer.music.load('music/tabla7.mp3')
		mixer.music.play(1)
		self.multi1.setText("7 x 0 = 0")
		self.multi2.setText("7 x 1 = 7")
		self.multi3.setText("7 x 2 = 14")
		self.multi4.setText("7 x 3 = 21")
		self.multi5.setText("7 x 4 = 28")
		self.multi6.setText("7 x 5 = 35")
		self.multi7.setText("7 x 6 = 42")
		self.multi8.setText("7 x 7 = 49")
		self.multi9.setText("7 x 8 = 56")
		self.multi10.setText("7 x 9 = 63")
		self.multi11.setText("7 x 10 = 70")
	


	def Ftabla8(self):
		mixer.init()
		mixer.music.load('music/tabla8.mp3')
		mixer.music.play(1)
		self.multi1.setText("8 x 0 = 0")
		self.multi2.setText("8 x 1 = 8")
		self.multi3.setText("8 x 2 = 16")
		self.multi4.setText("8 x 3 = 24")
		self.multi5.setText("8 x 4 = 32")
		self.multi6.setText("8 x 5 = 40")
		self.multi7.setText("8 x 6 = 48")
		self.multi8.setText("8 x 7 = 54")
		self.multi9.setText("8 x 8 = 64")
		self.multi10.setText("8 x 9 = 72")	
		self.multi11.setText("8 x 10 = 80")
	

	def Ftabla9(self):
		mixer.init()
		mixer.music.load('music/tabla9.mp3')
		mixer.music.play(1)
		self.multi1.setText("9 x 0 = 0")
		self.multi2.setText("9 x 1 = 9")
		self.multi3.setText("9 x 2 = 18")
		self.multi4.setText("9 x 3 = 27")
		self.multi5.setText("9 x 4 = 36")
		self.multi6.setText("9 x 5 = 55")
		self.multi7.setText("9 x 6 = 64")
		self.multi8.setText("9 x 7 = 73")
		self.multi9.setText("9 x 8 = 82")
		self.multi10.setText("9 x 9 = 91")
		self.multi11.setText("9 x 10 = 90")	

	def Ftabla10(self):
		mixer.init()
		mixer.music.load('music/tabla10.mp3')
		mixer.music.play(1)
		self.multi1.setText("10 x 0 = 0")
		self.multi2.setText("10 x 1 = 10")
		self.multi3.setText("10 x 2 = 20")
		self.multi4.setText("10 x 3 = 30")
		self.multi5.setText("10 x 4 = 40")
		self.multi6.setText("10 x 5 = 50")
		self.multi7.setText("10 x 6 = 60")
		self.multi8.setText("10 x 7 = 70")
		self.multi9.setText("10 x 8 = 80")
		self.multi10.setText("10 x 9 = 90")
		self.multi11.setText("10 x 10 = 100")		


class Cpropiedadesmultiplicacion(QMainWindow):
	def __init__(self,name =None):
		super(Cpropiedadesmultiplicacion, self).__init__()
		uic.loadUi("Propiedadesdemultiplicar.ui",self)
		self.neutro.clicked.connect(self.Fneutro)
		self.nulo.clicked.connect(self.Fnulo)
		self.show()
		mixer.init()
		mixer.music.load('music/propiedadesdemultiplicacion.mp3')
		mixer.music.play(1)
		hablar(self,"Aquí aprenderemos sobre las propiedades de la multiplicación selecciona una") 
		self.conmutativa.clicked.connect(self.FConmutativa)
		#self.distributiva.clicked.connect(self.Fdistributiva)
		self.salir.clicked.connect(self.cancelar)
		self.children = []
		
	def Fneutro (self):
		mixer.init()
		mixer.music.load('music/elementoneutro.mp3')
		mixer.music.play(1)
		self.ejemplo1.setText("1 x 2 = 2")
		self.ejemplo2.setText("1 x 3 = 3")
		self.ejemplo3.setText("8 x 1 = 8")
		hablar(self," El elemento neutro de las multiplicaciones es el número 1, quien al ser multiplicado por cualquier cantidad siempre dará como resultado el mismo número multiplicado, como puedes ver en la pizarra")


	def Fnulo (self):
		mixer.init()
		mixer.music.load('music/elementonulo.mp3')
		mixer.music.play(1)
		self.ejemplo1.setText("1 x 0 = 0")
		self.ejemplo2.setText("5 x 0 = 0")
		self.ejemplo3.setText("0 x 7 = 0")
		hablar(self,"El elemento nulo de las multiplicaciones es el número 0, debido a que multiplicar este número por otro siempre nos dará como resultado 0, como puedes ver en la pizarra")


	def FConmutativa (self):
		mixer.init()
		mixer.music.load('music/conmutativa.mp3')
		mixer.music.play(1)
		self.ejemplo1.setText("1 x 2 = 2    y    2 x 1 = 2" )
		self.ejemplo2.setText("5 x 4 = 20   y    4 x 5 = 20")
		self.ejemplo3.setText("3 x 7 = 21   y    7 x 3 = 21")
		hablar(self,"La conmutativa se refiere a que en las multiplicaciones el orden de los números no altera el resultado, como puedes ver en la pizarra")

	

	def cancelar(self):	
		self.close()
		child=MenuAprender()	
		self.children.append(child)			


class Cqueesmultiplicar(QMainWindow):
	def __init__(self,name =None):
		super(Cqueesmultiplicar, self).__init__()
		uic.loadUi("queesmultiplicacion.ui",self)
		self.salir.clicked.connect(self.cancelar)
		self.siguiente.clicked.connect(self.sigue)
		self.children = []
		self.show()
		mixer.init()
		mixer.music.load('music/defmultiplicacion.mp3')
		mixer.music.play(1)
		hablar(self,"La multiplicación es una operación matemática que consiste en sumar varias veces el mismo número, la multiplicación usa como base la suma sucesiva ")

	def sigue(self):	
		self.close()
		child=Cpropiedadesmultiplicacion()	
		self.children.append(child)			

	def cancelar(self):	
		self.close()
		child=MenuAprender()	
		self.children.append(child)	

class Cqueesmatematica(QMainWindow):
	def __init__(self,name =None):
		super(Cqueesmatematica, self).__init__()
		uic.loadUi("queesmatematica.ui",self)
		self.salir.clicked.connect(self.cancelar)
		self.children = []
		self.show()
		mixer.init()
		mixer.music.load('music/defmatematica.mp3')
		mixer.music.play(1)
		hablar(self,"Las matemáticas, se pueden explicar como todas las operaciones que podemos realizar gracias a los números, como lo pueden ser la suma o la resta, e incluso al contarlos para hacer cualquier cuenta estarás usando las matemáticas en tu vida.")
		

	def cancelar(self):	
		self.close()
		child=MenuAprender()	
		self.children.append(child)	

class Cqueessumasusesiva(QMainWindow):
	def __init__(self,name =None):
		super(Cqueessumasusesiva, self).__init__()
		uic.loadUi("queessumasuceciva.ui",self)
		self.salir.clicked.connect(self.cancelar)
		self.children = []

		self.show()
		mixer.init()
		mixer.music.load('music/sumassucesivaas.mp3')
		mixer.music.play(1)
		hablar(self,"Esta es una operación matemática bastante necesaria, y consiste en sumar un mismo número en repetidas ocasiones, como podemos ver en la pizarra.")
		
	def cancelar(self):	
		self.close()
		child=MenuAprender()	
		self.children.append(child)		


class MenuAprender(QMainWindow):
	def __init__(self,name =None):
		super(MenuAprender, self).__init__()
		uic.loadUi("AprendiendoMenu.ui",self)
		self.children = []
		mixer.init()
		mixer.music.load('music/AprendamosSobrelasmultiplicaciones.mp3')
		self.salir.setEnabled(False)
		self.sumassusesivas.setEnabled(False)
		self.multiplicar.setEnabled(False)
		self.matematica.setEnabled(False)
		self.tablasmulti.setEnabled(False)
		self.usosmatematica.setEnabled(False)
		self.ejemplos.setEnabled(False)
		self.ejemplosSuma.setEnabled(False)
		self.salir.clicked.connect(self.cancelar)
		self.matematica.clicked.connect(self.Fmatematica)
		self.sumassusesivas.clicked.connect(self.Fsumassusesivas)
		self.multiplicar.clicked.connect(self.Fmultiplicar)
		self.tablasmulti.clicked.connect(self.Ftablasmulti)
		self.usosmatematica.clicked.connect(self.Fusomatematica)
		self.ejemplos.clicked.connect(self.Fejemulti)
		self.ejemplosSuma.clicked.connect(self.FejeSuma)
		global SEXOUSER
		global NOMBREUSUARIO
		global CANTESTRELLAS
		self.totalEstrellas.setText(str(CANTESTRELLAS))

		if(SEXOUSER == "chico"):
			self.nombre.setText("Explorador: "+NOMBREUSUARIO)
		else:
			self.nombre.setText("Exploradora: "+NOMBREUSUARIO)
		self.show()
		mixer.music.play(1)
		hablar(self,"Aprendamos sobre las multiplicaciones")
		self.salir.setEnabled(True)
		self.sumassusesivas.setEnabled(True)
		self.multiplicar.setEnabled(True)
		self.matematica.setEnabled(True)
		self.tablasmulti.setEnabled(True)
		self.usosmatematica.setEnabled(True)
		self.ejemplos.setEnabled(True)
		self.ejemplosSuma.setEnabled(True)
	
	def Fmultiplicar (self):
		child = Cqueesmultiplicar(self)
		self.close()
		self.children.append(child)	

	def Fsumassusesivas (self):
		child = Cqueessumasusesiva(self)
		self.close()
		self.children.append(child)	
	
	def Fmatematica (self):
		child = Cqueesmatematica(self)
		self.close()
		self.children.append(child)	
			

	def Fejemulti(self):
		child = CAprendiendoMultiplicar2(self)
		self.close()
		self.children.append(child)	


	def Ftablasmulti(self):
		mixer.music.stop()
		mixer.quit()
		child = tablasdemultiplicar(self)
		self.close()
		self.children.append(child)

	def FejeSuma(self):
		child = CaprendiendoSumatoria(self)
		self.close()
		self.children.append(child)

	def Fusomatematica(self):
		child = CUsosMatematica(self)
		self.close()
		self.children.append(child)	
		
	def cancelar(self):	
		self.close()
		child=VentanaPrincipal()	
		self.children.append(child)	


class RegistrarProfesor(QMainWindow):
	def __init__(self):
		global NOMBREUSUARIO
		global SEXOPROFESOR
		global CORREOPROFESOR
		global PASSWORD
		super(RegistrarProfesor, self).__init__()
		self.children = []
		uic.loadUi("AdminReguistrar.ui",self)
		self.adelante.clicked.connect(self.registrar)
		self.salir.clicked.connect(self.salir2)
		self.movie = QMovie("images/shakehabla.gif", QByteArray(), self)
		self.movie.setCacheMode(QMovie.CacheAll) 
		self.movie.setSpeed(100)
		self.shake.setMovie(self.movie)
		self.movie.start()
		if NOMBREPROFESOR == "" :
			hablar(self, "Bienvenido profesor, porfavor ingrese los siguientes datos")
		else:
			hablar(self, "Edite sus datos")
			self.nombre.setText(NOMBREUSUARIO)
			self.correo.setText(CORREOPROFESOR)
			self.password.setText(PASSWORD)
		self.movie.stop()		
		self.show()


	def registrar(self) :
		global NOMBREPROFESOR
		global SEXOPROFESOR
		global CORREOPROFESOR
		global PASSWORD
		n=False
		s=False
		c=False
		p=False
		if (self.nombre.text()==""):
			print("campo vacio")
		else: 
			NOMBREPROFESOR = self.nombre.text()
			n=True
		if self.hombre.isChecked() :
			s=True
			SEXOPROFESOR = "Hombre" 	
		if self.mujer.isChecked() :
			s=True
			SEXOPROFESOR = "Mujer" 	
		if (self.correo.text()==""):
			print("campo vacio")
		else: 
			CORREOPROFESOR = self.correo.text()
			c=True	
		if (self.password.text()==""):
			print("campo vacio")
		else: 
			PASSWORD = self.password.text()
			p=True	

		if((n == True) and (s == True) and (n == True) and (s == True)):	
			print("todo correcto")
			ModificarArchivo()
			self.close()
			child = CmoduloAdministrador()
			self.children.append(child)
		else:
			QMessageBox.about(self, "Alerta!!!", "Alguno de los elemenos esta en blanco todos son necesarios")

	def salir2(self):
		self.close()


class CmoduloAdministrador(QMainWindow):
	def __init__(self,name =None):
		super(CmoduloAdministrador, self).__init__()
		uic.loadUi("moduloprofesor.ui",self)
		global NOMBREPROFESOR
		global SEXOPROFESOR
		global CORREOPROFESOR
		global PASSWORD
		global NOMBREUSUARIO

		self.children = []
		
		self.editar.clicked.connect(self.editar2)
		self.enviar.clicked.connect(self.Fenviar)
		self.nv1.clicked.connect(self.Fnv1)
		self.nv2.clicked.connect(self.Fnv2)
		self.nv3.clicked.connect(self.Fnv3)
		self.salir.clicked.connect(self.cancelar)
		if (SEXOPROFESOR=="Hombre"):
			self.mensaje.setText("Bienvenido Profesor: "+NOMBREPROFESOR+"")
		else:
			self.mensaje.setText("Bienvenida Profesora: "+NOMBREPROFESOR+"")
		if (SEXOUSER=="chico"):
			self.tablatitulo.setText("Ejercicios resueltos por: "+NOMBREUSUARIO+"")
		else:
			self.tablatitulo.setText("Ejercicios resueltos por: "+NOMBREUSUARIO+"")	
			
		self.show()

	def editar2(self):
		child = RegistrarProfesor()
		self.children.append(child)	

	def fadministrador(self):
		global NOMBREPROFESOR 
		child = RegistrarProfesor()
		self.children.append(child)	

	def CCorreo (self):
		global CORREOPROFESOR
		s = CORREOPROFESOR
		CORREOPROFESOR = self.correo.text()
		ModificarArchivo()
		print("correo "+s+" cambiado por "+CORREOPROFESOR+" ")

	def CNombre (self):
		global NOMBREPROFESOR
		s = NOMBREPROFESOR
		NOMBREPROFESOR = self.nombre.text()
		ModificarArchivo()
		print("Nombre "+s+" cambiado por "+NOMBREPROFESOR+" ")
	
	def CPassword (self):
		global PASSWORD
		s= PASSWORD
		PASSWORD = self.password.text()
		ModificarArchivo()
		print("Contraceña "+s+" cambiada por "+PASSWORD+" ")

	def CSexo (self):
		global SEXOPROFESOR

		if self.chica.isChecked() :
			s=True
			SEXOUSER = "Mujer" 	
		if self.chico.isChecked() :
			s=True
			SEXOUSER = "Hombre" 
		if s == False :
			print("seleccione sexo")
		else:
			ModificarArchivo()




	def Fnv1 (self):
		i=0
		for i in reversed(range(self.tablaDatos.rowCount())):
			self.tablaDatos.removeRow(i)
		file = open("files/multiplicacion1.txt", "r")
		linea = file.readline()
		cadena1=""
		cadena2=""
		row=0
		while linea != "":
			self.tablaDatos.insertRow(row)
			lugar= linea.find("/")
			cadena1 = linea[:lugar]
			cadena2 = linea[lugar+1:len(linea)-1]
			self.tablaDatos.setItem(row,0,QtWidgets.QTableWidgetItem(cadena1))
			self.tablaDatos.setItem(row,1,QtWidgets.QTableWidgetItem(cadena2))
			linea = file.readline()
			row=row+1
		file.close()

	def Fnv2 (self):
		i=0
		for i in reversed(range(self.tablaDatos.rowCount())):
			self.tablaDatos.removeRow(i)
		file = open("files/multiplicacion2.txt", "r")
		linea = file.readline()
		cadena1=""
		cadena2=""
		row=0
		while linea != "":
			self.tablaDatos.insertRow(row)
			lugar= linea.find("/")
			cadena1 = linea[:lugar]
			cadena2 = linea[lugar+1:len(linea)-1]
			self.tablaDatos.setItem(row,0,QtWidgets.QTableWidgetItem(cadena1))
			self.tablaDatos.setItem(row,1,QtWidgets.QTableWidgetItem(cadena2))
			linea = file.readline()
			row=row+1
		file.close()	
	

	def Fnv3 (self):
		i=0
		for i in reversed(range(self.tablaDatos.rowCount())):
			self.tablaDatos.removeRow(i)
		file = open("files/multiplicacion3.txt", "r")
		linea = file.readline()
		cadena1=""
		cadena2=""
		row=0
		while linea != "":
			self.tablaDatos.insertRow(row)
			lugar= linea.find("/")
			cadena1 = linea[:lugar]
			cadena2 = linea[lugar+1:len(linea)-1]
			self.tablaDatos.setItem(row,0,QtWidgets.QTableWidgetItem(cadena1))
			self.tablaDatos.setItem(row,1,QtWidgets.QTableWidgetItem(cadena2))
			linea = file.readline()
			row=row+1
		file.close()


	def Fenviar(self):
		global CORREOPROFESOR
		global NOMBREUSUARIO
		root = tkinter.Tk()
		root.withdraw()
		try: 
			remitente = 'shake-shake_app@outlook.com'
			destinatario  = [CORREOPROFESOR]
			print(CORREOPROFESOR)
			asunto = 'Ejercicios Resueltos'
			msg = 'Buenas '+NOMBREPROFESOR+' aquí le estamos enviando los últimos avances de '+NOMBREUSUARIO+' que usted Solicito'

			mensaje = MIMEMultipart()

			mensaje['From'] = remitente
			mensaje['To'] = ", ".join(destinatario)
			mensaje['Subject'] = asunto
			mensaje.attach(MIMEText(msg, 'plain'))
			m = MIMEApplication(open("files/multiplicación1.txt","rb").read())

			m.add_header('Content-Disposition', 'attachment', filename="multiplicaciónes.txt")
			
			mensaje.attach(m)

			m = MIMEApplication(open("files/multiplicación2.txt","rb").read())

			m.add_header('Content-Disposition', 'attachment', filename="multiplicaciónes2.txt")

			mensaje.attach(m)

			m = MIMEApplication(open("files/multiplicación3.txt","rb").read())

			m.add_header('Content-Disposition', 'attachment', filename="multiplicaciónes3.txt")

			mensaje.attach(m)

			mailserver = smtplib.SMTP('smtp.office365.com',587)

			mailserver.ehlo()

			mailserver.starttls()

			mailserver.login('shake-shake_app@outlook.com', 'proyectocursos1')

			mailserver.sendmail('shake-shake_app@outlook.com', CORREOPROFESOR ,mensaje.as_string())

			mailserver.quit() 
		except: 
			messagebox.showerror("Alerta!!!", "Error revise su conexion a internet o los datos de su correo")
			#QMessageBox.about(self, "Alerta!!!", "Error revise su conexion a internet o los datos de su correo")
	
	def cancelar(self):	
		self.close()
		

class FAdministrador(QMainWindow):
	def __init__(self,name =None):
		super(FAdministrador, self).__init__()
		uic.loadUi("adminlogin.ui",self)
		self.children = []
		self.adelante.clicked.connect(self.fadelante)
		self.movie = QMovie("images/shakehabla.gif", QByteArray(), self)
		self.movie.setCacheMode(QMovie.CacheAll) 
		self.movie.setSpeed(100)
		self.movie.start()
		self.show()
		hablar(self,"Èste es el módulo del administrador, de uso exclusivo para el maestro, si quiere ingresar debe colocar la contraseña correcta")	
		self.movie.stop()
		time.sleep(2)

	def fadelante(self):
		global PASSWORD
		password2=""
		if (self.Password.text()==""):
			print("campo vacio")
		else: 
			password2 = self.Password.text()
			print("todo correcto")
			if(password2==PASSWORD):
				self.close()
				child = CmoduloAdministrador()
				self.children.append(child)
			else:
				print("contraceña incorrecta")
				password2=""
				password2 = self.Password.setText("")


class VentanaPrincipal(QMainWindow):
	def __init__(self):
		global ENTRADAS
		global NOMBREUSUARIO
		global CANTESTRELLAS
		global SEXOPROFESOR
		global SEXOUSER
		mixer.init()
		mixer.music.load('music/volviste.mp3')

		#s = sched.scheduler(time.time, time.sleep)
		super(VentanaPrincipal, self).__init__()
		self.children = []
		uic.loadUi("principal.ui",self)
		self.TeoriaSuma.setEnabled(False)
		self.administrador.setEnabled(False)
		self.SumaAmigos.setEnabled(False)
		self.BuscaAmigos.setEnabled(False)
		self.AmigosMulti.setEnabled(False)
		self.TeoriaSuma.clicked.connect(self.menuaprender)
		self.administrador.clicked.connect(self.fadministrador)
		self.SumaAmigos.clicked.connect(self.FSuma)
		self.BuscaAmigos.clicked.connect(self.busca)
		self.AmigosMulti.clicked.connect(self.menu2)
		self.movie = QMovie("images/shakehabla.gif", QByteArray(), self)
		self.movie.setCacheMode(QMovie.CacheAll) 
		self.movie.setSpeed(100)
		self.shake.setMovie(self.movie)
		self.movie.start()
		self.totalEstrellas.setText(str(CANTESTRELLAS))
		if(SEXOUSER == "chico"):
			self.nombre.setText("Explorador: "+NOMBREUSUARIO)
		else:
			self.nombre.setText("Exploradora: "+NOMBREUSUARIO)
		if NOMBREPROFESOR != "":
			if(SEXOPROFESOR=="mujer"):	
				self.profesora.setText("Profesora: "+NOMBREPROFESOR)
			else:
				self.profesora.setText("Profesor: "+NOMBREPROFESOR)
		else:
			self.profesora.setText("")		
		self.totalEstrellas.setText(str(CANTESTRELLAS))
			
		
		self.show()
		mixer.music.play(1)	
		ENTRADAS= ENTRADAS +1
		hablar(self, "Hola "+NOMBREUSUARIO+", gracias por volver continuemos la aventura en busca de mis amigos estrellas, tu cantidad de estrellas es: "+str(CANTESTRELLAS)+" espero consigamos más")	
		ModificarArchivo()
		
		self.movie.stop()
		self.TeoriaSuma.setEnabled(True)
		self.administrador.setEnabled(True)
		self.SumaAmigos.setEnabled(True)
		self.BuscaAmigos.setEnabled(True)
		self.AmigosMulti.setEnabled(True)


	def busca(self):
		self.close()	
		child = buscaamigos(self)
		self.children.append(child)
		

	def FSuma(self):
		self.close()	
		child = CSuma(3,1)
		self.children.append(child)
		
	
	def menu2(self):	
		child = menu2(self)
		self.close()
		self.children.append(child)

	def menuaprender(self):
		child = MenuAprender()
		self.close()
		self.children.append(child)		

	def fadministrador(self):
		global NOMBREPROFESOR 

		if NOMBREPROFESOR == "":
			child = RegistrarProfesor()
			self.children.append(child)	
		else:		
			child = FAdministrador()
			self.children.append(child)	



class Inicio(QMainWindow):
	def __init__(self):
		global ENTRADAS
		global NOMBREUSUARIO
		global SEXOUSER
		super(Inicio, self).__init__()
		self.children = []
		mixer.init()
		mixer.music.load('music/shakeshake1ves.mp3')		
		uic.loadUi("inicios.ui",self)
		self.adelante.clicked.connect(self.fadelante)
		self.movie = QMovie("images/shakehabla.gif", QByteArray(), self)
		self.movie.setCacheMode(QMovie.CacheAll) 
		self.movie.setSpeed(100)
		self.shake.setMovie(self.movie)
		self.movie.start()
		self.show()
		mixer.music.play(1)
		hablar(self, "Hola como estas, esto es shake-shake una aplicación donde surcaremos el espacio para reunirme con mis amigos estrellas para eso utilizaremos las multiplicaciones")	
		self.movie.stop()

	def fadelante(self):
		global NOMBREUSUARIO
		global SEXOUSER
		n=False
		s=False
		if (self.Nombre.text()==""):
			print("campo vacio")
		else: 
			NOMBREUSUARIO = self.Nombre.text()
			n=True
		if self.chico.isChecked() :
			s=True
			SEXOUSER = "chico" 	
		if self.chica.isChecked() :
			s=True
			SEXOUSER = "chica" 	
		if((n == True) and (s == True)):	
			print("todo correcto")
			crearmulti1()
			crearmulti2()
			crearmulti3()
			ModificarArchivo()
			self.close()
			child = VentanaPrincipal()
			self.children.append(child)
		else:
			print("falta un dato")


if(os.path.exists('files/Datos.txt')):
	CargarDatos()
	app= QApplication(sys.argv)
	__ventana=VentanaPrincipal()

else:
	app= QApplication(sys.argv)
	__ventana=Inicio()

	
app.exec_()