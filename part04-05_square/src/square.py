# Copy here code of line function from previous exercise
def line(num, sym):
    if sym != "":
        print(num * sym[0])
    else:
        print(num * "*")

def square(size, character):
    # You should call function line here with proper parameters
    i = 0
    while size > i:
        line(size, character)
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")