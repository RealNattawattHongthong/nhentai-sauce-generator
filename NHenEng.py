import random as r
import webbrowser
import pyperclip as pc
from linkpreview import link_preview as lp
from PIL import Image
import requests
from io import BytesIO

print("WARNING THIS WILL NOT OPEN IN INCOGNITO MODE")
print("*******************")
print("Nhentai Generator number")
print("*******************")
show_img = input("show image preview? y/n:")
auto = input("Auto open link in browser? if no it will only copy the number in clipboard y/n:")
def gen():

  for i in range(1):
    r1 = r.randint(1, 3)
    r2 = r.randint(0, 9)
    r3 = r.randint(0, 9)
    r4 = r.randint(0, 9)
    r5 = r.randint(0, 9)
    r6 = r.randint(0, 9)
    allr = str(r1) + str(r2) + str(r3) + str(r4) + str(r5) + str(r6) 
    url = "http://nhentai.net/g/{}".format(allr)
    if(auto == "y"):
      webbrowser.open_new_tab(url)
    print("Generated and copied to clipboard!")
    print("This is the number:",allr)
    print("This is the link:",url)
    preview = lp(str(url))
    print("Link preview")
    response = requests.get(preview.image)
    print("title:", preview.title)
    print("tags:", preview.description)
    if show_img == "y":
      img = Image.open(BytesIO(response.content))
      img.show()
    print("Saved the numbers in the file named 6DigitCodeArchives.txt you can click on it to view")
    with open('6DigitCodeArchives.txt', 'a') as f:
      f.writelines(allr)
      f.writelines("\n")
    pc.copy(allr)
while True:
  gen()
  restart = input("Do you want to generate again y/n:")
  if restart == "y":
    gen()
  else:
    break