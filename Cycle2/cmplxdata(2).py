import numpy as np

print("**********************************")
print("SJC22MCA-2034")
print("J SIDDHARTH")
print("BATCH: 2022-2024")
print("**********************************")

two_dim_array = np.array([[1.1 + 2j, 3.2 + 4j, 5.1 + 6j], [7.6 + 8j, 9.2 + 10j, 11.1 + 12j]], dtype=complex)

print("2D Array:")
print(two_dim_array)
num_rows, num_cols = two_dim_array.shape
print(f"\na. Number of rows: {num_rows}")
print(f"b. Number of columns: {num_cols}")

dimension = two_dim_array.ndim
print(f"c. Dimension of the array: {dimension}")

reshaped_array = two_dim_array.reshape(3, 2)
print("\nReshaped Array (3x2):")
print(reshaped_array)
