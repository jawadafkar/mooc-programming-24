# Write your solution here
def sum_of_positives(list):
    sum = 0
    for item in list:
        if item > 0:
            sum += item
    return sum


if __name__ == "__main__":
    my_list = [-1, -2, 5, 10, 15, 12]
    result = sum_of_positives(my_list)
    print(result)