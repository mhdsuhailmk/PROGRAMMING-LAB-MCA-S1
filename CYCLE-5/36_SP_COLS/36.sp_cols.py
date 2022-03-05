import csv
with open("file1.csv","r") as f1:
    csvrdr=csv.reader(f1)
    for row in csvrdr:
        print(row[1],row[0])
        