@ECHO OFF 
:: This batch file details Windows 10, hardware, and networking configuration.
TITLE My System Info
ECHO Please wait... Checking system information.
:: Section 1: Windows 10 information
ECHO ==========================
ECHO WINDOWS INFO
ECHO ============================
systeminfo | findstr /c:"OS Name"
@REM systeminfo | findstr /c:"OS Version"
@REM systeminfo | findstr /c:"System Type"
:: Section 2: Hardware information.
@REM ECHO ============================
@REM ECHO HARDWARE INFO
@REM ECHO ============================
@REM systeminfo | findstr /c:"Total Physical Memory"
@REM wmic cpu get name
@REM wmic diskdrive get name,model,size
@REM @REM wmic path win32_videocontroller get name
@REM :: Section 3: Networking information.
@REM ECHO ============================
@REM ECHO NETWORK INFO
@REM ECHO ============================
@REM ipconfig | findstr IPv4
@REM @REM ipconfig | findstr IPv6
@REM ECHO ============================
@REM ECHO ============================
@REM ECHO You want start the program?
@REM ECHO Enter Y for yes
@REM ECHO Enter N for no
@REM CHOICE /c YN /m "Yes or No"
START  c:/Users/maneesh/webproject/pdf-json-brazil/.venv/Scripts/python.exe c:/Users/maneesh/webproject/pdf-json-brazil/step1_gui_brazil.py
@REM PAUSE