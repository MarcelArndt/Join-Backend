@echo off
setlocal

REM Überprüfen, ob das Verzeichnis "env" existiert
if not exist env (
    echo Erstelle virtuelle Umgebung "env"...
    python -m venv env
)

REM Aktivieren der virtuellen Umgebung
call env\Scripts\activate

REM Starte den Django-Server
echo Starte Django-Server...
python manage.py runserver

endlocal
