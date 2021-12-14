import random as r
import webbrowser
import pyperclip as pc
from linkpreview import link_preview as lp
from PIL import Image
import requests
from io import BytesIO

print("ข้อควรระวัง! ไม่เปิดในโหมดไม่ระบุตัวตนนะจ๊ะ")
print("*******************")
print("โปรแกรมสุ่มวาร์ป Nhentai")
print("*******************")
show_img = input("พรีวิวรูปไหม? y/n:")
auto = input("เปิดลิงค์ให้เลยไหม? ถ้าไม่จะก็อปโค้ดให้ในคลิปบอร์ด y/n:")
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
    print("สุ่มวาร์ปเรียบร้อยบริหารข้อมือให้สนุกนะ และ ก็อปโค้ดให้ในคลิปบอร์ดให้แล้วนะ!")
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
    print("เซฟเลขหกหลักใว้ใน 6DigitCodeArchives.txt ให้แล้วนะ")
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