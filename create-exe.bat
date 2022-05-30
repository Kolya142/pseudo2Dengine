@echo off
pyinstaller
if %errorlevel% == 9009 pip install pyinstaller
cls
pyinstaller --noconfirm --onefile --console  "%cd%\main.py"
copy dist\* build
del /s /q dist\*
rd dist
del /s /q build\main\*
rd build\main
del main.spec