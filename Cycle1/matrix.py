print("**********************************")
print("SJC22MCA-2034")
print("J SIDDHARTH")
print("BATCH: 2022-2024")
print("**********************************")
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix1 = []
matrix2 = []

print("Enter elements for the first matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at row {i + 1}, column {j + 1}: "))
        row.append(element)
    matrix1.append(row)

print("Enter elements for the second matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at row {i + 1}, column {j + 1}: "))
        row.append(element)
    matrix2.append(row)

result_matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        sum_element = matrix1[i][j] + matrix2[i][j]
        row.append(sum_element)
    result_matrix.append(row)

print("Sum of the matrices:")
for row in result_matrix:
    print(row)
