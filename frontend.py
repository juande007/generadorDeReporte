import eel, os, random
import GeneradorDeReporte



eel.init('web')

@eel.expose
def pick_file(comando):
    reporte = GeneradorDeReporte
    print(comando)
    return reporte.tarea(comando)

@eel.expose
def clientes():
    reportes = GeneradorDeReporte
    listadoClientes = reportes.listadoDeClientes()
    print "desde frontend "+listadoClientes
    return listadoClientes

# #    if os.path.isdir(folder):
#         return random.choice(os.listdir(folder))
#     else:
#         return 'Not valid folder'

eel.start('frontend.html')
