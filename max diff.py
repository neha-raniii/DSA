"""Q10. Find Maximum Difference
Array: [2, 7, 1, 8, 4]
Output: 7
Because 8 - 1 = 7."""
a = [2, 7, 1, 8, 4]

smallest = a[0]
largest = a[0]

for i in range(len(a)):
    if a[i] < smallest:
        smallest = a[i]

    if a[i] > largest:
        largest = a[i]

difference = largest - smallest

print(difference)
