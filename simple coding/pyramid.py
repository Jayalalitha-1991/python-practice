def print_pyramid(rows):
    for i in range(rows):
        # Print leading spaces
        print(" " * (rows - i - 1), end="")
        # Print asterisks
        print("*" * (2 * i + 1))

# Example usage
rows = 5  # You can adjust this value to change the height of the pyramid
print_pyramid(rows)
