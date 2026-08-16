arr = [8, 3, 6, 1, 5]
smallest = arr[0]

for i in range(len(arr)):
    if smallest > arr[i]:
        smallest =  arr[i]
print(smallest)