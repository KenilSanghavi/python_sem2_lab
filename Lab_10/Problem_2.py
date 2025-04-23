import csv

f = open('students.csv', 'r')
reader = csv.DictReader(f)
result = {}

for row in reader:
    rollno = row['Roll No']
    total = int(row['Subject1']) + int(row['Subject2']) + int(row['Subject3'])
    result[rollno] = {
        'name': row['Name'],
        'marks': [int(row['Subject1']), int(row['Subject2']), int(row['Subject3'])],
        'total': total
    }

f.close()

print(result)
