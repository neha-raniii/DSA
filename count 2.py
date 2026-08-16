"""Q4. Count the number of even and odd elements.
Example: [2, 7, 4, 9, 6, 3]
Output: Even = 3, Odd = 3"""

a = [2, 7, 4, 9, 6, 3]
odd = []
even = []

for i in range(len(a)):
    if a[i] % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])
print(len(odd))
print(len(even))