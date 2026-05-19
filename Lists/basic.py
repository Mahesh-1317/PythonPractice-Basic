list = [1,5,"Gabbar","c"]
print(list)
print(type(list))
print(list[2])
print(list[0])

#Updation in list
list[1] = "Samba"
print("list[1]: ",list[1])
print(list)

#Copy element
list[2] = list[1]
print(list)

#Length, deletion and neg index
print(len(list))
del list[2]
print(len(list))
print(list)
print(list[-1])

#append() and insert() methods
list.append(7.4)
print(list)
list.insert(0,9)
print(list)