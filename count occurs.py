"""
Q9. Count Frequency of an Element
Array: [2, 5, 2, 8, 2, 7, 5]
Target: 2
Output: 3"""

a = [2, 5, 2, 8, 2, 7, 5]
target = 2
count = []

for i in range(len(a)):
    if a[i] == target:
        count.append(a[i])
print(len(count))


