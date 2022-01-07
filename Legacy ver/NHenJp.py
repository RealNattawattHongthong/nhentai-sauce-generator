import random as r
import webbrowser
import pyperclip as pc
from linkpreview import link_preview as lp
from PIL import Image
import requests
from io import BytesIO

print("インコグニートモードでは開きません。")
print("*******************")
print("ンヘンタイゲツネラタ")
print("*******************")
show_img = input("ショー・イメージ・プレビュー? y/n:")
auto = input("リンクを自動的にブラウザで開きますか？ もしそうでなければ、クリップボードに番号をコピーするだけです。 y/n:")
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
    print("生成され、クリップボードにコピーされます")
    print("これは数:",allr)
    print("これがそのリンクです。:",url)
    preview = lp(str(url))
    print("これがリンクリンクのプレビュー")
    response = requests.get(preview.image)
    print("タイトル:", preview.title)
    print("タグ:", preview.description)
    if show_img == "y":
      img = Image.open(BytesIO(response.content))
      img.show()
    pc.copy(allr)
    print("6DigitCodeArchives.txtというファイルに保存されており、クリックすると表示されます。")
    with open('6DigitCodeArchives.txt', 'a') as f:
      f.writelines(allr)
      f.writelines("\n")
while True:
  gen()
  restart = input("また生成したいと思いますか？? y/n:")
  if restart == "y":
    gen()
  else:
    break