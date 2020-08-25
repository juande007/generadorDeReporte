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
        self.horaUltimoErrorDetectado = ""
        self.horaUltimoReinicio = ""
        self.segundosEntreUltimoErrorDetectado = ""
        self.cdReinicios = 0
        self.reiniciar = False
        self.primerReinicio = False
        self.diferenciaUltimoRegistroActual = 0
        self.rutaReinicios = "C:/thales/scripts/reinicios.json"
        self.tiempo_Entre_Reinicios =120
        self.tiempoDeRecuperacion = 120

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

                where = file.tell()
                line = file.readline()
                if not line: #Si no hay una nueva linea, se realiza el siguiente script
                    if self.primerConteo:   #Tras realizado el primer conteo, en este if se valida si hubo rotado de log.
                        self.primerConteo = False
                        for issues in self.listadoDeIssues:
                            if issues.numeroErroresActual < issues.erroresContados:
                                issues.erroresContados = 0

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
                                        self.escribirLog(str(issueOBJB['codigo'])+":"+str(issueOBJB['numeroErroresActual']))
                            self.tareas()
                            self.validarErrores= False #bool

                    time.sleep(1)
                    self.rotado_de_logs()
                    try: file.seek(where)
                    except IOError: file.seek(0)
                else:
                    for issues in self.listadoDeIssues: # para cada de log, con este FORe recorremos la lista de errores y buscamos el error en la linea
                        x = re.search(issues.issuesABuscar, line)
                        if x:
                            self.validarErrores= True
                            issues.numeroErroresActual +=1
                            print ("Id: "+str(issues.codigo) + ' = '+ str(issues.numeroErroresActual))

    def tareas (self):
        for issues in self.listadoDeIssues:
            issues.diferencias()
        self.reiniciarSonda()

    def reiniciarSonda (self):
        for issues in self.listadoDeIssues:
            issues.diferencias()
            if issues.diferencia >= issues.disparador :
                horaActual = elTiempo.datetime.now()

                a = open(self.rutaValidadorFolder + "reinicios.json", "r")
                contenidoArchivoReinicio = a.read()
                jsondecoded = json.loads(contenidoArchivoReinicio)

                for lineaArchivoReinicio in jsondecoded["Reinicio"]:
                    if lineaArchivoReinicio["horaUltimoReinicio"] == 0:
                        self.horaUltimoReinicio = horaActual
                        self.horaUltimoErrorDetectado = horaActual
                        self.cdReinicios=0
                        self.primerReinicio = True
                    else:
                        self.horaUltimoReinicio = datetime.strptime(lineaArchivoReinicio["horaUltimoReinicio"], '%Y-%m-%d %H:%M:%S.%f')
                        self.horaUltimoErrorDetectado=datetime.strptime(lineaArchivoReinicio["fechaUltimoReinicio"], '%Y-%m-%d %H:%M:%S.%f')
                        self.cdReinicios = lineaArchivoReinicio["contadorReinicios"]
                    self.escribirLog("Reinicio >"+ str(self.horaUltimoReinicio))
                    self.escribirLog("Fecha    >"+ str(self.horaUltimoErrorDetectado))
                    self.escribirLog("Contador de reinicios "+ str(self.cdReinicios))




                self.diferenciaUltimoRegistroActual = (horaActual - self.horaUltimoReinicio  ).seconds
                print("Tiempo entre reinicios: "+ str(self.diferenciaUltimoRegistroActual) +".Seg")

                res = self.diferenciaUltimoRegistroActual
                if res <= self.tiempo_Entre_Reinicios:
                     self.horaUltimoReinicio = horaActual
                     self.horaUltimoErrorDetectado = horaActual
                     if self.primerReinicio:
                        self.cdReinicios +=1
                        self.horaUltimoReinicio = horaActual
                        self.horaUltimoErrorDetectado = horaActual
                        self.primerReinicio = False
                        with open(self.rutaReinicios, "r") as files:
                            reiniciosJson = json.load(files)
                            for reinicioJSON in reiniciosJson ["Reinicio"]:
                                reinicioJSON["contadorReinicios"] =self.cdReinicios
                                reinicioJSON["horaUltimoReinicio"]=str(self.horaUltimoReinicio)
                                reinicioJSON["fechaUltimoReinicio"]=str(self.horaUltimoErrorDetectado)
                                archivoReiniciosActualizar = open(self.rutaReinicios, "w")
                                json.dump(reiniciosJson, archivoReiniciosActualizar)
                                archivoReiniciosActualizar.close()
                     else:
                         with open(self.rutaReinicios, "r") as files:
                              reiniciosJson = json.load(files)
                              for reinicioJSON in reiniciosJson ["Reinicio"]:
                                  reinicioJSON["contadorReinicios"]=lineaArchivoReinicio["contadorReinicios"]
                                  reinicioJSON["horaUltimoReinicio"]=lineaArchivoReinicio["horaUltimoReinicio"]
                                  reinicioJSON["fechaUltimoReinicio"]=str(self.horaUltimoErrorDetectado) #Solo este campo se debe actualizar.
                                  archivoReiniciosActualizar = open(self.rutaReinicios, "w")
                                  json.dump(reiniciosJson, archivoReiniciosActualizar)
                                  archivoReiniciosActualizar.close()

                elif res >= self.tiempo_Entre_Reinicios and self.cdReinicios <= 3:
                    self.escribirLog("Reiniciando, cumple con al menos una hora y menos de 3 reinicios")
                    self.cdReinicios +=1
                    self.horaUltimoReinicio = horaActual
                    self.horaUltimoErrorDetectado = horaActual

                    with open(self.rutaReinicios, "r") as files:
                        reiniciosJson = json.load(files)
                        for reinicioJSON in reiniciosJson ["Reinicio"]:
                            reinicioJSON["contadorReinicios"] =self.cdReinicios
                            reinicioJSON["horaUltimoReinicio"]=str(self.horaUltimoReinicio)
                            reinicioJSON["fechaUltimoReinicio"]=str(self.horaUltimoErrorDetectado)
                            archivoReiniciosActualizar = open(self.rutaReinicios, "w")
                            json.dump(reiniciosJson, archivoReiniciosActualizar)
                            archivoReiniciosActualizar.close()
                    subprocess.call("shutdown -r -f")
                    break
                elif self.cdReinicios > 2:
                        self.segundosEntreUltimoErrorDetectado = (horaActual - self.horaUltimoErrorDetectado ).seconds
                        self.escribirLog("Hora ultimo error detectado: "+str(self.segundosEntreUltimoErrorDetectado)+".seg")
                        if self.segundosEntreUltimoErrorDetectado >= self.tiempoDeRecuperacion:
                            self.cdReinicios = 0
                            self.escribirLog("Reiniciando luego de 3 horas detectar error")
                            self.horaUltimoReinicio = horaActual
                            self.horaUltimoErrorDetectado = horaActual
                            with open(self.rutaReinicios, "r") as files:
                                reiniciosJson = json.load(files)
                                for reinicioJSON in reiniciosJson ["Reinicio"]:
                                    reinicioJSON["contadorReinicios"] =self.cdReinicios
                                    reinicioJSON["horaUltimoReinicio"]=str(self.horaUltimoReinicio)
                                    reinicioJSON["fechaUltimoReinicio"]=str(self.horaUltimoErrorDetectado)
                                    archivoReiniciosActualizar = open(self.rutaReinicios, "w")
                                    json.dump(reiniciosJson, archivoReiniciosActualizar)
                                    archivoReiniciosActualizar.close()
                            subprocess.call("shutdown -r -f")
                            break
                        else:
                            self.horaUltimoErrorDetectado = horaActual
                            self.escribirLog("No debe reiniciar hasta "+str(self.horaUltimoErrorDetectado)+ " segundos sin reinicio")
                            with open(self.rutaReinicios, "r") as files:
                              reiniciosJson = json.load(files)
                              for reinicioJSON in reiniciosJson ["Reinicio"]:
                                  reinicioJSON["contadorReinicios"]=lineaArchivoReinicio["contadorReinicios"]
                                  reinicioJSON["horaUltimoReinicio"]=lineaArchivoReinicio["horaUltimoReinicio"]
                                  reinicioJSON["fechaUltimoReinicio"]=str(self.horaUltimoErrorDetectado) #Solo este campo se debe actualizar.
                                  archivoReiniciosActualizar = open(self.rutaReinicios, "w")
                                  json.dump(reiniciosJson, archivoReiniciosActualizar)
                                  archivoReiniciosActualizar.close()

    def leer_Archivo_Config (self):
        f = open(self.rutaValidadorFolder+ "config.json", "r")
        contenidoArchivoConfig = f.read()
        jsondecoded = json.loads(contenidoArchivoConfig)

        for lineaArchivoConfig in jsondecoded["Configuraciones"]:
            self.rutaNxClientLog  = lineaArchivoConfig["Ruta_File_Log"]
            self.rutaNxClientExe = lineaArchivoConfig["Ruta_File_exe"]
            self.rutaNxClientIssues = lineaArchivoConfig["Ruta_File_issues_json"]
            self.ruta_File_validador_log = lineaArchivoConfig["Ruta_File_validador_log"]

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
            rutaValidador = "C:/thales/scripts/validador.log"+"."+self.day
            shutil.copy("C:/thales/scripts/validador.log", rutaValidador)
            with open("C:/thales/scripts/validador.log", 'w'):
                pass

def main():

    validador = Validador()
    validador.administracion_De_Tiempo()

if __name__=='__main__':
    main()
