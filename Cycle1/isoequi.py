print("**********************************")
print("SJC22MCA-2034")
print("J SIDDHARTH")
print("BATCH: 2022-2024")
print("**********************************")
side1=int(input("Enter 1st side:"))
side2=int(input("Enter 2nd side:"))
side3=int(input("Enter 3rd side:"))
if side1 == side3 == side2:
    print("The given triangle is equilateral")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("The given triangle is isoceles")
else:
    print("The given triangle is scalene")