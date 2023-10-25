@echo off
chcp 65001 > nu
setlocal enabledelayedexpansion

rem Solicita ao usuário o nome do arquivo .dat
set /p dat_file_name=Digite o nome do arquivo .dat (sem extensão):

rem Solicita ao usuário o nome da pasta
set /p folder_name=Digite o nome da pasta:

rem Chama o script Python e passa os parâmetros
python kd2encodev3.py "!dat_file_name!" "!folder_name!"

endlocal
