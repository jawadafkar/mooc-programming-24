# Write your solution here
def spruce(size):
    space = size - 1
    star = 1
    print("a spruce!")
    while size > 0:
        print((size-1) * " " + star * "*")
        size -= 1
        star += 2
    print(space * " " + "*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)