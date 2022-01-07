@echo off
echo Checking Python Version!
timeout 5 > null
echo install required libraries
pip install linkpreview
pip install webbrowser
pip install Pillow
pip install pyperclip
pip install requests
pip install io
pip install colorama
timeout 5 > null 
echo installing...
del null
