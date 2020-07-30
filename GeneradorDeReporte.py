# -*- coding: utf-8 -*-
import re
from cliente import Cliente

#La funcion tarea capta y separa el nombre del cliente y la sonda que ingresaron
def tarea(comando):
	palabra= comando
	patron = re.compile('([a-zA-Z]+)(\s)')
	matcher = patron.search(palabra)
	cliente = matcher.group()
	print ('El cliente es: ' + cliente)
	patron = re.compile('(\s)([0-9]+)')
	matcher = patron.search(palabra)
	matcher.groups()
	id_sonda = matcher.group(0)
	print ('La sonda es: ' + id_sonda)
	#En este codigo se llama la clase Cliente y la funcion buscar cliente
	# objetoCliente = Cliente("tigo","test")
	# print(objetoCliente.buscar_cliente())
	return cliente

def listadoDeClientes():
	cliente=Cliente("test","test2")
	x=cliente.mostrar_clientes()
	return "resultado :"+str(x)


def main():
 	tarea("tigo 3322")
	listadoDeClientes()


	#crear un objeto cliente, el cliente debe gardar la sonda, crear la si no existe,
	#Se deben mostrar los issues
	#Crear dentro de la carpeta de la sonda una carpeta que diga incidentes, que por dentro tenta un json con los issues.
	#

if __name__=='__main__':
     main()
