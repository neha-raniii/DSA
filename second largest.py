"""Q6. Second Largest Element
Array: [10, 5, 8, 20, 15]
Output: 15"""

a = [10, 5, 8, 20, 15]
largest = a[0]
second = a[1]

for i in range(len(a)):
    if a[i] > largest:
        second = largest
        largest = a[i]
        
    elif a[i] > second and second != largest:
        second = a[i]
print(largest)
print(second)