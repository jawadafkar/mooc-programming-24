# Write your solution here
def distinct_numbers(list):
    new_list = []
    old = -1
    for item in sorted(list):
        if item != old:
            new_list.append(item)
            old = item
    return new_list

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]