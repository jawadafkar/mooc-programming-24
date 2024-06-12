# Write your solution here
def list_of_stars(list):
    for item in list:
        print(item * "*")

if __name__ == "__main__":
    list_of_stars([2, 3, 4, 5, 6])