# -*- coding: utf-8 -*-
import time
import json
import re
import GeneradorDeReporte
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
			print ("El cliente es desde word: "+str(self.cliente))
			id_cliente = int(raw_input('Customer (1=Tigo Bolivia 2=Nuevatel ): '))

			if id_cliente == 1:
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
				document.add_paragraph("Customer:"+ str(self.cliente))
				document.add_paragraph("Contac Name: Carlos Mercado")
				document.add_paragraph("Call id: ")
				document.add_paragraph("Date & Time: " + time.strftime("%x"))

				self.lista = li
				# for value in self.lista:
				contador = 0
				for element in self.lista:
					print li[contador][0]
					sonda = li[contador][0]
					issue = li[contador][1]
					contador =+ 1

					paragraph = document.add_paragraph('')
					run = paragraph.add_run('Cliente ID: ' + str(sonda))
					run.bold = True
					paragraph = document.add_paragraph('')
					run = paragraph.add_run('Descripcion: ')
					run.bold = True


					document.add_paragraph("--------------------------------------------------------------------")
					document.add_paragraph("2. DETAILS OF INCIDENT: ")
					document.add_paragraph("Impacted platform: ")
					document.add_paragraph("Root Cause: "+ str(issue))
					document.add_paragraph("Incident description: ")
					document.add_paragraph("Evidencias: ")

					document.add_paragraph("--------------------------------------------------------------------")
					document.add_paragraph("3. RESOLUTION")
					document.add_paragraph("Incident Analysis: ")
					document.add_paragraph("Workaround: ")
					document.add_paragraph("Recommendation: ")
					document.add_paragraph("Additional comments: NA")
					document.save('C:\Users\CORE i3\Documents\GitHub\generadorDeReporte\Clientes\Temporal\Reporte_Errores\Sonda.docx')


			elif id_cliente > 1:
				print ('Descarga doc 2')
				document = Document()
				document.add_heading("Python Doc Word 2")
				document.add_paragraph("ID de la sonda: " + str(id_sonda))
				document.add_paragraph("ID de erros: ")
				document.save('SondaDePrueba2.docx')

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
