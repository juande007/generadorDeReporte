import json
import os
from os import remove
from shutil import rmtree


def menu_cliente():

    print('1- Editar un cliente: ')
    print('2- Eliminar un cliente: ')
    opcion = (raw_input('Seleccione la tarea a realizar: '))

    if opcion == '1':
        editar_cliente()
    else:
        eliminar_cliente()


def mostrar_clientes():
    print('L I S T A  D E  C L I E N T E S')
    dir = "./Clientes"
    contenido = os.listdir(dir)
    print(contenido)


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
    with open(os.path.join(dir, file_name), 'w') as file:
        json.dump(clientJson, file, indent=4)

    print ("Se guardo nuevo cliente: " + nuevo_cliente)


def editar_cliente():


    dir_Clientes = "./Clientes/"
    nombre_cliente = str(raw_input('Ingrese nombre del cliente: '))
    nuevo_nombre = str(raw_input('Ingrese el nuevo nombre: '))
    path_cliente =  dir_Clientes+nombre_cliente
    clientJson = {}
    clientJson ['nombreDeCliente'] =[]
    clientJson ['nombreDeCliente'].append({
    'nombre_corto ': nuevo_nombre
    })

    path_nombre = dir_Clientes+nuevo_nombre
    file_cliente_old = path_nombre + '/' + nombre_cliente+".json"
    file_cliente_new = path_nombre + '/' + nuevo_nombre+".json"
    os.rename(path_cliente,path_nombre) #rename de directory
    os.rename(file_cliente_old,file_cliente_new)


    with open(str(file_cliente_new), 'r') as file:
        json.load(file)
        file.close()
        print("archivo a crear :"+file_cliente_new)
        print("Nombre del anterior archivo:"+file_cliente_old)

    with open(str(file_cliente_new), 'w') as file:
        json.dump(clientJson, file, indent=4)

def eliminar_cliente():

    carpeta= (raw_input('Escriba el nombre de la carpeta a eliminar: '))
    rmtree('./Clientes/'+ carpeta,carpeta)


def main():

    agregar_Cliente()
    mostrar_clientes()
    menu_cliente()

    #editar_cliente()
    #eliminar_cliente()
if __name__=='__main__':
    main()
