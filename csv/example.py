import csv

with open("example.csv", "r") as f:
    r = csv.reader(f)
    for row in r:
        print(row)

with open("example.csv", "r") as f:
    r = csv.DictReader(f)
    for row in r:
        print(row)