import csv

with open("EmployeePay.csv","r") as printfile:
    reader = csv.reader(printfile)
    #next(reader)
    for row in reader:
        print(row)

file = open("EmployeePay.csv","r")
reader = csv.reader(file)
print(file)
printfile.close()