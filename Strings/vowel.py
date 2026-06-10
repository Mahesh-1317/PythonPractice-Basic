str = 'Hello, how are YOU doing today?'
Vowel = {'a','e','i','o','u','A','E','I','O','U'}

count = 0
for vowel in str:
    if vowel in Vowel:
        count += 1
print(count)

print(str[15:18])
print(str[::-1])