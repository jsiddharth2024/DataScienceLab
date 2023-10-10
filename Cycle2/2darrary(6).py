import numpy as np

print("**********************************")
print("SJC22MCA-2034")
print("J SIDDHARTH")
print("BATCH: 2022-2024")
print("**********************************")

# Create a 4x4 array
array_2d = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12],
                     [13, 14, 15, 16]])

# a. Display all elements excluding the first row
print("a. All elements excluding the first row:")
print(array_2d[1:])

# b. Display all elements excluding the last column
print("\nb. All elements excluding the last column:")
print(array_2d[:, :-1])

# c. Display the elements of 1st and 2nd column in 2nd and 3rd row
print("\nc. Elements of 1st and 2nd column in 2nd and 3rd row:")
print(array_2d[1:3, :2])

# d. Display the elements of 2nd and 3rd column
print("\nd. Elements of 2nd and 3rd column:")
print(array_2d[:, 1:3])

# e. Display 2nd and 3rd element of 1st row
print("\ne. 2nd and 3rd element of 1st row:")
print(array_2d[0, 1:3])

# f. Display the elements from indices 4 to 10 in descending order
print("\nf. Elements from indices 4 to 10 in descending order:")
print(array_2d.flatten()[4:11][::-1])
