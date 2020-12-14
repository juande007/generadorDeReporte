# -*- coding: utf-8 -*-
import json
#import simplejson as json

path = "C:\Users\CORE i3\Documents\GitHub\generadorDeReporte\Incidentes\SF.json"

# diccionario =[]
#
# diccionario={
#     {
#         "nuevoIncident": [
#             {
#                 u"Analisis": u"La sim falla y la sonda no logra establecer conexión a la red.",
#                 u"Descripcion": u"Cuando se presenta un fallo en la SIM, se observa un mensaje de error como este ERROR: SIM failure",
#                 u"Workaround": u"Generalmente luego de un tiempo la sonda se recupera, sin embargo se ha aplicado un fix el cual ayuda a mitigar este error.",
#                 u"Root Cause": u"Desconocido, posible desgaste natural o un ambiente no apropiado.",
#                 u"Recomendacion": u"En caso de que el issue se presente constantemente, se recomienda hacer un cambio de SIM CARD",
#                 u"Nombre": u"SimF"
#             }
#         ]
#     }
# }

# diccionario=u"holá"
#diccionario=diccionario.decode("ascii",errors='replace')
#print(diccionario.encode("ascii",errors='replace'))
with open(path) as f:
    data = json.load(f)

    for lineaArchivo in data["nuevoIncident"]:
        analisisX = lineaArchivo["Analisis"]
        print (analisisX)

#print(data)

# archivo = open(path, "r")
# archivo.write(json.dumps(diccionario))
# archivo.close()
# #cad_uni.encode("ascii",errors='replace')
#
# print(diccionario)
