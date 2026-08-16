"""
Q3. Count how many positive, negative and zero elements are present.
Example: [2, -1, 0, 5, -3, 0]
Output: Positive = 2, Negative = 2, Zero = 2
"""
a =  [2, -1, 0, 5, -3, 0]
pos = []
neg = []
zero = []

for i in range(len(a)):
    if a[i] > 0 :
        pos.append(a[i])
    elif a[i] < 0 :
        neg.append(a[i])
    else :
        zero.append(a[i])
print(len(pos))
print(len(neg))
print(len(zero))
