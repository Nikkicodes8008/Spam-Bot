#Importing requird Python Modules
import pyautogui,time
#Warning dont remove time.sleep(5) .If you remove it program will start typing into ide
# You have 5 seconds  after that  Program will type wherever the cursour is
time.sleep(5)
#Loop
i=0
while(i==0):
    pyautogui.typewrite("word")#change word to  anything you want
    pyautogui.press('enter')

 