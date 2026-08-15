"""
maximum sum of subarray with negative values 
used brute force apprach only for practice"""

arr = [1,3,-1,4,5,-2,-8,5]
max_sum = arr[0]

for i in range(len(arr)):
    curret_sum= 0
    for j in range(i,len(arr)):
        curret_sum += arr[j]
        if max_sum < curret_sum:
            max_sum = curret_sum
print(max_sum)