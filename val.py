import time
import subprocess, sys


def run():
    t=1
    while t <= 12:
   	time.sleep(2)
   	p = subprocess.Popen(["powershell.exe",
              ".\\validador\\w7_validador.ps1"],
              stdout=sys.stdout)
	p.communicate()
   	print("Hola mundo" + str(t))
    t +=1

def main():
    run()

if _name=='main_':
    main()
