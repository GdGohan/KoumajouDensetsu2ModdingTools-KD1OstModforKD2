@echo off
setlocal enabledelayedexpansion
set /p "input_file=Arraste e solte o arquivo para descriptografar: "
set python_executable=python
set script_path=kd2decrypt.py

rem Extrair o nome do arquivo (sem extensão) e a extensão
for %%F in ("!input_file!") do (
  set "filename=%%~nF"
  set "extension=%%~xF"
)

set output_file="!filename!_decrypted!extension!"

"%python_executable%" "%script_path%" "!input_file!"
endlocal
