import getpass
import shutil
import os
import json
USER_NAME = getpass.getuser()

class Instalador ():

    def instalador(self):
        rutaValidador = "C:/thales/scripts/"
        if not os.path.exists(rutaValidador):
            os.makedirs(rutaValidador)

        shutil.copy("validador.py", rutaValidador)
        print("la ruta que va a crear es " + rutaValidador )
        rutaTareaProgramada = "C:/thales/scripts/validador.py"

        if rutaTareaProgramada == "":
            rutaTareaProgramada = os.path.dirname(os.path.realpath(__file__))
        rutaArchivoDeIniciacion = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        with open(rutaArchivoDeIniciacion + '\\' + "inicia_validador.bat", "w+") as bat_file:
                bat_file.write(r'C:\python27\python.exe %s' % rutaTareaProgramada)

        rutaValidador = "C:/thales/scripts/"
        usuario = getpass.getuser()
        rutaArchivoLog = "C:/Users/" +usuario+ "\AppData\Local\Swiss Mobility Solutions\NxClient\NxClient.log"

        f = open("C:/thales/scripts/validador.log", "w")
        f. close()
        print ("Se creo archivo log con exito")

        ruta_File_validador_log = "C:/thales/scripts/validador.log"

        if os.path.isfile(rutaArchivoLog):
            print ("la ruta escrita en config.json es: "+ rutaArchivoLog)
        else:
            print("No se pudo encontrar ningun archivo .log")

        print ('La ruta es: '+ str(rutaArchivoLog))

        ruta_File_exe = "C:\Program Files\Swiss Mobility Solutions\NxClient\NxClient.exe"
        ruta_exe_dos = "C:\Program Files (x86)\Swiss Mobility Solutions\NxClient\NxClient.exe"

        if os.path.isfile(ruta_File_exe):
            print ("la ruta escrita en config.json es: "+ ruta_File_exe)

        elif os.path.isfile(ruta_exe_dos):
            print ("la ruta escrita en config.json es: "+ ruta_exe_dos)
            ruta_File_exe = ruta_exe_dos
        else:
            print("No se pudo encontrar ningun archivo .exe")

        print ('La ruta es: '+ str(ruta_File_exe))

        ruta_file_issues = "C:/thales/scripts/issues.json"

        config = {}
        config ['Configuraciones'] =[]
        config ['Configuraciones'].append({
        'Ruta_File_Log': rutaArchivoLog,
        'Ruta_File_exe': ruta_File_exe,
        'Ruta_File_issues_json':ruta_file_issues,
        'Ruta_File_validador_log':ruta_File_validador_log
        })

        archivoConfig = 'config.json'
        with open(os.path.join(rutaValidador, archivoConfig), 'w') as file:
            json.dump(config, file, indent=4)

        print ("Guardado con exito")

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
        "disparador": 3
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

        reinicios = {}
        reinicios ['Reinicio'] = []
        reinicios ['Reinicio'].append({
        "horaUltimoReinicio": 0,
        "fechaUltimoReinicio": 0,
        "contadorReinicios": 0
        })

        rutaValidador = "C:/thales/scripts/"
        archivoReinicios = 'reinicios.json'
        with open(os.path.join(rutaValidador, archivoReinicios), 'w') as file:
            json.dump(reinicios, file, indent=4)

def main():
    install = Instalador ()
    install.instalador()
if __name__=='__main__':
    main()
