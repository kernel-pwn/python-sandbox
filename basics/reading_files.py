# (.txt, .json, .csv)

#import json
import csv

file_path = "C:/Users/CM/Desktop/nigga.json"

try:
    with open(file_path, "r") as file:
        # content = file.read()
        # content = json.load(file)
        # print(content["name"])
        content = csv.reader(file)
        for row in content:
            print(row)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")