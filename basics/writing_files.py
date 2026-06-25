# (.txt, .json, .csv)

# employees = ["eugene", "squidward", "spongebob", "patrick"]

# import json
import csv

employees = [["name", "age", "job"],
            ["spongebob", 30, "cook"],
            ["patrick", 27, "unemployment"],
            ["sandy", 25, "scientist"]]

# txt_data = "i like pizza"

file_path = "C:/Users/CM/Desktop/nigga.csv"

try:
    with open(file_path, "w", newline="") as file:
        # for employee in employees:
            # file.write(employee + " ")
        # json.dump(employee, file, indent=4)
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")

except FileExistsError:
    print("file exists")
