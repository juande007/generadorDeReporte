
#def leer_tarea():  # Es la tarea que el usuario va a realizar, como escribir:tigo 3322
#	id_sonda = int(raw_input('Ingrese el ID de la sonda: '))
#	id_cliente = int(raw_input('Customer (1=Tigo Bolivia 2=Nuevatel ): '))

from Sonda import Sonda
class Cliente(object):
    def __init__(self,nombre_cliente,nombre_contacto):
        self.nombre_cliente = nombre_cliente
        self.nombre_contacto = nombre_contacto

    def cliente_contacto(self):
	    return "El nombre del cliente es %s y su contacto es %s" % (self.nombre_cliente, self.nombre_contacto)

def main():
	tarea=raw_input('Ingrese el cliente y las sondas. ejemplo togobo 2233 4456')
        print(tarea)
	carlos=Cliente("Tigo","Carlos Mercado")
	print(carlos.cliente_contacto())
        sonda = Sonda(raw_input('Ingrese Id de la nueva sonda: '))
        print (sonda.agregarSonda())
        print (sonda.agregarNombre(raw_input('Ingrese el nombre de la sonda: ')))
        print (sonda.agregarDescripcion(raw_input('Descripcion de sonda: ')))
        sonda.imprimirSonda()

if __name__=='__main__':
    main()
