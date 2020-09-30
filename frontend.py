import eel, os, random
import GeneradorDeReporte
import re
from datetime import datetime
from incidents import Incidents
# from generador_word import datosReporte
from generador_word import Reportes


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
    print ("El cliente es desde PYTHON FRONTEND: '" + str(cliente)+"'")
    obj.cliente=cliente
    incidentes = Incidents()
    mostrarIncidents = incidentes.mostrarIncidents()
    inc =''

    reporte = GeneradorDeReporte
    sondas = reporte.tarea(comando)
    print(comando)
    resultado="<input type='text' id='cliente' value='"+cliente+"'>"+cliente+"</input>"
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
def imprimirSonda(datosSonda,cliente):

    print("Resultadp desde python "+str(datosSonda))
    la=[]
    li = list(datosSonda.split(";"))
    print ("Cliente en imprimirSonda es: '"+str(cliente)+"'")
    for element in li:
        print element
        print ("el contenido element es:"+element)
        if element != "":
            la.append(element.split(","))
            print la
    reportes = Reportes(cliente)
    datosReporte = reportes.generadorWord(la)


@eel.expose
def abrirArchivo():
    now = datetime.utcnow()
    date_timeFile = now.strftime("%Y%m%d")
    print os.getcwd()
    os.startfile('.\\Clientes\\'+obj.cliente+'\\Reporte_Errores\\'+str(date_timeFile)+'_ATT_Probes.docx')

eel.start('frontend.html')
