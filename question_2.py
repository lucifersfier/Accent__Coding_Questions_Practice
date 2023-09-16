# Execute the given function.
'''def LargeSmallSum(arr)
The function takes an integral arr which is of the size or length of its arguments. Return the 
sum of the second smallest element at odd position ‘arr’ and the second largest element at the 
even position.
Assumption
o Every array element is unique.
o Array is 0 indexed.
Note:
o If the array is empty, return 0.
o If array length is 3 or <3, return 0.
Example
Input:
Arr: 3 2 1 7 5 4
Output:
7
'''

#****************************************************#

import numpy as np
def LargeSmallSum(arr):
    if len(arr)<=3 :
        return 0
    evn_list = []
    odd_list = []
    for i in range(len(arr)):    
        if(i%2==0):
            evn_list.append(arr[i])
        else:
            odd_list.append(arr[i])
    evn_list.sort()
    odd_list.sort()
    print(evn_list)
    print(odd_list)
    x = evn_list[-2]
    y = odd_list[1]
    print("The Second largest element at even position is : ",x)
    print("The Second smallest element at odd position is : ",y)
    print(x+y)
z = np.array([3,2,1,7,5,4])
LargeSmallSum(z)
a = np.array([1,2,3,4,5,6,7,8,9])
b = np.array([3,2,5,6,7,1,7,5,4])
c = np.array([3,2,1,7,5,45,6,7,1])
d = np.array([3,2,1,7,5,4.76,32,13,56,43,21])
print("Result Of array a")
LargeSmallSum(a)
print("Result Of array b")
LargeSmallSum(b)
print("Result Of array c")
LargeSmallSum(c)
print("Result Of array d")
LargeSmallSum(d)

