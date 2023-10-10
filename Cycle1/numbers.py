print("**********************************")
print("SJC22MCA-2034")
print("J SIDDHARTH")
print("BATCH: 2022-2024")
print("**********************************")


def sum_of_digits(n):
    # Function to calculate the sum of digits of a number
    return sum(int(digit) for digit in str(n))


num = int(input("Enter a positive number: "))

while num > 0:
    digit_sum = sum_of_digits(num)
    print(f"{num} - {digit_sum} = {num - digit_sum}")
    num -= digit_sum

print("Result is positive.")
