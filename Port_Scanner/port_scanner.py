import socket
from termcolor import colored

Target = input("Enter target IP: ")

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def port_scanner(port):
    try:
        service = socket.getservbyport(port, "tcp")
    except OSError:
        try:
            service = socket.getservbyport(port, "udp")
        except OSError:
            service = "UNKNOWN"

    result = tcp_sock.connect_ex((Target, port))

    if result == 0:
        print(colored(f"[+] {port}/tcp  open  {service}", "green"))

print()

print(colored(f"  Target: {Target}", "red"))
print(colored(f"  PORT      STATE  SERVICE", "yellow"))

for port in range(1, 1000):
    port_scanner(port)

tcp_sock.close()