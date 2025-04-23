import csv

data = [
    ['Roll No', 'Name', 'Subject1', 'Subject2', 'Subject3'],
    [101, 'Alice', 85, 90, 88],
    [102, 'Bob', 78, 82, 89],
    [103, 'Charlie', 92, 88, 91]
]

f = open('students.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerows(data)
f.close()
