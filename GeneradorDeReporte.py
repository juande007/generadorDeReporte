# -*- coding: utf-8 -*-
import re
from cliente import Cliente

#La funcion tarea capta y separa el nombre del cliente y la sonda que ingresaron
def tarea(comando):
	palabra= comando
	patron = re.compile('([a-zA-Z]+)(\s)')
	matcher = patron.search(palabra)
	cliente = matcher.group()
	print(('El cliente es: ' + cliente))
	regex = '\d+'
	match = re.findall(regex, comando)
	print(match)
	return match

def listadoDeClientes():
	cliente=Cliente("test","test2")
	x=cliente.mostrar_clientes()
	return x

def main():
    tarea("tigo 3322")
    listadoDeClientes()
	#crear un objeto cliente, el cliente debe gardar la sonda, crear la si no existe,
	#Se deben mostrar los issues
	#Crear dentro de la carpeta de la sonda una carpeta que diga incidentes, que por dentro tenta un json con los issues.
	#

if __name__=='__main__':
     main()
