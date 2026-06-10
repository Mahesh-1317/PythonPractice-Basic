s = 'abcdef'
str = 'axttxa'
i = 0
is_palindrome = True
while i < len(s) / 2:
    if s[i] != s[len(s) - i - 1]:
        is_palindrome = False
        break
    i += 1

print(is_palindrome) 

print()
while i < len(str) / 2:
    if str[i] != str[len(str) - i - 1]:
        print(f'{str} is not palindrome')
    else:
        print(f'{str} is palindome')
    break