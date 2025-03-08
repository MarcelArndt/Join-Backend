@echo off
setlocal


if not exist env (
    echo Erstelle virtuelle Umgebung "env"...
    python -m venv env
)


call env\Scripts\activate


echo Installiere Requirements...
pip install -r requirements.txt


echo Führe Datenbankmigrationen durch...
python manage.py makemigrations
python manage.py migrate


echo Starte Django-Server...
start /b python manage.py runserver

REM Warte kurz, um sicherzustellen, dass der Server läuft
timeout /t 5


echo Führe utils.py aus...
python utils.py


echo Stoppe den Django-Server...
taskkill /f /im python.exe

endlocal
echo Daten sind installiert und fenster kann geschlossen werden
pause