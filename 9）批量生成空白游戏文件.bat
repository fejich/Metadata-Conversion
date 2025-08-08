@echo off
:: 遍历当前目录下的所有txt文件

SET PDR=%~dp0\
FOR /R %~dp0 %%I IN (*.txt) DO (
  CD "%%~pI"
  ECHO "%%~pI"
  python "%PDR%generate_files_same_dir.py"
)

pause