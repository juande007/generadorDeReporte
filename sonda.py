import json

class Sonda (object):
    clientID = str()
    nombre = str()
    descripcion = str()

    def __init__(self,clientID):
        self.clientID = clientID

    def agregarSonda(self):
        data = {}
        data ['nuevaSonda']= []
        data['nuevaSonda'].append({
        'ID Sonda:': self.clientID})
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
        return 'El id de la sonda es %s '%(self.clientID)
    def editarSonda():
        return "Sin implentar"
    def eliminarSonda():
        return "Sin implementar"

    def prueba(self):
        print 'El id de la sonda es %s '%(self.clientID)

def main():
    sonda = Sonda(raw_input('Ingrese Id de la nueva sonda: '))
    print (sonda.agregarSonda())

if __name__=='__main__':
    main()
