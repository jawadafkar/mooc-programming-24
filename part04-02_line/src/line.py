# Write your solution here
def line(num, sym):
    if sym != "":
        print(num * sym[0])
    else:
        print(num * "*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "LOL")