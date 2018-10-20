m = input("Please enter the number of rows: ")
n = input("Please enter the number of elements in each row: ")

elements = input("Please enter each element seperated by a space: \n")

elements = elements.split()

matrix = []

for y in range(int(m)):
    imatrix = []
    for x in range(int(n)):
        imatrix.append(elements.pop(0))
    matrix.append(imatrix)

print(matrix)
=======

matrix = [[2.0, 3.0, 4.0, 0], 
          [1.0, -4.0, 3.0, 4.0], 
          [2.0, 5.0, -2.0, 3.0]]

# m x n is m rows by n columns
m = len(matrix)
n = len(matrix[0])

# Gets the matrix into row-echelon form
for i in range(n - 1):
    for j in range(i + 1, m):
        a = matrix[j][i] / matrix[i][i]
        
        for k in range(n):
            matrix[j][k] -= a * matrix[i][k]

    # Make the current row all 1s
    multiplier = matrix[i][i]
    for j in range(n):
        matrix[i][j] /= multiplier

# Gets the matrix into RREF

# Iterate through columns
for i in range(n - 1, 0, -1):
    for j in range(i - 1):
        mult = matrix[j][i - 1]

        for k in range(n):
            matrix[j][k] -= matrix[i - 1][k] * mult

# Print the matrix
for row in matrix:
    for element in row:
        print(element, end=' ')

    print()
