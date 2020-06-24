#Se define la ruta C:\gemalto\scripts como la ruta donde se hubicaran los scripts realizados por Gemalto Soporte.
#En la siguiente linea se defina la ruta
Set-ExecutionPolicy Unrestricted
$rutaDelInstalador = Get-Location
$rutaPrimerEjecutable = "C:\gemalto\scripts"

#En la siguiente linea se valida si la ruta existe y si el resultado va a la variabla RutaPrincipal
$rutaPrincipal = Test-Path $rutaPrimerEjecutable

#En este If, si la ruta existe o No
If ($rutaPrincipal -eq $True) {
   Write-Host "El directorio es el correcto"  
} Else {
   Write-Host "No se encontró el directorio C:\gemalto\scripts"
   Write-Host "Creando el directorio"
   #Se crea el directorio
   New-Item -Path 'C:\gemalto\scripts' -ItemType Directory
   #se crear el archivo variable    
}

   Remove-Item -Path $rutaPrimerEjecutable"\dbErrores.txt"
   Remove-Item -Path $rutaPrimerEjecutable"\listaErrores.txt"
   New-Item -Path $rutaPrimerEjecutable"\dbErrores.txt" -ItemType file
   New-Item -Path $rutaPrimerEjecutable"\listaErrores.txt" -ItemType file
   Add-Content -Path $rutaPrimerEjecutable"\dbErrores.txt" -Exclude "help*" -Value "*"
   Add-Content -Path $rutaPrimerEjecutable"\listaErrores.txt" -Exclude "help*" -Value "*Late packet*"
   Add-Content -Path $rutaPrimerEjecutable"\listaErrores.txt" -Exclude "help*" -Value "*SIM failure*"
   Add-Content -Path $rutaPrimerEjecutable"\listaErrores.txt" -Exclude "help*" -Value "*Limiting DL traffic of umts*"
   Add-Content -Path $rutaPrimerEjecutable"\listaErrores.txt" -Exclude "help*" -Value "*SIM PIN required*"
   Add-Content -Path $rutaPrimerEjecutable"\listaErrores.txt" -Exclude "help*" -Value "*Couldn't get the name of the port to send QMI commands*"   
   Copy-Item $rutaDelInstalador"\w7_validador.ps1" -Destination $rutaPrimerEjecutable
   Copy-Item $rutaDelInstalador"\variables.ps1" -Destination $rutaPrimerEjecutable
   schtasks /delete /tn "Validar_si_hay_errores_manana" /f
   schtasks /delete /tn "Validar_si_hay_errores_tarde" /f
   schtasks /delete /tn "Validar_si_hay_errores_noche" /f
   schtasks /create /tn "Validar_si_hay_errores_manana" /tr "powershell C:/gemalto/scripts/w7_validador.ps1" /sc daily /st 11:30:00
   schtasks /create /tn "Validar_si_hay_errores_tarde" /tr "powershell C:/gemalto/scripts/w7_validador.ps1" /sc daily /st 17:00:00
   schtasks /create /tn "Validar_si_hay_errores_noche" /tr "powershell C:/gemalto/scripts/w7_validador.ps1" /sc daily /st 19:00:00