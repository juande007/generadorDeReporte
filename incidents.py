import os
import json


def incidentes ():
    data = {}
    #Aqui solicitamos los datos necesarios para crear el archivo Json de Incidentes en las Sondas
    name_incident = (raw_input('Nombre del incidente: '))
    desc_incident = (raw_input('Descripcion de incidente: '))
    analisis_incident = (raw_input('Analisis: '))
    root_incident = (raw_input('Rot cause: '))
    workar_incident = (raw_input('Workaround: '))
    rec_incident = (raw_input('Recomendacion: '))
    #Se crea una lista que capte los datos y los guarde
    data ['nuevoIncident']= []
    data['nuevoIncident'].append({
    'Nombre: ': name_incident,
    'Descripcion: ': desc_incident,
    'Analisis: ': analisis_incident,
    'Root Cause: ': root_incident,
    'Workaround: ': workar_incident,
    'Recomendacion: ': rec_incident
    })
    #Este codigo guarda en archivo en la carpeta de Incidentes
    dir = '.\Incidentes'
    file_name = str(name_incident)+'.json'
    with open(os.path.join(dir, file_name), 'w') as file:
            json.dump(data, file, indent=4)


def main():
    incidentes ()


if __name__=='__main__':
    main()
