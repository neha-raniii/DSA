arr = [1, 3, 5, 8, 12]
k = 4
i = 0 
j = len(arr)- 1

while i < j:
    if arr[i]- arr[j]== k:
        print(arr[i],arr[j],"are two pairs")
        break
    elif arr[i] - arr[j] <  k:
        j -=1
    else:
        i += 1