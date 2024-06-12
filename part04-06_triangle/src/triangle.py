# Copy here code of line function from previous exercise
def line(num, sym):
    if sym != "":
        print(num * sym[0])
    else:
        print(num * "*")

def triangle(size):
    # You should call function line here with proper parameters
    i = 1
    while size >= i:
        line(i, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
