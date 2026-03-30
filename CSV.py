import csv

try:
    with open("sample.csv", "r") as file:
        reader = csv.reader(file)

        count = 0

        for row in reader:
            count = count + 1

    print("Total number of rows:", count)

except FileNotFoundError:
    print("File not found!")