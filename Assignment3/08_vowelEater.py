user_word = input("Enter a character or string: ")
user_word = user_word.upper()
print(user_word)
word_without_vowel = ""

for i in user_word:
    if i == 'A':
        continue
    elif i == 'E':
        continue
    elif i == 'I':
        continue
    elif i == 'O':
        continue
    elif i == 'U':
        continue
    else:
        word_without_vowel += i
print("Word without vowel: ",word_without_vowel)