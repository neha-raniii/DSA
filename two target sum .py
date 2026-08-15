"""
Input:  [1, 2, 4, 6, 8, 7]
Target: 10
Output: [2, 8]
"""
arr = [1,2,4,6,8,7]
arr.sort()
target = 10
i = 0
j = len(arr)-1
while i< j :
    if arr[i]+arr[j]== target:
        print(arr[i], arr[j] ,"are two number sum")
        break
    elif arr[i] + arr[j] < target:
        i += 1

    else:
        j -= 1