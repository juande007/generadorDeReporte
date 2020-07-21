import os
import json

def prueba():
    issue = {}
    issue ['issues'] =[]
    issue ['issues'].append({
    "codigo": "LP",
    "issuesABuscar": "Late packet",
    "numeroErroresActual": 0,
    "erroresContados": 0,
    "disparador": 50
    })
    issue ['issues'].append({
    "codigo": "SF",
    "issuesABuscar": "SIM failure",
    "numeroErroresActual": 0,
    "erroresContados": 0,
    "disparador": 50
    })
    issue ['issues'].append({
    "codigo": "LDLT",
    "issuesABuscar": "Limiting DL traffic of umts",
    "numeroErroresActual": 0,
    "erroresContados": 0,
    "disparador": 30
    })
    issue ['issues'].append({
    "codigo": "SE",
    "issuesABuscar": "SIM PIN required",
    "numeroErroresActual": 0,
    "erroresContados": 0,
    "disparador": 30
    })
    issue ['issues'].append({
    "codigo": "QMI",
    "issuesABuscar": "Couldn't get the name  of the port to send QMI commands",
    "numeroErroresActual": 0,
    "erroresContados": 0,
    "disparador": 30
    })
    issue ['issues'].append({
    "codigo": "GTO",
    "issuesABuscar": "getConnectionToken has timed out 100 times",
    "numeroErroresActual": 0,
    "erroresContados": 0,
    "disparador": 20
    })

    rutaValidador = "C:/thales/scripts/"
    archivoIssues = 'issues.json'
    with open(os.path.join(rutaValidador, archivoIssues), 'w') as file:
        json.dump(issue, file, indent=4)

    print ("Guardado con exito")

def main():
    prueba()
if __name__=='__main__':
    main()
