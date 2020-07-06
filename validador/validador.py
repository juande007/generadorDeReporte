import os
import json
import os.path
import re
import subprocess
from os import path
from datetime import datetime
#control shift /  para comentar todo

#
# $destination_folder="C:\gemalto\scripts"
# cd $destination_folder
# .\variables.ps1
#
# difernciaStandar = 50
# tiempoIncioNxClient = 10
class Issues ():
    def __init__(self, codigo, issuesABuscar, erroresContados, numeroErroresActual, disparador):

        self.codigo = codigo
        self.issuesABuscar = issuesABuscar
        self.erroresContados = erroresContados
        self.numeroErroresActual = 0
        self.disparador = disparador
        self.diferencia = 0


    def diferencias (self):
        self.diferencia = self.erroresContados - self.numeroErroresActual


class Validador ():

    def __init__(self):
        self.rutaLog = 'NxClient.log'
        self.nombreDelArchivo='NxClient.log'
        self.listDeIssues = []
        #$Global:source_folder="C:\Users\Admin\Desktop\software\DINSTALL\"

        destination_folder = "C:\gemalto\scripts"
        aplication_name = "NxClient.exe"
        #$Global:startup_folder="C:\Users\Admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"
        self.service_name = "NxClient"

        #Ruta de desarrollo
        #self.aplication_folder = "C:\Users\Admin\AppData\Local\Swiss Mobility Solutions\NxClient"
        self.aplication_folder = "C:/thales/scripts/"

        #Ruta Sondas MC
        self.aplication_folderMC = "C:\Users\AdminQoS\AppData\Local\Swiss Mobility Solutions\NxClient"

        #Ruta oficial
        #$Global:aplication_folder="C:\Program Files\Swiss Mobility Solutions\NxClient"
        aplication_exe_folder = "C:\Program Files\Swiss Mobility Solutions\NxClient"
        aplication_exe_folderB = "C:\Program Files (x86)\Swiss Mobility Solutions\NxClient"

    def escribirLog(self,log):
        archivo = self.aplication_folder + self.service_name + ".log"

        if path.isfile(archivo):
            print ("Is it File")
            now = datetime.utcnow()
            date_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            with open(archivo, "a") as f:
                f.write("\n"+date_time+" - "+str(log))
        else:
             print ("it is not a File")


    # if Test-Path $fileToCheck -PathType leaf
    #           Write-Host "La ruta es "$fileToCheck
    #           Add-Content -Path $aplication_folder$service_name".log" -Exclude "help*" -Value text
    # else
    #           Write-Host "La ruta es "
    #           Add-Content -Path $aplication_folderMC$service_name".log" -Exclude "help*" -Value text

    # def leerListaErrores():
    #
    # Write-Host $destination_folder"\listaErrores.txt"
	# get-content -Path $destination_folder"\listaErrores.txt" | foreach {
	# 	$linea = $_
	# 	if ($linea -ne "") {
	# 		$script:ListaDeErrores.Add($linea)
	# 		$script:numeroDeErroresActual.Add("0")
	# 		$script:numeroDeErroresOld.Add(0)
	# 		$script:contadores.Add(0)

# def obtenerErrores_Anteriores():
# {
# 	$contador=0
# 	Write-Host $destination_folder"\dbErrores.txt"
# 	get-content -Path $destination_folder"\dbErrores.txt" | ForEach {
# 		$numeroDeErroresAntes = $_
# 		if ($numeroDeErroresAntes -ne '*') {
# 			$script:numeroDeErroresOld[$contador]=$numeroDeErroresAntes
# 		}else {
# 		    Write-Host "No hay errores"
# 		}
# 		$contador=$contador+1
#
# 	}
# 	$numeroDeErroresOld
# }

    def leer_errores (self, ruta):
        with open(ruta) as file:
            issues_json = json.load(file)
            for issueOBJ in issues_json ['issues']:
                self.listDeIssues.append (Issues(issueOBJ['codigo'], issueOBJ['issuesABuscar'], issueOBJ['erroresContados'], issueOBJ['numeroErroresActual'], issueOBJ['disparador']))

    def contadorMultiErrores (self):
        archivoLog = open('NxClient.log', "r")
        for lineaDelLog in archivoLog.readlines(): # Este for recorre todas las lineas del archivo nxclient .log
            for issues in self.listDeIssues: # para cada de log, con este FORe recorremos la lista de errores y buscamos el error en la linea
                x = re.search(issues.issuesABuscar, lineaDelLog)
                if x:
                    issues.numeroErroresActual +=1

        print ('Se encontro el error '+ str(issues.issuesABuscar) + 'La sumatoria de errores es'+ str(issues.numeroErroresActual))
        archivoLog.close()

        for issues in self.listDeIssues:


            # print('Errores contados = '+ str(issues.erroresContados) + 'Errores Actuales = '+ str(issues.numeroErroresActual))
            # issues.diferencia = int(issues.numeroErroresActual) - int(issues.erroresContados)

            ruta = "issues.json"
        with open(ruta) as file:
            issues_jsonB = json.load(file)
            for issueOBJB in issues_jsonB ['issues']:
                for issues in self.listDeIssues:
                    if issueOBJB['codigo'] == issues.codigo:
                        issueOBJB['numeroErroresActual']=issues.erroresContados
                        issueOBJB['erroresContados']=issues.numeroErroresActual
                        print('Errores contados: '+str(issues.erroresContados))
                        print(issueOBJB['codigo'] +" Errores Contados:"+ str(issueOBJB['erroresContados']) + "errores contados en objeto"+ str(issues.numeroErroresActual))
            print(issues_jsonB)


        a_file = open("issues.json", "w")
        json.dump(issues_jsonB, a_file)
        a_file.close()


    def tareas (self):
        for issues in self.listDeIssues:
            issues.diferencias()
            print ('Para el error '+ str(issues.codigo)+' la diferenciaes '+ str(issues.diferencia))

    def reiniciarSonda (self):

        for issues in self.listDeIssues:
            issues.diferencias()

            if issues.diferencia > issues.disparador :
                print ('Correcto, disparador es: ' + str(issues.disparador) + ' La diferencia es :' + str(issues.diferencia))
                subprocess.call("shutdown -r")
            else:
                print ('Paila papa, disparador es: ' + str(issues.disparador) + ' La diferencia es :' + str(issues.diferencia))



        #Validar por medio del log si  nxClient
        #Reiniciar NxClient
        #Si la diferencia es mayor al disparador entonces reinicia la Sondas
        #Hacer que el script inicie a la vesz que inicia Windows
        #Colocar dos tareas programadas para que inicie el validador

        # print (issues.codigo +': '+ str(issues.numeroErroresActual))
        # issues.erroresContados =  issues.numeroErroresActual - issues.erroresContados
        # print (issues.codigo +': '+ str(issues.numeroErroresActual))












                #print("El contador es igual a: " + x + " para el error " + issue.codigo)

    #     if (Test-Path $fileLog -PathType leaf){
    #         Write-Host "Ruta de los logs"$fileLog
    #     }
    #     else {
    #         $fileLog = $aplication_folderMC+$service_name+".log"
    #         Write-Host "Ruta de los logs"$fileLog
    #     }
    #
    #
    # get-content -Path $fileLog | foreach {
	# 	$linea = $_
	# 	for($i=0;$i -lt $ListaDeErrores.count;$i++){
	# 		if ($linea -like $ListaDeErrores[$i].ToString()) {
	# 	      		$script:Contadores[$i]=$Contadores[$i]+1
	# 		}
	# 	}
	# }
#
# 	for($i=0;$i -lt $ListaDeErrores.count;$i++){
# 		Write-Host "Numero de Errores "$Contadores[$i]" para el error: "$ListaDeErrores[$i]
# 	}
#     actualizarErrores
# }

    def holamundo(self):
        print ('Hola Mundo')

def main():

    validador = Validador()
    validador.escribirLog("Iniciando validador...")
    ruta = "issues.json"
    #validador.leer_errores(ruta)
    #validador.contadorMultiErrores()
    validador.tareas()
    validador.reiniciarSonda()
    validador.escribirLog("Finalizando validador...")


if __name__=='__main__':
    main()
