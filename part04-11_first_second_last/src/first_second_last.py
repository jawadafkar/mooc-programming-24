# Write your solution here
def first_word(string):
    char = ""
    word = ""
    i = 0

    while char != " ":
        word += char
        char = string[i]
        i += 1

    return word

def second_word(string):
    i = 0
    word = ""
    char = ""
    
    while string[i] != " ":
        i += 1
    
    i += 1

    while char != " " and i < len(string):
        
        char = string[i]
        if char != " ":
            word += char
        i += 1   
    
    return word

def last_word(string):
    
    word = ""
    i = len(string) - 1
    
    while string[i] != " ":
        i -= 1
    
    i += 1
    
    while i < len(string):
        word += string[i]
        i += 1
    return word
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))