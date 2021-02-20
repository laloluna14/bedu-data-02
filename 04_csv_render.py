import csv

FILENAME = 'employees.csv'

with open (FILENAME) as csv_file:
    csv_reader = csv.reader(csv_file)
    # print(csv_reader)
    for row in csv_reader:
        # print(type(row))
        # print(row)
        print(row[2])