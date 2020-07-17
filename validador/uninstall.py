import getpass
import os
from shutil import rmtree
from os import remove

def desinstalador ():
    path = "C:/thales"
    usuario = getpass.getuser()
    file = 'C:/Users/'+ usuario +'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\inicia_validador.bat'
    rmtree(path)
    remove(file)
def main():
    desinstalador()

if __name__=='__main__':
    main()
