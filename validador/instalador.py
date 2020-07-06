import getpass
import shutil
import os
import json
USER_NAME = getpass.getuser()

class Instalador ():

    def instalador(self):

        path_validador = "C:/thales/scripts"

        if not os.path.exists(path_validador):
            os.makedirs(path_validador)
        shutil.copy("validador.py", path_validador)
        shutil.copy("issues.json", path_validador)

        config = {}
        config ['Configuraciones'] =[]
        config ['Configuraciones'].append({
        'Ruta_File_Log': 'nxClient.log',
        'Ruta_File_exe': 'nxClient.exe'
        })

        file_name = 'config.json'
        with open(os.path.join(path_validador, file_name), 'w') as file:
            json.dump(config, file, indent=4)

        print ("Guardado con exito")


    file_path = "C:/thales/scripts/validador.py"

    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "inicia_validador.bat", "w+") as bat_file:
            bat_file.write(r'start "" %s' % file_path)

#C:\gemalto\scripts
def main():
    install = Instalador ()
    install.instalador()
if __name__=='__main__':
    main()
