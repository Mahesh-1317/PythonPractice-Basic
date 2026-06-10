with open('FileHandling/student.txt','w') as f:
    f.write('Karishma Kapoor, 67, Moscow\n')
    f.write('Salman Khan, 35, UAE\n')
    f.write('Katappa, 99, Mahishmati\n')

with open('FileHandling/student.txt','a') as f:
    f.write('Mogembo, 98, Delhi.\n')

with open('FileHandling/student.txt','r') as f:
    content = f.read()
print(content)

with open ("FileHandling/student.txt", 'r') as f:
    for line in f:
        name, marks, city = line.strip().split(',')
        print(f'{name:<15} | {marks:>5} | {city}')
        print('-------------')