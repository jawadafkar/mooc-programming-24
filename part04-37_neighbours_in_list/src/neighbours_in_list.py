# Write your solution here
def longest_series_of_neighbours(list):
    count = 1
    longest = count
    for i in range(1, len(list)):

        if abs(list[i] - list[i-1]) == 1:
            count += 1
        else:
            count = 1
        longest = max(count, longest)
        i += 1
    return longest

if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(my_list))