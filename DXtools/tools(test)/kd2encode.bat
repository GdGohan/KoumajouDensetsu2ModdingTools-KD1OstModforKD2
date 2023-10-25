@echo off
chcp 65001 > nul
setlocal

set /p input_folder=Digite o caminho da pasta de entrada: 
set /p output_filename=Digite o nome do arquivo de saída (com extensão): 

DXAEncode.exe -K:EFC12001DCF7BB72FACBF201 "%input_folder%" "%output_filename%"

endlocal
