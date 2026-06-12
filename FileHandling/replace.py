with open("FileHandling/replace.txt", "w") as f:
    f.write('Hi everyone\nwe are learning File Handling\n')
    f.write('using Java.\nI like programming in Java.')

with open("FileHandling/replace.txt", "r") as f:
    data = f.read()
    print(data)

print()
new_data = data.replace('Java', 'Python')
print(new_data)

with open("FileHandling/replace.txt", "w") as f:
    f.write(new_data)

#   Search
print()
with open("FileHandling/replace.txt", "r") as f:
    data = f.read()
    if(data.find('learning') != -1):
        print("Found")
    else:
        print("Not found")

def check_line():
    word = 'Python'
    new_data = True
    line_no = 1

    with open("FileHandling/replace.txt", "r") as f:
        while new_data:
            new_data = f.readline()
            if(word in new_data):
                print(line_no)
                return
            line_no += 1
    return -1

print(check_line())