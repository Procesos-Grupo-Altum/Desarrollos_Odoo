@echo off
:loop
Rem== quiero que desde aqui me calcule el tiempo
for /f "tokens=*" %%a in ('powershell get-date -uformat %%s') do set "start_time=%%a"

rem== aqui lo que quiero ejecutar ciclico
"E:\Desarrollos_Odoo\Automatizaciones\.venv\Scripts\python.exe" "E:\Desarrollos_Odoo\Automatizaciones\Ejecuciones\python\Migracion Odoo.py" 





rem== aqui me aparesca el tiempo de duracion
for /f "tokens=*" %%a in ('powershell get-date -uformat %%s') do set "end_time=%%a"
set /a duration=end_time-start_time
echo [INFO] Tiempo transcurrido: %duration% segundos

timeout /t 20 /nobreak
goto loop


