@echo off
echo Checking Python Version!
timeout 5 > null
echo install required libraries
pip3 install linkpreview
pip3 install webbrowser
pip3 install Pillow
pip3 install pyperclip
pip3 install requests
pip3 install io
timeout 5 > null 
echo installing...
del null
