import json
import os

class Sonda (object):
    clientID = str()
    nombre = str()
    descripcion = str()

    def __init__(self,clientID):
        self.clientID = clientID
        self.data = {}

    #Esta funcion crea una sonda con su respectivo id
    def agregarSonda(self):
        self.data ['nuevaSonda']= []
        self.data['nuevaSonda'].append({
        'ID Sonda:': self.clientID})
        return 'El id de la sonda es %s '%(self.data)

    #Esta funcion agrega un nombre a la sonda que estamos creando guardandolo en un archivo json
    def agregarNombre(self,nombre):
        self.data ['nuevoNombre']= []
        self.data ['nuevoNombre'].append({
        'Nombre sonda: ': nombre
        })
        return "El nombre de la Sonda es %s" %(self.data)
    #Esta funcion agrega la descripcion de la sonda a crear en el archivo json
    def agregarDescripcion(self,descripcion):
        self.data ['nuevaDescripcion']= []
        self.data ['nuevaDescripcion'].append({
        'Descripcion sonda: ': descripcion
        })
        return "Descripcion de sonda: %s" %(self.data)
    #Esta funcion nos permite guardar una sonda en una carpeta y archivo json nombradas con su id, guardandola con su respectivo id, nombre y descripcion
    def imprimirSonda(self):

        dir = './tigoco/clientNx/clientID/' +self.clientID
        os.mkdir(str(dir))
        file_name = str(self.clientID)+'.json'
        with open(os.path.join(dir, file_name), 'w') as file:
            json.dump(self.data, file, indent=4)
        #Aqui se hace la operacion que permite crear una carpeta de incidenetes en cada Sonda creada
        file_inc = '/Incidentes'
        direc = './tigoco/clientNx/clientID/' +self.clientID  +file_inc
        os.mkdir(direc)
        return

    def buscarSonda(self):
        existe="No existe"
        return existe

    def editarSonda():
        return "Sin implentar"
    def eliminarSonda():
        return "Sin implementar"

    def prueba(self):
        print 'El id de la sonda es %s '%(self.clientID)

def main():
    sonda = Sonda(raw_input('Ingrese Id de la nueva sonda: '))
    print (sonda.agregarSonda())
    print (sonda.agregarNombre(raw_input('Ingrese el nombre de la sonda: ')))
    print (sonda.agregarDescripcion(raw_input('Descripcion de sonda: ')))
    sonda.imprimirSonda()


if __name__=='__main__':
    main()
