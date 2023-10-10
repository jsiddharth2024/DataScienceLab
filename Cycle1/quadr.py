import math
print("**********************************")
print("SJC22MCA-2034")
print("J SIDDHARTH")
print("BATCH: 2022-2024")
print("**********************************")
a= int(input("Enter coefficent of x^2:"))
b= int(input("Enter coefficent of x:"))
c= int(input("Enter constant:"))
d= b * b - (4 * a * c)
if d >= 0:
    x1= float(-b + math.sqrt(d)) / (2 * a)
    x2= float(-b - math.sqrt(d))/ (2 * a)
    print(f"Root 1:{x1:.2f}")
    print(f"Root 2:{x2:.2f}")
else:
    print("Invalid roots")