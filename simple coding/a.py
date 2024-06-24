def print_alphabet_pyramid(rows):
    # ASCII value of 'A' is 65
    start_char = 65
    for i in range(rows):
        # Print leading spaces
        print(" " * (rows - i - 1), end="")
        # Print alphabets
        for j in range(i + 1):
            print(chr(start_char + j), end=" ")
        for j in range(i - 1, -1, -1):
            print(chr(start_char + j), end=" ")
        print()

# Example usage
rows = 5  # You can adjust this value to change the height of the pyramid
print_alphabet_pyramid(rows)
