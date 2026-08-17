a = [1,4,5,3,6,7,8,9]
target = 7
i = 0          #starting of window
current_sum = 0
max_len = 0
subarray = []

for j in range(len(a)):
    current_sum += a[j]

    while current_sum > target :
        current_sum -= a[i]
        i -= 1

    length = j - i + 1

    if length > max_len:
        max_len = length
        subarray = a[i : j + 1]
print(max_len)
print(subarray)