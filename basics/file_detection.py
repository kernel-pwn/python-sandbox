import os

file_path = "C:\\Users\\CM\\Desktop/nigga.txt"

if os.path.exists(file_path):
    print(f"the location {file_path} exists")

    if os.path.isfile(file_path):
        print("that is a file")
    elif os.path.isdir(file_path):
        print("that is a directory")

else:
    print(f"the location {file_path} does not exist")