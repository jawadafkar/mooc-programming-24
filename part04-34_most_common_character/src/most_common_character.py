# Write your solution here
def most_common_character(string):
    most = string[0]
    occured = 0
    for character in string:
       if string.count(character) > occured:
           occured = string.count(character)
           most = character
    return most

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
