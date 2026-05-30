beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print(beatles)

newMenbers = ["Stu Sutcliffe","Pete Best"]
for i in newMenbers:
    beatles.append(i)
print(beatles)

del beatles[-2]
del beatles[-1]
print(beatles)

beatles.insert(0,"Ringo Starr")
print(beatles)