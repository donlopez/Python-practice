num_rows = int(input())
num_columns = int(input())

# Outer loop for rows
for i in range(1, num_rows + 1):
    # Inner loop for columns
    for j in range(num_columns):
        # chr(65) is 'A', so adding j to 65 gives the letters in sequence
        print(f'{i}{chr(65 + j)}', end=' ')
    print()  # This will move to the next line after each row is completed
