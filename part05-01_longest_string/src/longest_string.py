# Write your solution here
def longest(strings: list):
    longest_length = len(strings[0])
    longest_name = strings[0]
    for name in strings:
        if len(name)>longest_length:
            longest_length = len(name)
            longest_name = name
    return longest_name


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))