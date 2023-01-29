customer_country

import csv

with open("customer.csv","r") as file1:
    reader = csv.reader(file1)

    with open("outputfile.csv","w", newline="") as file2:
        writer = csv.writer(file2)

        for row in reader:
            writer.writerow(row)
