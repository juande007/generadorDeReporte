import json
import os
from os import remove
from shutil import rmtree
from Sonda import Sonda
#EL OBJ
class Cliente(object):

    #Esta funcion es con constructor, el cual va a recibir el nombre del cliente y persona a cargo.
    def __init__(self,nombre_cliente,nombre_contacto):
        self.nombre_cliente = nombre_cliente
        self.nombre_contacto = nombre_contacto

    def cliente_contacto(self):
	    return "El nombre del cliente es %s y su contacto es %s" % (self.nombre_cliente, self.nombre_contacto)
        #Esta funcion muestra el menu de Gestion de Cliente
    def menu_cliente():
        print('1- Editar un cliente: ')
        print('2- Eliminar un cliente: ')
        opcion = (raw_input('Seleccione la tarea a realizar: '))
        if opcion == '1':
            editar_cliente()
        else:
            eliminar_cliente()
        #Esta funcion muestra todos los clientes existentes
    def mostrar_clientes(self):
        print('L I S T A  D E  C L I E N T E S')
        dir = "./Clientes"
        contenido = os.listdir(dir)
        print(contenido)
        return contenido
        #Esta funcion crea un nuevo cliente con sus respectivos atributos
    def agregar_Cliente():
        print ('Nuevo cliente.\n')
        nuevo_cliente= str(raw_input('Ingrese nombre del nuevo cliente: '))
        clientJson = {}
        clientJson ['nombreDeCliente'] =[]
        clientJson ['nombreDeCliente'].append({
        'nombre_corto ': nuevo_cliente
        })
        dir = './Clientes/' +nuevo_cliente
        os.mkdir(str(dir))
        file_name = str(nuevo_cliente)+'.json'
        #Este codigo crea un archivo json del nuevo cliente
        with open(os.path.join(dir, file_name), 'w') as file:
            json.dump(clientJson, file, indent=4)
        print ("Se guardo nuevo cliente: " + nuevo_cliente)
        #Esta funcion permite editar un cliente ya existente
    def editar_cliente():
        dir_Clientes = "./Clientes/"
        #Aqui se solcita el nombre y nuevo nombre del cliente que se quiere editar
        nombre_cliente = str(raw_input('Ingrese nombre del cliente: '))
        nuevo_nombre = str(raw_input('Ingrese el nuevo nombre: '))
        path_cliente =  dir_Clientes+nombre_cliente
        clientJson = {}
        clientJson ['nombreDeCliente'] =[]
        clientJson ['nombreDeCliente'].append({
        'nombre_corto ': nuevo_nombre
        })
        #Aqui se especifican las rutas donde se renombra el cliente que se quiere editar, la carpeta y archivo json seran editados
        path_nombre = dir_Clientes+nuevo_nombre
        file_cliente_old = path_nombre + '/' + nombre_cliente+".json"
        file_cliente_new = path_nombre + '/' + nuevo_nombre+".json"
        #Este codgo es el responsable de editar el nombre del cliente
        os.rename(path_cliente,path_nombre)
        os.rename(file_cliente_old,file_cliente_new)
        #Este codigo abre y renombra el archivo json
        with open(str(file_cliente_new), 'r') as file:
            json.load(file)
            file.close()
            print("archivo a crear :"+file_cliente_new)
            print("Nombre del anterior archivo:"+file_cliente_old)
        with open(str(file_cliente_new), 'w') as file:
            json.dump(clientJson, file, indent=4)
        #Esta funcion permite eliminar un cliente
    def eliminar_cliente():
        #Aqui especificamos la ruta de la carpeta del cliente a eliminar y solicitamos el nombre del cliente a eliminar
        carpeta= (raw_input('Escriba el nombre de la carpeta a eliminar: '))
        rmtree('./Clientes/'+ carpeta,carpeta)
        #Esta funcion nos permite buscar un cliente en el directorio
    def buscar_cliente(self):
        #Aqui solicitamos el nombre del cliente a buscar y se muestra el resultado
        carpetaBusq = (raw_input('Ingrese el nombre del cliente a buscar: '))
        print(os.path.isdir('./Clientes/' +carpetaBusq))
        print(carpetaBusq)
        return "Esta funcion no se ah implemenado"

def main():
        #eliminar_cliente()
        tarea=raw_input('Ingrese el cliente y las sondas. ejemplo togobo 2233 4456')
        print(tarea)
        carlos=Cliente("Tigo","Carlos Mercado")
        print(carlos.cliente_contacto())
        sonda = Sonda(raw_input('Ingrese Id de la nueva sonda: '))
        print (sonda.agregarSonda())
        print (sonda.agregarNombre(raw_input('Ingrese el nombre de la sonda: ')))
        print (sonda.agregarDescripcion(raw_input('Descripcion de sonda: ')))
        print (sonda.buscarSonda())
        sonda.imprimirSonda()
        objetoCliente=Cliente("tigo","test")
        objetoCliente.buscar_cliente()
        #buscar_cliente()

if __name__=='__main__':
        main()
