print("**********************************")
print("SJC22MCA-2034")
print("J SIDDHARTH")
print("BATCH: 2022-2024")
print("**********************************")
elements = input("Enter elements separated by spaces: ").split()
elements = [int(e) for e in elements]

n = len(elements)
for i in range(n):
    swapped = False

    for j in range(0, n - i - 1):
        if elements[j] > elements[j + 1]:
            elements[j], elements[j + 1] = elements[j + 1], elements[j]
            swapped = True
    if not swapped:
        break
print("Sorted list:", elements)
