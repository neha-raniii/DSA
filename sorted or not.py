"""Q8. Check if Array is Sorted
Array: [1, 2, 3, 4, 5]
Output: True"""

a = [1, 2, 3, 4, 5]
sort = True
for i in range(1 , len(a)):
    if  a[i-1] > a[i]:
        sort = False
        
      
if sort == False:
        print(" not  sorted")
else:
        print("sorted")



