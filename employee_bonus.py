import csv

with open("customers.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    first_name_index = header.index("FirstName")
    last_name_index = header.index("LastName")
    country_index = header.index("Country")

    data = []
    for values in reader:
        data.append([values[first_name_index], values[last_name_index], values[country_index]])

print(data)
