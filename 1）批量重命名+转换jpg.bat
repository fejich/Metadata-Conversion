@echo off
setlocal enabledelayedexpansion

::重命名
set "counter=1"
for %%F in (box*.jpg box*.png) do (
    set "ext=%%~xF"
    ren "%%F" "boxFront!counter!!ext!"
    set /a counter+=1
)
echo ReName Done.

::转换jpg到png
SET PDR=%~dp0\
FOR /R %~dp0 %%I IN (box*.jpg) DO (
  CD "%%~pI"
  ECHO "%%~pI"
  python "%PDR%jpg_to_png.py"
)

pause