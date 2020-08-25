schtasks /delete /tn "Validar_si_hay_errores_manana" /f
schtasks /delete /tn "Validar_si_hay_errores_tarde" /f
schtasks /delete /tn "Validar_si_hay_errores_noche" /f
C:\python27\python.exe instalador.py
@echo off
C:
cd\gemalto\scripts\
cd %2
del/Q *.*
if exist %1 del %1
cd\