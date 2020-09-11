import eel, os, random
import GeneradorDeReporte
from incidents import Incidents
# from generador_word import datosReporte
from generador_word import Reportes



eel.init('web')

@eel.expose
def pick_file(comando):

    incidentes = Incidents()
    mostrarIncidents = incidentes.mostrarIncidents()
    inc =''

    reporte = GeneradorDeReporte
    sondas = reporte.tarea(comando)
    print(comando)
    resultado=''
    for element in sondas:
        resultado=resultado+"<div><li id="+element+">"+element+"</li>"
        for issueElmente in mostrarIncidents:
            resultado=resultado+"<li class='boton_sondas' onclick= adicionarSondaAReporte('"+element+"','"+issueElmente+"') >"+issueElmente+"</li>"
    resultado=resultado+"</div>"

    return resultado


@eel.expose
def clientes():
    reportes = GeneradorDeReporte
    listadoClientes = reportes.listadoDeClientes()
    resultado=''
    for element in listadoClientes:
        resultado=resultado+"<div class='boton_clientes' id="+element+" onclick=buscarCliente('"+element+"')>"+element+"</div>"

    print ("el objet es!"+str(type(resultado)))
    print (resultado)
    return resultado

@eel.expose
def listaIncidentes():
    incidentes = Incidents()
    mostrarIncidents = incidentes.mostrarIncidents()
    inc =''
    for element in mostrarIncidents:
        inc = inc + "<div class='boton_issues' id="+element+" onclick=adicionarIssueAReporte('"+element+"')>"+element+"</div>"
    print (inc)
    print("entro aqui")
    return inc
@eel.expose
def imprimirSonda(datosSonda):
    print("Resultadp desde python "+str(datosSonda))
    li = list(datosSonda.split(";"))
    for element in li:
        print element
    reportes = Reportes()
    datosReporte = reportes.datosReporte(li)

eel.start('frontend.html')
