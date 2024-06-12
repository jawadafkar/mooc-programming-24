def print_square(layers):
    # Ensure layers is an integer and within the valid range
    if not isinstance(layers, int) or layers < 1 or layers > 26:
        raise ValueError("Layers must be an integer between 1 and 26")

    # Create a list of letters
    letters = [chr(i + 64) for i in range(layers)]

    # Calculate the length of the square side
    side_length = 2 * layers - 1

    # Create the square
    square = []
    for i in range(side_length):
        row = []
        for j in range(side_length):
            # Calculate the distance from the center
            distance = min(abs(side_length // 2 - i), abs(side_length // 2 - j))
            row.append(letters[distance])
        square.append(''.join(row))

    # Print the square
    for row in square:
        print(row)

# Ask for user input
try:
    layers = int(input("Enter the number of layers (1-26): "))
    print_square(layers)
except ValueError:
    print("Invalid input. Please enter an integer between 1 and 26.")
