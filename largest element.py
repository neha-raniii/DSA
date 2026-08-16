a = [3, 7, 2, 9, 4]
max = a[0]

for i in range(len(a)):
    if max < a[i]:
        max = a[i] 
print(max)
