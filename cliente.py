
#def leer_tarea():  # Es la tarea que el usuario va a realizar, como escribir:tigo 3322
#	id_sonda = int(raw_input('Ingrese el ID de la sonda: '))
#	id_cliente = int(raw_input('Customer (1=Tigo Bolivia 2=Nuevatel ): '))

class cliente():

	def __init__(nombre_cliente, nombre_contacto):
 	 		self.nombre_cliente = nombre_cliente
 	 		self.nombre_contacto = nombre_contacto

 	def cliente_contacto(self):
 	 		return "El nombre del cliente es %s y su contacto es %i" % (self.nombre_cliente, self.nombre_contacto) 
