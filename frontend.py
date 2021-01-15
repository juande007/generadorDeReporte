import eel, os, random
import GeneradorDeReporte
import re
from datetime import datetime
from incidents import Incidents
# from generador_word import datosReporte
from generador_word import Reportes
from sonda import Sonda


class DatosReporte:
    def __init__(self):
        self.cliente = ""

obj = DatosReporte
obj.cliente=""

eel.init('web')
@eel.expose

def pick_file(comando):
    palabra= comando
    patron = re.compile('([a-zA-Z]+)(\s)')
    matcher = patron.search(palabra)
    cliente = matcher.group()
    cliente=cliente.strip()
    obj.cliente=cliente
    incidentes = Incidents()
    mostrarIncidents = incidentes.mostrarIncidents()
    inc =''

    reporte = GeneradorDeReporte
    sondas = reporte.tarea(comando)
    print(comando)
    resultado="<input disabled type='text' id='cliente' value='"+cliente+"'><p>"+cliente+"</p></input>"
    view=True
    for element in sondas:
        resultado=resultado+"<div id=sonda-"+element+">"
        for issueElmente in mostrarIncidents:
            if view:
                resultado=resultado+"<li class='boton_sondas_A' onclick= adicionarSondaAReporte('"+element+"','"+issueElmente+"') >"+element+" - "+issueElmente+"</li>"
            else:
                resultado=resultado+"<li class='boton_sondas_B' onclick= adicionarSondaAReporte('"+element+"','"+issueElmente+"') >"+element+" - "+issueElmente+"</li>"
        if view:
            view=False
        else:
            view=True
        resultado=resultado+"</div>"
    return resultado


@eel.expose
def clientes():
    reportes = GeneradorDeReporte
    listadoClientes = reportes.listadoDeClientes()
    resultado="<ul class='boton_clientes'>"
    for element in listadoClientes:
        resultado=resultado+"<li><a id="+element+" onclick=buscarCliente('"+element+"')>"+element+"</a></li>"
    resultado=resultado+"</ul>"

    #print (resultado)
    return resultado

@eel.expose
def listaIncidentes():
    incidentes = Incidents()
    mostrarIncidents = incidentes.mostrarIncidents()
    inc =""
    for element in mostrarIncidents:
        inc = inc + "<div class='boton_issues' id="+element+" onclick=adicionarIssueAReporte('"+element+"')>"+element+"</div>"
    return inc


@eel.expose
def imprimirSonda(datosSonda,cliente):

    print(("Concatenado en python "+str(datosSonda)))
    la=[]
    #los ; el conjunto de datos cada sonda.
    li = list(datosSonda.split(";"))
    print(("Este es li: "+str(li)))
    print(("Cliente es: '"+str(cliente)+"'"))
    for datosUnaSonda in li:
        print(("Paquete de una sonda es:"+datosUnaSonda))
        if datosUnaSonda != "":
            la.append(datosUnaSonda.split(","))
            print(("la tiene los datos"+str(la)))
    reportes = Reportes(cliente)
    datosReporte = reportes.generadorWord(la)
    print ("Entrada 1")


@eel.expose
def abrirArchivo():
    print ("Entrada 2")
    now = datetime.utcnow()
    date_timeFile = now.strftime("%Y%m%d")
    print((os.getcwd()))
    os.startfile('.\\Clientes\\'+obj.cliente+'\\Reporte_Errores\\'+str(date_timeFile)+'_ATT_Probes.docx')

@eel.expose
def mostrarSondas():
    sondas = Sonda("test")
    mostrarSondas = sondas.mostrarSondas()
    son =""
    for element in mostrarSondas:
        son = son + "<div class='boton_issues' id="+element+" onclick=sondaAmostrar('"+element+"')>"+element+"</div>"
    return son

@eel.expose
def evidenciasDoc(texto):
    caja = texto
    print(("Esta es la caja de texto desde python: "+texto))

eel.start('frontend.html')
