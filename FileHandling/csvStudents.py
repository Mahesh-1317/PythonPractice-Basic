import csv

records = [
    ['Name', 'Age', 'Math_marks','Sci_marks','Eng_marks'],
    ['Rahul', 17, 89, 56,47],
    ['Peter',18, 67, 98,37],
    ['John', 20, 35, 67,90]
]

with open('FileHandling/records.csv', 'w', newline='') as f:
    csv.writer(f).writerows(records)

name = input("Enter student's name:")
found  = False

with open('FileHandling/records.csv', 'r') as f:
    for row in csv.DictReader(f):
        if row["Name"] == name:
            print(f'Found {name}')
            print(f'{row["Name"]}: {row["Age"]}, Marks:  Maths = {row["Math_marks"]} Science = {row["Sci_marks"]} English = {row["Eng_marks"]}')
            found = True
            break

if not found:
    print("Student not found!")