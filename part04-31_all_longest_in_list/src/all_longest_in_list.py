# Write your solution here
def all_the_longest(list):
    new_list = []
    longest = len(list[0])
    
    for item in list:
        if len(item) > longest:
            longest = len(item)
    
    for item in list:
        if len(item) == longest:
            new_list.append(item)
    return new_list


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']