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
        shutil.copy("issues.json", rutaValidador)
        print("la ruta que va a crear es " + rutaValidador )
        rutaTareaProgramada = "C:/thales/scripts/validador.py"

        if rutaTareaProgramada == "":
            rutaTareaProgramada = os.path.dirname(os.path.realpath(__file__))
        rutaArchivoDeIniciacion = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        with open(rutaArchivoDeIniciacion + '\\' + "inicia_validador.bat", "w+") as bat_file:
                bat_file.write(r'start "" %s' % rutaTareaProgramada)

        rutaValidador = "C:/thales/scripts/"
            #rutaArchivoLog = "C:\Users\AdminQoS\AppData\Local\Swiss Mobility Solutions\NxClient.log"
        rutaArchivoLog = "C:\Users\AdminQoS\AppData\Local\Swiss Mobility Solutions\NxClient\NxClient.log"
        ruta_logs_Dos = "C:\Users\Niko\AppData\Local\Swiss Mobility Solutions\NxClient\Nxclient.log"
        ruta_logs_Tres = "C:\Users\AdminQoS\AppData\Local\Swiss Mobility Solutions\NxClient\NxClient.log"

        if os.path.isfile(rutaArchivoLog):
            print ("la ruta escrita en config.json es: "+ rutaArchivoLog)
        elif os.path.isfile(ruta_logs_Dos):
            print ("la ruta escrita en config.json es: "+ ruta_logs_Dos)
            rutaArchivoLog = ruta_logs_Dos
        elif os.path.isfile(ruta_logs_Tres):
            print ("la ruta escrita en config.json es: "+ ruta_logs_Tres)
            rutaArchivoLog = ruta_logs_Tres
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
        'Ruta_File_issues_json':ruta_file_issues
        })

        archivoConfig = 'config.json'
        with open(os.path.join(rutaValidador, archivoConfig), 'w') as file:
            json.dump(config, file, indent=4)

        print ("Guardado con exito")

#C:\gemalto\scripts
def main():
    install = Instalador ()
    install.instalador()
if __name__=='__main__':
    main()
