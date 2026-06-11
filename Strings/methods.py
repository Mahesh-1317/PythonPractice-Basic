text = '   Hello Python Programmer   '

# Replace
print(text.replace('Python', 'Anaconda'))

# Split and Join 
csv = 'Rahul,22,Indore,Engineer'
text1 = csv.split(',')
print(text1)
print(text1[2])
text2 = '  |  '.join(text1)
print(text2)

# Check content
print('hello12'.isalnum())
print('12350'.isdigit())
print('Python'.isalpha())
print('   '.isspace())

#   Start/End check
email = "myusername@gmaail.com"
print(email.startswith('my'))
print(email.endswith('.com'))