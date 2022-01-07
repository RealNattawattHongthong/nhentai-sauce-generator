import random as r
import webbrowser
import pyperclip as pc
from linkpreview import link_preview as lp
from PIL import Image
import requests
from io import BytesIO
from colorama import Fore, Back, Style
from colorama import init
import os


init()
os.system('cls' if os.name == 'nt' else 'clear')
print("WARNING THIS WILL NOT OPEN IN INCOGNITO MODE")
print(Fore.MAGENTA + "*************************************")
print("Nhentai Number Generator With Checker")
print("*************************************")
print(Fore.RESET)
init()
print(Fore.GREEN + "This is only for mode 1:")
amount1 = int(input("How many codes do you want to check and generate but the amount will be decreased by 1:"))
print("This is only for mode 2:")
show_img = input("show image preview? y/n:")
auto = input("Auto open link in browser? if no it will only copy the number in clipboard y/n:")
print("This is only for mode 3:")
amount = int(input("How many codes do you want to check and generate but the amount will be decreased by 1:"))
def gen_select():
  print("Select Mode:")
  print("1 Auto Generate mode for Nhentai codes only(optimized for performance)")
  print("2 Normal mode for generating 1 NHentai code per time with all the features(copy to clipboard,full description,cover preview)")
  print("3 For Generating NHentai codes in a specified amount with description will be saved in 6DigitCodesPreview")
  print("4 Is for checking NHentai codes")
def gen():
  for i in range(1):
    r1 = r.randint(1, 3)
    r2 = r.randint(0, 9)
    r3 = r.randint(0, 9)
    r4 = r.randint(0, 9)
    r5 = r.randint(0, 9)
    r6 = r.randint(0, 9)
    r1re = str(r1)
    if r1re == "0":
      r2 = r.randint(1,8)
      r1re = r1re.replace("0", "")
    allr = str(r1re) + str(r2) + str(r3) + str(r4) + str(r5) + str(r6) 
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
    print("Saved the numbers in the file named 6DigitCodePreview.txt you can click on it to view")
    with open('6DigitCodePreview.txt', 'a', encoding="utf-8") as f:
      f.writelines("This is the code:" + allr)
      f.writelines("\n")
      f.writelines(url)
      f.writelines("\n")
      f.writelines("title:"+ preview.title)
      f.writelines("\n")
      f.writelines("tags:"+ preview.description)
      f.writelines("\n")
      f.writelines("\n")
    print("Saved the numbers in the file named 6DigitCodeArchives.txt you can click on it to view")
    with open('6DigitCodeArchives.txt', 'a') as f:
      f.writelines(allr)
      f.writelines("\n")
    pc.copy(allr)
def genBatch(amount):
  os.system('cls' if os.name == 'nt' else 'clear')
  for i in range(amount):
    print("Process Number:",i)
    r1 = r.randint(0, 3)
    r2 = r.randint(0, 8)
    r3 = r.randint(0, 9)
    r4 = r.randint(0, 9)
    r5 = r.randint(0, 9)
    r6 = r.randint(0, 9)
    r1re = str(r1)
    if r1re == "0":
      r2 = r.randint(1,8)
      r1re = r1re.replace("0", "")
    allr = str(r1re) + str(r2) + str(r3) + str(r4) + str(r5) + str(r6) 
    url = "http://nhentai.net/g/{}".format(allr)
    if(auto == "y"):
      webbrowser.open_new_tab(url)    
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
    print("Saved the numbers in the file named 6DigitCodePreview.txt you can click on it to view")
    with open('6DigitCodePreview.txt', 'a', encoding="utf-8") as f:
      f.writelines("This is the code:" + allr)
      f.writelines("\n")
      f.writelines(url)
      f.writelines("\n")
      f.writelines("title:"+ preview.title)
      f.writelines("\n")
      f.writelines("tags:"+ preview.description)
      f.writelines("\n")
      f.writelines("\n")
    print("Saved the numbers in the file named 6DigitCodeArchives.txt you can click on it to view")
    with open('6DigitCodeArchives.txt', 'a') as f:
      f.writelines(allr)
      f.writelines("\n")
def run():
  for i in range(amount1):
    r1 = r.randint(0, 3)
    r2 = r.randint(0, 9)
    r3 = r.randint(0, 9)
    r4 = r.randint(0, 9)
    r5 = r.randint(0, 9)
    r6 = r.randint(0, 9)
    r1re = str(r1)
    allr = str(r1re.replace("0", "")) + str(r2) + str(r3) + str(r4) + str(r5) + str(r6) 
    print("Save successful! Process number:",i)
    with open('6DigitCodeArchives.txt', 'a') as f:
      f.writelines(allr)
      f.writelines("\n")
def checker():
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
  print("Finished checking and generating codes:", amount - 1)
  gen_select()
  mode = input("Enter the mode you want:")
  if mode == "1":
    run()
  elif mode == "2":
    gen()
  elif mode == "3":
    genBatch()
  elif mode == "4":
    print("*******************")
    print("Nhentai Code info checker")
    print("*******************")
    checker()
  restart = input("Do you want to generate/check again in the same mode? y/n:")
  if restart == "y":
    if mode == "1":
      run()
    elif mode == "2":
      gen()
    elif mode == "3":
      amount = int(input("How many codes do you want to check and generate but the amount will be decreased by 1:"))
      genBatch()
    elif mode == "4":
      print("*******************")
      print("Nhentai Code info checker")
      print("*******************")
      checker()
  else:
    selectmode = input("Do you want to select another mode y/n?:")
    if selectmode == "y":
      gen_select()
      mode = input("Enter the mode you want:")
      if mode == "1":
        run()
      elif mode == "2":
        gen()
      elif mode == "3":
        amount = int(input("How many codes do you want to check and generate but the amount will be decreased by 1:"))
        genBatch()
      elif mode == "4":
        print("*******************")
        print("Nhentai Code info checker")
        print("*******************")
        checker()
    elif selectmode == "n":
      break
