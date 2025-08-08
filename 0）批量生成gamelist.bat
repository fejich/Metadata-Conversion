@echo off
:: 遍历当前目录下的所有txt文件

SET PDR=%~dp0\
FOR /R %~dp0 %%I IN (*.txt) DO (
  CD "%%~pI"
  ECHO "%%~pI"
  python "%PDR%metadata_to_gamelist.py"
)

pause