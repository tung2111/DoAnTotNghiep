import time, threading

# from win32api import GetKeyState

giay = 0
giayGym = 0
phut = 0
enabletimer = False
def demgiay():
    global giay,giayGym, phut,enabletimer,GymActive,YogaActive
    while (1):
        time.sleep(1)
        if(giayGym != 60):
            giayGym += 1
        else:
            giayGym = 0
            phut += 1
        print('giay Gym la ' + str(giayGym))

        if (enabletimer == False or giay == 60):
            giay = 0
        else:
            giay += 1
        print('giay Yoga la ' + str(giay))

def init():
    t = threading.Thread(target=demgiay)
    t.start()


'''
def key_down(key):
    state = GetKeyState(ord(key))
    if (state != 0) and (state != 1):
        return True
    else:
        return False
'''
