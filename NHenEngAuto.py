import random as r

print("This will generate automatically and will be saved in 6DigitCodeArchives.txt")
print("*******************")
print("Nhentai number generator")
print("*******************")
amount = int(input("Enter how many codes do you want:"))
def run():
  for i in range(amount):
    r1 = r.randint(1, 3)
    r2 = r.randint(0, 9)
    r3 = r.randint(0, 9)
    r4 = r.randint(0, 9)
    r5 = r.randint(0, 9)
    r6 = r.randint(0, 9)
    allr = str(r1) + str(r2) + str(r3) + str(r4) + str(r5) + str(r6) 
    print("Save successful! Process number:",i)
    with open('6DigitCodeArchives.txt', 'a') as f:
      f.writelines(allr)
      f.writelines("\n")
while True:
  run()
  print("Operation Done! generated {} codes".format(amount))
  exite = input("generate again? y/n")
  if exite == "n":
    break

