import time
import easygui
#import winsound

a = 1
b = input("przez ile sekund pokazywac zegar")
b = int(b)
c = int(b)

while (a <= b):
   lokczas= time.localtime()
   czas = time.strftime("%H:%M:%S", lokczas)
   print (czas, "pozostalo jeszcze",c,"sekund")
   time.sleep (1)
   a = a + 1
   c = c - 1
   if c == 0:
     print ('KONIEC')
     #sygnal dzwiekowy potrzebny winsound (zaimportowany powyzej) pierwszy paramater to czestotliwosc, drugi dlugosc w ms
     #winsound.Beep(2500,1000)
     time.sleep (5)

