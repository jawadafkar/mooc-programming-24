# Write your solution here
def list_sum(list1, list2):
    i = 0
    sum = []
    length = len(list1)
    while length > i:
        new = list1[i] + list2[i]
        sum.append(new)
        i += 1
    return sum

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]