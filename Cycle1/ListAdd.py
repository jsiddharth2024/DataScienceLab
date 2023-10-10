print("**********************************")
print("SJC22MCA-2034")
print("J SIDDHARTH")
print("BATCH: 2022-2024")
print("**********************************")
limit = int(input("Enter the limit:"))
list1 = []
list2 = []
for i in range(limit):
    l1 = int(input("Enter list 1 element:"))
    list1.append(l1)
print("\n")
for i in range(limit):
    l2 = int(input("Enter list 2 element:"))
    list2.append(l2)
res = []
for i in range(limit):
    res.append(list1[i] + list2[i])
print("The sum of List are:")
print(res)
