# str = "Reverse"
# for i in  range(len(str)-1,-1,-1):
#     print(str[i],end="")

def reverse(str):
    rev = ""
    for i in str:
        rev = i + rev
    return rev
print(reverse("reverse"))