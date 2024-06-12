# Write your solution here
def everything_reversed(list):
    new_list = []
    rev_list = list[::-1]
    for item in rev_list:
        new_list.append(item[::-1])
    return new_list

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)

