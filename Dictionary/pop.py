dict = {"kwait": "flower"}
dict.update({"gleba":"soil"})
print(dict)

dict.popitem()
print(dict)

if "flower" in dict:
    print("Yes")
else:
    print("Nahi re..")