# Write your solution here
def palindromes(string):
    reversed = string[::-1]
    return string == reversed

def main():
    while True:
        string = input("Please type in a palindrome: ")
        p = palindromes(string)
        if not p:
            print("that wasn't a palindrome")
        else:
            print(string, "is a palindrome!")
            break
main()
# Note, that at this time the main program should not be written inside
#if __name__ == "__main__":
