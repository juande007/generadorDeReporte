# -*- coding: utf-8 -*-
import time
import json
import re
import os
import GeneradorDeReporte
from datetime import datetime
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Inches
from docx.enum.text import WD_LINE_SPACING
from docx.shared import Length
from docx.shared import Pt
#
class Reportes:
	def __init__(self,cliente):
 		self.cliente =cliente

	def datosReporte(self, li):

		self.lista = li
		contador=0
		for element in li:
			print li[contador][0]
			contador =+ 1
			print("Entro a generador word")


	def recolectorDatos():

		incidente='LatePacket.json'
		f = open("C:\Users\CORE i3\Documents\GitHub\generadorDeReporte/Incidentes/"+incidente, "r")
		contenido = f.read()
		archivoJson = json.loads(contenido)

		for lineaArchivoConfig in archivoJson["nuevoIncident"]:
			analisis  = lineaArchivoConfig["Analisis"]
			descripcion = lineaArchivoConfig["Descripcion"]
			workAround = lineaArchivoConfig["Workaround"]
			rootCause = lineaArchivoConfig["Root Cause"]
			recomendacion = lineaArchivoConfig["Recomendacion"]

			print(descripcion)
			print(analisis)
			print(rootCause)

	def generadorWord(self, li):

			# id_sonda = int(raw_input('Ingrese el ID de la sonda: '))
			print ("El cliente es desde word: '"+str(self.cliente)+"'")

			now = datetime.utcnow()
			date_time = now.strftime("%d-%m-%Y")
			date_timeFile = now.strftime("%Y%m%d")

			# C:/Users/CORE i3/Documents/GitHub/generadorDeReporte
			file = open('Clientes/'+self.cliente+'/'+self.cliente+'.json', "r")
			cont = file.read()
			archJson = json.loads(cont)

			for lineaArchivo in archJson["nombreDeCliente"]:
				contacto  = lineaArchivo["nombre_contacto"]

			print 'Descarga el doc 1'
			document = Document()
			style = document.styles['Normal']
			font = style.font
			font.name = 'Arial'
			font.size = Pt(9.1)
			font.italic = True

			document.add_paragraph("--------------------------------------------------------------------")
			document.add_paragraph("1. GENERAL INFO")
			document.add_paragraph("GEMALTO SUPPORT TEAM - TECHNICAL REPORT")
			document.add_paragraph("Customer: "+ str(self.cliente))
			document.add_paragraph("Contac Name: "+str(contacto))
			document.add_paragraph("Call id: ")
			document.add_paragraph("Date & Time: " + str(date_time))
			#2020-09-18
			#time.strftime("%x"))
			self.lista = li
			# for value in self.lista:
			contador = 0
			for element in self.lista:
				print li[contador][0]
				sonda = li[contador][0]
				issue = li[contador][1]


				incidente= issue
				f = open("C:\Users\CORE i3\Documents\GitHub\generadorDeReporte/Incidentes/"+incidente, "r")
				contenido = f.read()
				archivoJson = json.loads(contenido)

				for lineaArchivoConfig in archivoJson["nuevoIncident"]:
					analisis  = lineaArchivoConfig["Analisis"]
					descripcion = lineaArchivoConfig["Descripcion"]
					workAround = lineaArchivoConfig["Workaround"]
					rootCause = lineaArchivoConfig["Root Cause"]
					recomendacion = lineaArchivoConfig["Recomendacion"]

					document.add_paragraph("")
					document.add_paragraph("")
					document.add_paragraph("")
					document.add_paragraph("")
					document.add_paragraph("--------------------------------------------------------------------")
					paragraph = document.add_paragraph('')
					run = paragraph.add_run('Cliente ID: ' + str(sonda))
					run.bold = True
					paragraph = document.add_paragraph('')
					run = paragraph.add_run('Descripcion: '+ str(descripcion))
					run.bold = True

					document.add_paragraph("--------------------------------------------------------------------")
					document.add_paragraph("2. DETAILS OF INCIDENT: ")
					document.add_paragraph("Impacted platform: ")
					document.add_paragraph("Root Cause: "+ str(rootCause))
					document.add_paragraph("Incident description: ")
					document.add_paragraph("Evidencias: ")

					document.add_paragraph("--------------------------------------------------------------------")
					document.add_paragraph("3. RESOLUTION")
					document.add_paragraph("Incident Analysis: "+ str(analisis))
					document.add_paragraph("Workaround: "+ str(workAround))
					document.add_paragraph("Recommendation: "+ str(recomendacion))
					document.add_paragraph("Additional comments: NA")

					contador += 1


			ruta = 'C:/Users/CORE i3/Documents/GitHub/generadorDeReporte/Clientes/'+self.cliente+'/Reporte_Errores/'
			print (ruta)
					#20200918_ATT_Probes
			if os.path.exists(ruta):
				document.save(ruta+'/'+str(date_timeFile)+'_ATT_Probes.docx')
			else:
				print ("Entro a else")
				os.makedirs(ruta)
				document.save(ruta+'/'+str(date_timeFile)+'_ATT_Probes.docx')


class DatosReporte:
	   def __init__(self, sonda, issue):
			self.sonda = sonda
			self.issue = issue
			self.lista = []

def main():
	reportes = Reportes()
	reportes.generadorWord()
	# reportes.datosReporte()
if __name__=='__main__':
        main()
