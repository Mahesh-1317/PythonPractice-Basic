dict = {
    "Katappa": "Bahubali",
    "Gabbar": "Sambha",
    "Mogembo": "Shakha"
}
rollNum = {'Krish': 177, 'Jatin': 150}
empty_dict = {}

print(dict)
print(type(dict))
print(rollNum)
print(type(rollNum))
print(empty_dict)
print(type(empty_dict))

print(dict["Katappa"])    
print(rollNum["Jatin"])


words = ['Katappa','Mogembo','Gabbar']
for word in words:
    if word in dict:
        print(word, "->", dict[word])
    else:
        print("Rahne de...")