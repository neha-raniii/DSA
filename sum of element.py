"""Q5. Find the sum of all elements in an array.
Example: [2, 5, 3, 7] → 17"""
a = [2, 5, 3, 7] 
sum = 0
for i in range(len(a)):
    sum += a[i]

print(sum)
