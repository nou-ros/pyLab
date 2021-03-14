'''
1. demonstration of pynput package methods
2. Controlling our mouse & litening to mouse input
3. Controlling our keyboard & litening to keyboard input
'''

'''
# Mouse control
from pynput.mouse import Controller

def controlMouse():
    mouse = Controller()
    # changing mouse position in x axis 10 and y axis 20. As top corner is (0,0)
    mouse.position = (500,200)

# controlMouse()
'''

# We can't control mouse and keyboard simultaneously.
'''
# Keyboard control
from pynput.keyboard import Controller

def controlKeyboard():
    keyboard = Controller()
    keyboard.type("Python is awesome!")

controlKeyboard()
'''





