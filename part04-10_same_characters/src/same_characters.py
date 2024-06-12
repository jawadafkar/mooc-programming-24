# Write your solution here
def same_chars(string, a, b):
    length = len(string)
    if a >= length or b >= length:
        return False
    elif string[a] == string[b]:
        return True
    return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("codero", 1, 2))