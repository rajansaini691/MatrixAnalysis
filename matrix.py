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
