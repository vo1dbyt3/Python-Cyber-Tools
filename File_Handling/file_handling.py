import os

handling = True

def creating():
    file_name = input("Enter file name: ")
    txt = ".txt"
    txt_file = file_name + txt

    with open(txt_file, "w") as file:
        content = input("Enter file content: ")
        file.write(content)
        print(f"{file_name} was created successfully")

def deleting():
    file_name = input("Enter file name: ")

    file_path = os.path.join(path, file_name)

    if os.path.exists(file_path):
        os.remove(file_name)
        print(f"{file_name} was deleted suucessfully")
    else:
        print(f"{file_name} doesn't exist in {path}")

def viewing():
    file_name = input("Enter file name: ")

    with open(file_name, "r") as file:
        content = file.read()
        print(f"content: {content}")

def editing():
    file_name = input("Enter file name: ")

    with open(file_name, "r") as file:
        old_content = file.read()
        print(f"Old content: {old_content}")

    with open(file_name, "w") as file:
        content = input("Enter new file content: ")
        file.write(content)

        print(f"{file_name} was editted successfully")

while handling:
    print("-" * 15)
    print("[1] Create a file")
    print("[2] Delete a file")
    print("[3] View a file")
    print("[4] Edit a file")
    print("[5] Exit")
    print("-" * 15)

    choice = int(input("Enter service: "))

    if choice == 1:
        path = input("Choose path: ")
        os.chdir(path)
        creating()
    elif choice == 2:
        path = input("Choose path: ")
        os.chdir(path)
        deleting()
    elif choice == 3:
        path = input("Choose path: ")
        os.chdir(path)
        viewing()
    elif choice == 4:
        path = input("Choose path: ")
        os.chdir(path)
        editing()
    elif choice == 5:
        handling = False