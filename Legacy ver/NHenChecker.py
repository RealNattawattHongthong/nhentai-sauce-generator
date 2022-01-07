import random as r
import webbrowser
import pyperclip as pc
from linkpreview import link_preview as lp
from PIL import Image
import requests
from io import BytesIO
from colorama import init, Fore, Back, Style

#used for windows environment only
init()
print("*******************")
print("Nhentai Code info checker")
print("*******************")
print("It will crash if the code is invalid")
show_img = input("show image preview? y/n:")
auto = input("Auto open link in browser? y/n:")
def gen():
  for i in range(1):
    num = int(input("Please input the nhentai code:"))
    url = "http://nhentai.net/g/{}".format(num)
    if(auto == "y"):
      webbrowser.open_new_tab(url)
    print("This is the number:",num)
    print("This is the link:",url)
    preview = lp(str(url))
    print("Link preview")
    response = requests.get(preview.image)
    print("title:", preview.title)
    print("tags:", preview.description)
    if show_img == "y":
      img = Image.open(BytesIO(response.content))
      img.show()
while True:
  gen()
  restart = input("Do you want to check another code? y/n:")
  if restart == "y":
    gen()
  else:
    break