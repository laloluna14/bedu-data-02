import csv

FILENAME = 'employees.csv'

with open (FILENAME) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # print(type(row))
        # print(row)
        # print(row['Name'])
        salary = row.get('Salary')
        if salary:
            salary_with_taxes = float(salary) * 1.35
            print(salary_with_taxes)
