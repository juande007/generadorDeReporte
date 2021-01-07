import re

palabra= (raw_input('Escriba una palabra: '))
patron = re.compile('([a-zA-Z]+)(\s)')
matcher = patron.search(palabra)
cliente = matcher.group()

print ('El cliente es: ' + cliente)

patron = re.compile('(\s)([0-9]+)')
matcher = patron.search(palabra)
matcher.groups()
sonda = matcher.group(0)

print ('La sonda es: ' + sonda)
