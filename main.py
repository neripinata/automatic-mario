import pyautogui
import keyboard
import time
from input import Jump


# pyautogui.moveTo(control_x,control_y)
# pyautogui.click()

def DetectMario():
    try:
        mario = pyautogui.locateOnScreen('images/mario.png')
        mario = pyautogui.center(mario)

        mario_x = mario[0]
        mario_y = mario[1]

        print(mario)

        return mario
    except:
        print("No Mario")


def DetectGoomba():
    try:
        goomba = pyautogui.locateOnScreen('images/goomba.png') 
        goomba = pyautogui.center(goomba)

        goomba_x = goomba[0]
        goomba_y = goomba[1]

        print(goomba)
        return goomba
    except:
        print("No Goomba")


while True:
    try:
        isGoomba = DetectGoomba()
        iSMario = DetectMario()

        if abs(isGoomba[0]-iSMario[0]) < 60 and abs(isGoomba[1]-iSMario[1]) < 10:
            Jump()
    except:
        pass

    if keyboard.is_pressed('q'):
        break







#time.sleep(3)



    
    
