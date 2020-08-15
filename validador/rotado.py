
import shutil
import time
import datetime
from datetime import datetime as date
import datetime as elTiempo

fechaActual = elTiempo.datetime.now()
horaActual = elTiempo.datetime.now()
# print("Fecha actual: "+ str(fechaActual))
# print("Hora actual: "+ str(horaActual))

actual1 = elTiempo.datetime.now()
print(actual1)
x = datetime.timedelta(seconds=3600)
print(x)
antes=actual1-datetime.timedelta(seconds=3600)
print(antes)
actual2 = elTiempo.datetime.now()
diferencia =actual2 - antes
print(diferencia.total_seconds()/60)
datetime.timedelta(seconds=3600)
#
# def actual1 < x:
#     print ("entro a la condicion")

# datetime.timedelta(seconds=3600)
#
# # ayer = ahora - datetime.timedelta(days=1)
# print(actual1)
# print(actual2)
# diferencia = actual1 - horaActual.datetime.timedelta(seconds=3600)
#
# print(diferencia.days)
# print(diferencia.seconds)
# #
# print(diferencia.total_seconds())
