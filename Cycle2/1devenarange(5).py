import numpy as np

print("**********************************")
print("SJC22MCA-2034")
print("J SIDDHARTH")
print("BATCH: 2022-2024")
print("**********************************")

# Create a 1D array with the first 15 even numbers
even_numbers = np.arange(2, 31, 2)

# a. Elements from index 2 to 8 with step 2 (also demonstrate the same using slice function)
subset_a = even_numbers[2:9:2]
subset_a_slice = even_numbers[2:9:2]
print("a. Elements from index 2 to 8 with step 2:")
print(subset_a)
print("Slice Function Equivalent:")
print(subset_a_slice)

# b. Last 3 elements of the array using negative index
last_three = even_numbers[-3:]
print("\nb. Last 3 elements of the array using negative index:")
print(last_three)

# c. Alternate elements of the array
alternate_elements = even_numbers[::2]
print("\nc. Alternate elements of the array:")
print(alternate_elements)

# d. Display the last 3 alternate elements
last_three_alternate = even_numbers[-3::2]
print("\nd. Last 3 alternate elements:")
print(last_three_alternate)
