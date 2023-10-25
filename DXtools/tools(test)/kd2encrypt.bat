@echo off
setlocal enabledelayedexpansion
set /p "input_file=Arraste e solte o arquivo para encriptografar: "
set python_executable=python
set script_path=kd2encrypt.py

rem Extrair o nome do arquivo (sem extensão) e a extensão
for %%F in ("!input_file!") do (
  set "filename=%%~nF"
  set "extension=%%~xF"
)

"%python_executable%" "%script_path%" "!input_file!"
endlocal
