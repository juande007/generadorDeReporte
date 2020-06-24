# -*- coding: utf-8 -*-
import time

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Inches
from docx.enum.text import WD_LINE_SPACING
from docx.shared import Length
from docx.shared import Pt

#navegador = str(raw_input('Ejemplo: Ingrese Tigo 3322'))

#contact = str(raw_input('Nombre de Contacto : '))
#navegador =

#if navegador

#def leer_tarea():  # Es la tarea que el usuario va a realizar, como escribir:tigo 3322
id_sonda = int(raw_input('Ingrese el ID de la sonda: '))
id_cliente = int(raw_input('Customer (1=Tigo Bolivia 2=Nuevatel ): '))
#leer_tarea()

def run():
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
		document.add_paragraph("Customer: Tigo Bolivia")
		document.add_paragraph("Contac Name: Carlos Mercado")
		document.add_paragraph("Call id: ")
		document.add_paragraph("Date & Time: " + time.strftime("%x"))

		paragraph = document.add_paragraph('')
		run = paragraph.add_run('Cliente ID: ' + str(id_sonda))
		run.bold = True

		paragraph = document.add_paragraph('')
		run = paragraph.add_run('Descripcion: ')
		run.bold = True

		document.add_paragraph("--------------------------------------------------------------------")
		document.add_paragraph("2. DETAILS OF INCIDENT: ")
		document.add_paragraph("Impacted platform: ")
		document.add_paragraph("Root Cause: ")
		document.add_paragraph("Incident description: ")
		document.add_paragraph("Evidencias: ")

		document.add_paragraph("--------------------------------------------------------------------")
		document.add_paragraph("3. RESOLUTION")
		document.add_paragraph("Incident Analysis: ")
		document.add_paragraph("Workaround: ")
		document.add_paragraph("Recommendation: ")
		document.add_paragraph("Additional comments: NA")
		document.save('Sonda.docx')

	elif id_cliente > 1:
		print ('Descarga doc 2')
		document = Document()
		document.add_heading("Python Doc Word 2")
		document.add_paragraph("ID de la sonda: " + str(id_sonda))
		document.add_paragraph("ID de erros: ")
		document.save('SondaDePrueba2.docx')
run()
