#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import os.path
import re
import subprocess
import time
from os import path
from datetime import datetime

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
        self.rutaNxClientIssues =""
        self.validarErrores= False
        self.primerconteo = False


    def escribirLog(self,log):
        archivo = self.rutaNxClientLog

        if path.isfile(archivo):
            now = datetime.utcnow()
            date_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            with open(archivo, "a") as f:
                f.write("\n"+date_time+" - "+str(log))
        else:
             print ("No se encontró el archivo: "+archivo)

    def leer_errores (self):
        with open(self.rutaNxClientIssues, 'r') as file:
            issues_json = json.load(file)
            for issueOBJ in issues_json ['issues']:
                self.listadoDeIssues.append (Issues(issueOBJ['codigo'], issueOBJ['issuesABuscar'], issueOBJ['erroresContados'], issueOBJ['numeroErroresActual'], issueOBJ['disparador']))

    def contador_Multi_Errores (self):
        filename = self.rutaNxClientLog
        file = open(filename,'r')
        while 1:
                where = file.tell()
                line = file.readline()
                if not line: #Si no hay una nueva linea, se realiza el siguiente script
                    if self.validarErrores:
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
                                        self.tareas()
                                        self.validarErrores= False
                                        self.primerconteo= True

                    time.sleep(1)
                    try: file.seek(where)
                    except IOError: file.seek(0)
                else:
                    #print line
                    for issues in self.listadoDeIssues: # para cada de log, con este FORe recorremos la lista de errores y buscamos el error en la linea
                        x = re.search(issues.issuesABuscar, line)
                        if x:
                            self.validarErrores= True
                            issues.numeroErroresActual +=1
                            print ("Error encontrado: "+str(issues.codigo) + ' = '+ str(issues.numeroErroresActual))

    def tareas (self):
        for issues in self.listadoDeIssues:
            #print (str(issues.codigo)+' diferencia='+ str(issues.diferencia))
            issues.diferencias()
        self.reiniciarSonda()


    def reiniciarSonda (self):
        for issues in self.listadoDeIssues:
            issues.diferencias()
            if issues.diferencia > issues.disparador :
                self.escribirLog("Reiniciando...")
                subprocess.call("shutdown -r")

    def leer_Archivo_Config (self):
        f = open(self.rutaValidadorFolder+ "config.json", "r")
        contenidoArchivoConfig = f.read()
        jsondecoded = json.loads(contenidoArchivoConfig)

        for lineaArchivoConfig in jsondecoded["Configuraciones"]:
            self.rutaNxClientLog  = lineaArchivoConfig["Ruta_File_Log"]
            print("Ruta log: " + self.rutaNxClientLog)

        for lineaArchivoConfig in jsondecoded["Configuraciones"]:
            self.rutaNxClientExe = lineaArchivoConfig["Ruta_File_exe"]
            print("Ruta exe: " + self.rutaNxClientExe)

        for lineaArchivoConfig in jsondecoded["Configuraciones"]:
            self.rutaNxClientIssues = lineaArchivoConfig["Ruta_File_issues_json"]
            print("Ruta issues: " + self.rutaNxClientIssues)

def main():

    validador = Validador()
    validador.escribirLog("Iniciando validador...")
    validador.leer_Archivo_Config()
    validador.leer_errores()
    validador.contador_Multi_Errores()
    validador.escribirLog("Finalizando validador...")

if __name__=='__main__':
    main()
