# Write your solution here
def chessboard(size):
    i = 0
    cell = "1"
    row = ""
    while size > i:
        j = 0
        while size > j:
            row += cell
            if cell == "1":
                cell = "0"
            else:
                cell = "1"
            j += 1
        if row[0] == "1":
            cell = "0"
        else:
            cell = "1"
        print(row)
        row = ""
        i += 1
            

# Testing the function
if __name__ == "__main__":
    chessboard(4)
