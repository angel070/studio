@ECHO OFF
@REM cd C:\DjangoProject\StudioManagementsystem 
@REM call Django_env\Scripts\activate 
@REM cd Studio
@REM python manage.py runserver
@REM start "" "http://127.0.0.1:8000/"

start cmd.exe /C "cd C:\DjangoProject\StudioManagementsystem && Django_env\Scripts\activate && cd Studio && python manage.py runserver" 
start "" "http://127.0.0.1:8000/"
