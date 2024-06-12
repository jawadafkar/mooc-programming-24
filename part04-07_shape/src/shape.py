# Copy here code of line function from previous exercise and use it in your solution
def line(num, sym):
    if sym != "":
        print(num * sym[0])
    else:
        print(num * "*")

def shape(size, t, h, r):
    i = 1
    while size >= i:
        line(i, t)
        i += 1
    i = 0
    while h > i:
        line(size, r)
        i += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")