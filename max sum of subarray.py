"""
finding maximum sum of subarray using kadane's algorithmfo best optimization"""
arr = [3, -4, 5, 4, -1, 7, -8]
current_sum = arr[0]
max_sum = arr[0]

for i in range(1,len(arr)):
    current_sum = max(arr[i],current_sum + arr[i])
    max_sum = max(max_sum,current_sum)
print(max_sum)