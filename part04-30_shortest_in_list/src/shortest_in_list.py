# Write your solution here
def shortest(list):
    shortest = list[0]
    length = len(list[0])
    for item in list:
        if length > len(item):
            shortest = item
            length = len(item)
    return shortest

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)
