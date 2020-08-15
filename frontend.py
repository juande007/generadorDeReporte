import eel, os, random
import GeneradorDeReporte
from incidents import Incidents



eel.init('web')

@eel.expose
def pick_file(comando):
    reporte = GeneradorDeReporte
    sondas = reporte.tarea(comando)
    print(comando)
    resultado=''
    for element in sondas:
        resultado=resultado+"<div class='boton_clientes'>"+element+"</div>"
    return resultado

@eel.expose
def clientes():
    reportes = GeneradorDeReporte
    listadoClientes = reportes.listadoDeClientes()
    resultado=''
    for element in listadoClientes:
        resultado=resultado+"<div class='boton_clientes' onclick=prueba('"+element+"')>"+element+"</div>"

    print ("el objet es!"+str(type(resultado)))
    print (resultado)
    return resultado

@eel.expose
def listaIncidentes():
    incidentes = Incidents()
    mostrarIncidents = incidentes.mostrarIncidents()
    inc =''
    for element in mostrarIncidents:
        inc = inc + "<div class='boton_clientes'>"+element+"</div>"
    print (inc)
    print("entro aqui")
    return inc

eel.start('frontend.html')
