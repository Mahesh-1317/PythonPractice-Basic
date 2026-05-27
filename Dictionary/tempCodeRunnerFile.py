
print(dict.keys())
for key in dict.keys():
    print(key, "->",dict[key])

for key,value in dict.items():      
    print(key, "->",value)

print(dict.items())
print(dict.values())

copy_dict = dict.copy()
print("copy_dict:", copy_dict)