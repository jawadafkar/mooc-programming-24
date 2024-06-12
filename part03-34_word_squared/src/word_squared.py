# Write your solution here
def squared(string, num):
    square = string * num*num
    i = 0
    while num*num > i:
        print(square[i:i+num])
        i += num

if __name__ == "__main__":
    squared("python", 15)