import getpass
import time
USER_NAME = getpass.getuser()

class Simulador ():

    def simulador(self):
        error = (raw_input("Ingrese el error: "))
        while 1:
        # for ejecucion in range(int(rango)):
            usuario = getpass.getuser()
            rutaArchivoLog = "C:/Users/" +usuario+ "\AppData\Local\Swiss Mobility Solutions\NxClient\NxClient.log"
            with open(rutaArchivoLog, "a") as file:
                file.write('\n'+error)
            file.close()
            time.sleep(5)

def main():
    simulador = Simulador()
    simulador.simulador()

if __name__=='__main__':
    main()
