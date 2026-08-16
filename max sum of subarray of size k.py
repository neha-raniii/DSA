"""
finding maximum sum of subarray of size k using fixed window technique(sliding window) """

a =  [1,5,3,5,6,7,8,9,4,5]
k = int(input("enter the size of window"))   #size of window

current_sum = sum(a[ : k])   #finds first window sum
max_sum = current_sum
window = a[ : k]

for i in range(k,len(a)):   
    current_sum = current_sum + a[i] - a[i - k]    #current sum of  subarray of size k , then remove first old element of window and add new number of window
    if max_sum < current_sum:
        max_sum = current_sum
        window = a[i-k+1:i+1]
print(max_sum)
print("subarray : " , window)
