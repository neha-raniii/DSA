arr = [1, 2, 3, 2, 1]
i = 0 
j = len(arr) - 1
while i< j:
    if arr[i] != arr[j]:
        print("not palindrome")
        break
    i +=1
    j -= 1
else:
    print("palindrome")