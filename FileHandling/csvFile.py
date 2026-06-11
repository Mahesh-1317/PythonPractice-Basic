import csv
records = [
    ['Name', 'Marks', 'City', 'Grade'],
    ['Rahul', 47, 'Rom', 'D'],
    ['Peter', 77, 'Rom', 'B'],
    ['John', 90, 'Rom', 'A']
]

with open('FileHandling/students.csv', 'w', newline='') as f:
    csv.writer(f).writerows(records)

with open('FileHandling/students.csv', 'r') as f:
    for row in csv.DictReader(f):
        print(f'{row['Name']}: {row['Marks']} marks ({row['City']})')