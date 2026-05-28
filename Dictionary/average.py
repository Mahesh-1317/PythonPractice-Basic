student = {}
while True:
    name = input("Enter name of student: ")
    if name == '':
        break   
    score  = int(input(f"Enter {name}'s score:"))
    if score not in range(1,11):
        break

    if name in student:
        student[name] += (score,)
    else:
        student[name] = (score,)

print(student)

for name,marks in student.items():
    sum = 0
    for mark in marks:
        sum += mark
    print(name, "->", sum / len(marks))