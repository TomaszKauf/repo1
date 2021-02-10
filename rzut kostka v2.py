import time
from easygui import *
from random import randint

looper = True
while looper == True:
  
   a = buttonbox("Wanna toss the dice ??","Choose your destiny",["Yes","Quite"])
   if a =="Yes":
        a = randint(1,6)
        print ("You got ", a)
        if a == 1:
             print (" _________ ")
             print ("|         |")
             print ("|         |")
             print ("|    O    |")
             print ("|         |")
             print ("|_________|")
        elif a == 2:
             print (" _________ ")
             print ("|         |")
             print ("|  O      |")
             print ("|         |")
             print ("|      O  |")
             print ("|_________|")
        elif a == 3:
             print (" _________ ")
             print ("|         |")
             print ("|  O      |")
             print ("|    O    |")
             print ("|      O  |")
             print ("|_________|")
        elif a == 4:
             print (" _________ ")
             print ("|         |")
             print ("|  O   O  |")
             print ("|         |")
             print ("|  O   O  |")
             print ("|_________|")
        elif a == 5:
             print (" _________ ")
             print ("|         |")
             print ("|  O   O  |")
             print ("|    O    |")
             print ("|  O   O  |")
             print ("|_________|")
        else:
             print (" _________ ")
             print ("|         |")
             print ("|  O O O  |")
             print ("|         |")
             print ("|  O O O  |")
             print ("|_________|")

        time.sleep(4)
        looper = True
   else:
        print ('Bye Bye!')
        time.sleep(2)
        looper = False
