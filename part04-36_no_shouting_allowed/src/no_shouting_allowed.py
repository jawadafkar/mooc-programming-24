# Write your solution here
def no_shouting(list):
    pruned_list = []
    for item in list:
        if not item.isupper():
            pruned_list.append(item)
    return pruned_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)