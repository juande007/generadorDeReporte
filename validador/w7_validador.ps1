# —- Script busca textos con errores en el log NxCliente.log
#Se generan las variables que tendrán los mensajes a validar

$ListaDeErrores= New-Object System.Collections.ArrayList
$ListaDeErroresOld= New-Object System.Collections.ArrayList
$numeroDeErroresActual=New-Object System.Collections.ArrayList
$numeroDeErroresOld=New-Object System.Collections.ArrayList
$contadores=New-Object System.Collections.ArrayList

# Metemos el contenido del archivo en la variable $linea y por cada una de las
# líneas que nos devuelve buscamos dentro la $cadena, que es el segundo parámetro
# que le hemos pasado al script
#validamos si la ruta es correcta

$destination_folder="C:\gemalto\scripts"
cd $destination_folder
.\variables.ps1

$difernciaStandar=50
$tiempoParaInciarNxClient=10

function escribirEnLog([string]$text)
{
  Write-Host $text
  $date = Get-Date;
  $formattedDate=$date.ToUniversalTime().ToString("yyyy-MM-dd H:mm:ss")
  $text=$formattedDate+"000 - "+$text
  $fileToCheck = $aplication_folder + $service_name+".log"  
  if (Test-Path $fileToCheck -PathType leaf){
            Write-Host "La ruta es "$fileToCheck
            Add-Content -Path $aplication_folder$service_name".log" -Exclude "help*" -Value $text    
  }
  else {
            Write-Host "La ruta es "
            Add-Content -Path $aplication_folderMC$service_name".log" -Exclude "help*" -Value $text
  }
  
}



Function leerListaDeErrores{
	Write-Host $destination_folder"\listaErrores.txt"
	get-content -Path $destination_folder"\listaErrores.txt" | foreach {
		$linea = $_
		if ($linea -ne "") {
			$script:ListaDeErrores.Add($linea)
			$script:numeroDeErroresActual.Add("0")
			$script:numeroDeErroresOld.Add(0)
			$script:contadores.Add(0)
		}
	}
}


Function obtenerErroresAnteriores{
	$contador=0
	Write-Host $destination_folder"\dbErrores.txt"
	get-content -Path $destination_folder"\dbErrores.txt" | ForEach { 
		$numeroDeErroresAntes = $_
		if ($numeroDeErroresAntes -ne '*') {
			$script:numeroDeErroresOld[$contador]=$numeroDeErroresAntes
		}else {
		    Write-Host "No hay errores"		    
		}
		$contador=$contador+1
		
	}
	$numeroDeErroresOld	
}


Function actualizarErrores{   
   Remove-Item -Path $destination_folder"\dbErrores.txt"
   New-Item -Path $destination_folder"\dbErrores.txt" -ItemType file
	for($i=0;$i -lt $ListaDeErrores.count;$i++){		
		$a=$ListaDeErrores[$i].ToString()
		$b=$contadores[$i].ToString()
		Write-Host "fila:"$i" error:"$a" numero errores:"$b
		Add-Content -Path $destination_folder"\dbErrores.txt" -Exclude "help*" -Value $b
	}
}

Function reiniciarNxClient{
	$idNxClient = (Get-Process $service_name).id
	Write-Host "Id process de la apliación: "$idNxClient
	Write-Host "Deteniendo NxClient"
	Stop-Process -Id $idNxClient
	Write-Host "Esperando a que se cierre NxClient..."
	Wait-Process -Id $idNxClient
	Start-Sleep -s $tiempoParaInciarNxClient    
    $fileToCheck = $aplication_exe_folder + $aplication_name
    Write-Host $fileToCheck
    if (Test-Path $fileToCheck -PathType leaf)
    {
        start-process -filepath $aplication_exe_folder$aplication_name
        Write-Host "Inciando 32 bits"
        
    }else {
        start-process -filepath $aplication_exe_folderB$aplication_name
        Write-Host "Inciando 64 bits"$aplication_exe_folderB$aplication_name
    }
    $idNxClient = (Get-Process $service_name).id
	Write-Host "NxCient inicio con el process id: "$idNxClient
    exit
}


Function contadorMultiErrores{
        $fileLog = $aplication_folder + $service_name+".log"
        if (Test-Path $fileLog -PathType leaf){
            Write-Host "Ruta de los logs"$fileLog
        }
        else {
            $fileLog = $aplication_folderMC+$service_name+".log"
            Write-Host "Ruta de los logs"$fileLog
        }





    get-content -Path $fileLog | foreach {
		$linea = $_		
		for($i=0;$i -lt $ListaDeErrores.count;$i++){
			if ($linea -like $ListaDeErrores[$i].ToString()) {							
		      		$script:Contadores[$i]=$Contadores[$i]+1				
			}
		}
	}

	for($i=0;$i -lt $ListaDeErrores.count;$i++){
		Write-Host "Numero de Errores "$Contadores[$i]" para el error: "$ListaDeErrores[$i]
	}
    actualizarErrores
}

Function deferenciadorDeError{	

		for($i=0;$i -lt $ListaDeErrores.count;$i++){
			Write-Host "Contadores:"$contadores[$i]" valores anteriores:"$numeroDeErroresOld[$i]		
            
            if ([int]$contadores[$i] -ge [int]$numeroDeErroresOld[$i]) {                
                $diferencia=[int]$contadores[$i] - [int]$numeroDeErroresOld[$i]                
            }else {
                ## Write-Host "Hay un rotado de log o reinstalación"
                $diferencia=[int]$contadores[$i]
            }	

    		if ($difernciaStandar -le $diferencia) {
    			if (($i -eq 1) -or ($i -eq 3) -or ($i -eq 4)) {
                    escribirEnLog("Reiniciando.... Sonda")                    
                    Restart-Computer -Force                   
                    exit                    
    			    
    			}else {
                    escribirEnLog("Reiniciando.... NxClient")
                    reiniciarNxClient                                        
    			}


    		}
	}

}







Function validarSiNxclientExiste{			
		$NxClient = Get-Process nxclient -ErrorAction SilentlyContinue
		if($NxClient -eq $null)
		{
		 Write-host "NxClient no está corriendo"
		 reiniciarNxClient
		}
		else
		{
            $fileLog = $aplication_folder+$service_name+".log"
            if (Test-Path $fileLog -PathType leaf){
                  $log = $fileLog
            }
            else {
                $log = $aplication_folderMC+$service_name+".log"
            }


    		$log = get-content -Path $log
    		$log.GetType()|Format-Table -AutoSize | Out-String
            [int]$contadorLineas = $log.count
            [int]$contadorLineas = [int]$contadorLineas - 1
            Write-host "Total de lineas = "$contadorLineas  
            $lineaAEvaluar=$log[$contadorLineas] 
            $dateLog=$lineaAEvaluar.Substring(0, 19)
         
            for($i=20;$i -ge 0;$i--){
                $dateLog = $dateLog -as [DateTime];

                if ($dateLog){ break
                }else { Write-host 'No es una fecha, pasando a la siguiente linea'}

                $contadorLineas=$contadorLineas-1
                $lineaAEvaluar=$log[$contadorLineas]             
                $dateLog=$lineaAEvaluar.Substring(0, 19)
            }

            escribirEnLog(" - Validador - iniciando analisis de log - version 20200422")         
            $date = Get-Date;
            $date=$date.ToUniversalTime().ToString("yyyy-MM-dd H:mm:ss")
            $diferencia = New-TimeSpan -Start $dateLog -End $date
            Write-host "Fecha sistema: "$date
            Write-host "Fecha log: "$dateLog
            Write-host "Diferencia horas :"$diferencia.hours # Check results
            Write-host "Diferencia dias  :"$diferencia.days # Check results
            [int] $diffHoras=$diferencia.hours
            [int] $diffDias=$diferencia.days
            if (($diffDays -ge 1 ) -Or ($diffHoras -ge 2)) {
                $enLog="Reiniciando Nxlient... Diferencia horas :"+$diferencia.hours+"  Diferencia dias  :"+$diferencia.days
                    escribirEnLog($enLog)
                    reiniciarNxClient                
            }
    		 
    	}

}


validarSiNxclientExiste
leerListaDeErrores
obtenerErroresAnteriores
contadorMultiErrores
deferenciadorDeError
