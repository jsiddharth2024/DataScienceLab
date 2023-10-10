print("**********************************")
print("SJC22MCA-2034")
print("J SIDDHARTH")
print("BATCH: 2022-2024")
print("**********************************")
input_string = input("Enter a string: ")

vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

input_string = input_string.lower()

for char in input_string:
    if char in vowel_counts:
        vowel_counts[char] += 1

for vowel, count in vowel_counts.items():
    print(f'{vowel}: {count}')
