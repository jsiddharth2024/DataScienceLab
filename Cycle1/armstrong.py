print("**********************************")
print("SJC22MCA-2034")
print("J SIDDHARTH")
print("BATCH: 2022-2024")
print("**********************************")
def is_armstrong_number(n):

    num_digits = len(str(n))
    sum_of_powers = sum(int(digit) ** num_digits for digit in str(n))
    return n == sum_of_powers

for num in range(1, 1001):
    if is_armstrong_number(num):
        print(num)