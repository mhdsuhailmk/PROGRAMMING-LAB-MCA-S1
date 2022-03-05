import csv

d={1:'XIANY',2:'ZHUY',3:'KLUWA',4:'ZIANKY'}

with open("file1.csv","w") as f1:
    csvrdr=csv.writer(f1)
    for item in d.items():
        csvrdr.writerow(item)

with open("file1.csv","r") as f1:
    csvrdr=csv.reader(f1)
    for row in csvrdr:
        print(" ".join(row))