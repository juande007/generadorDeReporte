#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import os.path
import re
import subprocess
import time
import shutil
import datetime as elTiempo
from os import path
from datetime import datetime
from datetime import datetime as date


class Issues ():
    def __init__(self, codigo, issuesABuscar, erroresContados, numeroErroresActual, disparador):

        self.codigo = codigo
        self.issuesABuscar = issuesABuscar
        self.erroresContados = erroresContados
        self.numeroErroresActual = 0
        self.disparador = disparador
        self.diferencia = 0
    def diferencias (self):
        self.diferencia = self.numeroErroresActual - self.erroresContados

class Validador ():

    def __init__(self):
        self.rutaLog = 'NxClient.log'
        self.nombreDelArchivo='NxClient.log'
        self.listadoDeIssues = []
        self.rutaValidadorFolder= "C:/thales/scripts/"
        self.rutaNxClientExe = ""
        self.rutaNxClientLog = ""
        self.ruta_File_validador_log = ""
        self.rutaNxClientIssues =""
        self.validarErrores= False
        self.primerConteo = True
        self.day= date.today().strftime("%A")
        self.fechaUltimoReinicio = ""
        self.horaUltimoReinicio = ""
        self.cdReinicios = 0
        self.reiniciar = False
        self.diferenciaUltimoRegistroActual = 0

    def escribirLog(self,log):
        # archivo = "C:/thales/scripts/validador.log"

        if path.isfile(self.ruta_File_validador_log):
            now = datetime.utcnow()
            date_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            with open(self.ruta_File_validador_log, "a") as f:
                f.write("\n"+date_time+" - "+str(log))
                f.close()
        else:
             print ("No se encontró el archivo: ")

    def leer_errores (self):
        with open(self.rutaNxClientIssues, 'r') as file:
            issues_json = json.load(file)
            for issueOBJ in issues_json ['issues']:
                self.listadoDeIssues.append (Issues(issueOBJ['codigo'], issueOBJ['issuesABuscar'], issueOBJ['erroresContados'], issueOBJ['numeroErroresActual'], issueOBJ['disparador']))

    def contador_Multi_Errores (self):
        filename = self.rutaNxClientLog
        file = open(filename,'r')
        while 1:
                #self.escribirLog("Nuevo ciclo")
                print(".")
                where = file.tell()
                line = file.readline()
                if not line: #Si no hay una nueva linea, se realiza el siguiente script
                    if self.primerConteo:   #Tras realizado el primer conteo, en este if se valida si hubo rotado de log.
                        self.primerConteo = False
                        for issues in self.listadoDeIssues:
                            if issues.numeroErroresActual < issues.erroresContados:
                                issues.erroresContados = 0

                    if self.validarErrores:
                        print("validando errore")
                        with open(self.rutaNxClientIssues, "r") as files:
                            issues_jsonB = json.load(files)
                            for issueOBJB in issues_jsonB ['issues']:
                                for issues in self.listadoDeIssues:
                                    if issueOBJB['codigo'] == issues.codigo:
                                        issueOBJB['numeroErroresActual']=issues.numeroErroresActual
                                        issueOBJB['erroresContados']=issues.numeroErroresActual
                                        archivoIssuesActualizar = open(self.rutaNxClientIssues, "w")
                                        json.dump(issues_jsonB, archivoIssuesActualizar)
                                        archivoIssuesActualizar.close()
                                        self.escribirLog(str(issueOBJB['codigo'])+":"+str(issueOBJB['numeroErroresActual']))
                            self.tareas()
                            self.validarErrores= False #bool

                    time.sleep(1)
                    self.rotado_de_logs()
                    try: file.seek(where)
                    except IOError: file.seek(0)
                else:
                    print line
                    for issues in self.listadoDeIssues: # para cada de log, con este FORe recorremos la lista de errores y buscamos el error en la linea
                        print("Error a buscar "+str(issues.issuesABuscar))
                        x = re.search(issues.issuesABuscar, line)
                        if x:
                            self.validarErrores= True
                            issues.numeroErroresActual +=1
                            print ("Contador, issue Id "+str(issues.codigo) + ' = '+ str(issues.numeroErroresActual))
                        else:
                            print("error no encontrado")

    def tareas (self):
        for issues in self.listadoDeIssues:
            issues.diferencias()
        self.reiniciarSonda()

    def reiniciarSonda (self):
        for issues in self.listadoDeIssues:
            issues.diferencias()
            if issues.diferencia > issues.disparador :
                fechaActual = elTiempo.datetime.now()
                horaActual = elTiempo.datetime.now()

                a = open(self.rutaValidadorFolder + "reinicios.json", "r")
                contenidoArchivoReinicio = a.read()
                jsondecoded = json.loads(contenidoArchivoReinicio)

                for lineaArchivoReinicio in jsondecoded["Reinicio"]:
                    if lineaArchivoReinicio["horaUltimoReinicio"] == 0:
                        self.horaUltimoReinicio = horaActual
                        self.fechaUltimoReinicio = fechaActual
                    else:
                        self.horaUltimoReinicio = datetime.strptime(lineaArchivoReinicio["horaUltimoReinicio"], '%Y-%m-%d %H:%M:%S.%f')
                        self.fechaUltimoReinicio=datetime.strptime(lineaArchivoReinicio["fechaUltimoReinicio"], '%Y-%m-%d %H:%M:%S.%f')
                    self.contadorReinicios = lineaArchivoReinicio["contadorReinicios"]

                print("Reinicio "+ str(self.horaUltimoReinicio))
                print("Fecha "+ str(self.fechaUltimoReinicio))
                print("Contador de reinicios "+ str(self.contadorReinicios))


                self.diferenciaUltimoRegistroActual = (self.horaUltimoReinicio - horaActual).seconds
                print("Tiempo entre reinicios: "+self.diferenciaUltimoRegistroActual+".seconds.................................................")

                res = self.diferenciaUltimoRegistroActual
                tiempo_Entre_Reinicios = 180
                if res <= tiempo_Entre_Reinicios:
                    self.cdReinicios +=1
                    with open("C:/thales/scripts/reinicios.json", "r") as files:
                        reiniciosJson = json.load(files)
                        for reinicioJSON in reiniciosJson ["Reinicio"]:
                            reinicioJSON["contadorReinicios"] =self.cdReinicios
                            reinicioJSON["horaUltimoReinicio"]=str(self.horaUltimoReinicio)
                            reinicioJSON["fechaUltimoReinicio"]=str(self.fechaUltimoReinicio)
                            archivoReiniciosActualizar = open("C:/thales/scripts/reinicios.json", "w")
                            json.dump(reiniciosJson, archivoReiniciosActualizar)
                            archivoReiniciosActualizar.close()
                else print("Debe haber una diferencia de tres minutos....")

                if res <= tiempo_Entre_Reinicios and self.cdReinicios <= 3:
                    self.escribirLog("Reiniciando cumple luego menos de una hora y menos de 3 reinicios.........................................")
                    print("Reiniciando cumple luego menos de una hora y menos de 3 reinicios.........................................")
                    # subprocess.call("shutdown -r -f")
                    # break
                elif res >= 180 and self.cdReinicios > 3:
                        self.cdReinicios = 0
                        self.escribirLog("*********************Reiniciando luego de 3 horas sin reiniciar o algun error")
                        print("********************ENTRO AL SEGUNDO IF DE REINICIOS********************")
                time.sleep(2)
                        # subprocess.call("shutdown -r -f")
                        # break
# actual1 = datetime.datetime.now()
# actual2 = datetime.datetime.now()
#
# diferencia = actual2 - actual1
#
# print(diferencia.days)
# print(diferencia.seconds)
#
# print(diferencia.total_seconds())
                # self.escribirLog(str(issues.diferencia) +" es mayor que "+ str(issues.disparador))
                # self.escribirLog("Reiniciando...")
                # subprocess.call("shutdown -r -f")



    def leer_Archivo_Config (self):
        f = open(self.rutaValidadorFolder+ "config.json", "r")
        contenidoArchivoConfig = f.read()
        jsondecoded = json.loads(contenidoArchivoConfig)

        for lineaArchivoConfig in jsondecoded["Configuraciones"]:
            self.rutaNxClientLog  = lineaArchivoConfig["Ruta_File_Log"]
            self.rutaNxClientExe = lineaArchivoConfig["Ruta_File_exe"]
            self.rutaNxClientIssues = lineaArchivoConfig["Ruta_File_issues_json"]
            self.ruta_File_validador_log = lineaArchivoConfig["Ruta_File_validador_log"]
            print("Ruta log: " + self.rutaNxClientLog)
            print("Ruta exe: " + self.rutaNxClientExe)
            print("Ruta issues: " + self.rutaNxClientIssues)
            print("Ruta validador.log: " + self.ruta_File_validador_log)

    def administracion_De_Tiempo(self):
        self.leer_Archivo_Config()
        self.escribirLog("Iniciando validador...")
        self.leer_errores()
        self.contador_Multi_Errores()
        self.escribirLog("Finalizando validador...")

    def rotado_de_logs(self):
        dayNew =date.today().strftime("%A")
        if self.day == str(dayNew):
            self.day = str(date.today().strftime("%A"))

        else:
            self.day = str(date.today().strftime("%A"))
            print("Hacemos el rotado de logs")
            print("El dia es diferente "+ self.day)
            rutaValidador = "C:/thales/scripts/validador.log"+"."+self.day
            shutil.copy("C:/thales/scripts/validador.log", rutaValidador)
            with open("C:/thales/scripts/validador.log", 'w'):
                pass

def main():

    validador = Validador()
    validador.administracion_De_Tiempo()
    # validador.leer_Archivo_Config()
    # validador.escribirLog("Iniciando validador...")
    # validador.leer_errores()
    # validador.contador_Multi_Errores()
    # validador.escribirLog("Finalizando validador...")

if __name__=='__main__':
    main()
