import subprocess
import os
import requests
import time

hosting = True

def file_creation():
    global file_path, file

    file_path = input("Enter path for file: ")
    os.chdir(file_path)
    
    file_name = input("Enter file name: ")
    html = ".html"
    file = file_name + html

    with open(file, "w") as site:
        content = input("Enter file content: ")
        site.write(content)

def host():
    global hosting, port_num, askToHost

    askToHost = input("Host site?(Yes -> 1 / No -> 0): ")

    if askToHost == "1":
        port_num = int(input("Enter port number (1024 - 49151): "))
        subprocess.Popen(["python3", "-m", "http.server", str(port_num), "-d", file_path])
        time.sleep(1)
    elif askToHost == "0":
        hosting = False
    else:
        print("Enter a valid value")

def server_response():
    if askToHost == "1":
        url = f"http://localhost:{port_num}/{file}"
        site = requests.get(url)
        print(f"Status: {site.status}")
        print(f"Content: {site.text}")
    elif askToHost == "0":
        print("Disconnected from hosting server")

while hosting:
    file_creation()
    host()
    server_response()

    hosting = False