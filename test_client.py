#!/usr/bin/env python3

import socket
import json
import time

def send_command(sock, command):
    """Send a command to the server and get response"""
    json_data = json.dumps(command)
    sock.send(json_data.encode())
    
    # Wait for response
    data = ""
    while True:
        try:
            data += sock.recv(1024).decode()
            return json.loads(data)
        except ValueError:
            continue
        except Exception as e:
            return f"Error: {e}"

def test_keylogger():
    """Test the keylogger functionality"""
    try:
        # Connect to server
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('127.0.0.1', 54321))
        print(" Connected to KeyLogger server!")
        
        # Test commands
        commands = [
            "help",
            "pwd",
            "whoami",
            "screenshot",
        ]
        
        for cmd in commands:
            print(f"\n🔹 Testing command: {cmd}")
            try:
                response = send_command(sock, cmd)
                print(f"📝 Response: {response}")
                time.sleep(1)
            except Exception as e:
                print(f" Error with {cmd}: {e}")
        
        # Close connection
        sock.close()
        print("\n Test completed!")
        
    except Exception as e:
        print(f" Connection failed: {e}")

if __name__ == "__main__":
    test_keylogger()