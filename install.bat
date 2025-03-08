@echo off
setlocal

REM Überprüfen, ob das Verzeichnis "env" existiert
if not exist env (
    echo Erstelle virtuelle Umgebung "env"...
    python -m venv env
)

REM Aktivieren der virtuellen Umgebung
call env\Scripts\activate

REM Installieren der Anforderungen
echo Installiere Requirements...
pip install -r requirements.txt

REM Datenbankmigrationen durchführen
echo Führe Datenbankmigrationen durch...
python manage.py makemigrations
python manage.py migrate

REM Starte den Django-Server im Hintergrund
echo Starte Django-Server...
start /b python manage.py runserver

REM Warte kurz, um sicherzustellen, dass der Server läuft
timeout /t 5

REM Führe utils.py aus
echo Führe utils.py aus...
python utils.py

REM Stoppe den Django-Server
echo Stoppe den Django-Server...
taskkill /f /im python.exe

endlocal
echo Daten sind installiert und fenster kann geschlossen werden
pause