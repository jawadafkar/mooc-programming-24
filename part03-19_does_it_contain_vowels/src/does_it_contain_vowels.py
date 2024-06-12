# Write your solution here
string = input("Please type in a string: ")
vowels = "aeo"
i = 0

while len(vowels) > i:
    vowel = vowels[i]
    if vowel in string:
        print(vowel, "found")
    else:
        print(vowel, "not found")
    i += 1