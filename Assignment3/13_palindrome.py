str = "madam"
i = 0
while i < len(str) /2:
    if str[i] != str[len(str) - 1 - i]:
        print(f"{str} is not palindrome")
    else:
        print(f"{str} is palindrome")
        break