#palindrome is a word ,string or number which the same from forward and backward

s= input("enter a string\n")
left = 0
right = len(s)-1
while left<right:
    if s[left] != s[right]:
        print("Not palindrome")
        break
    left += 1
    right -= 1
else:
    print("palindrome")

"""time complexity= O(n)
space complexity=O(1)"""