#! python
import csv

f = open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row

f.close()

values =[[1, 2, 3], [1, 2, 3]]
with open('hosts.csv', "w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(values)

with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{}, {}".format(row['name'], row['users'])))

users = [{"name": "1", "username": "2", "department": "3"},
            {"name": "1", "username": "2", "department": "3"},
            {"name": "1", "username": "2", "department": "3"}]
keys = ["name", "username", "deparment"]
with open('by_department.csv') as by_department:
    writer = csv.DictWriter(by_department, fieldnames = keys)
    writer.writeheader()
    writer.writerows(users)