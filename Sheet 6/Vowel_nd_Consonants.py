# a = input("Enter a string to check: ")
# vowels = 0
# consonants = 0
# for ch in a:
#     if ch.isalpha():
#         if ch in 'aeiou':
#             vowels+=1
#         else:
#             consonants+=1
# print("Vowels:",vowels)
# print("Consonants:",consonants)



a = input("String daalo: ")
vowels = 0
consonants = 0
for ch in a:
    if ch.isalpha():
        if ch in "aeiou":
            vowels+=1
        else:
            consonants+=1
print("Vowels-",vowels)
print("Consonants-",consonants)