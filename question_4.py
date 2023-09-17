#            Perform the following function.
#            def Productsmallpair(sum,arr)
#            This function accepts the integers sum and arr.
#            It is used to find the arr(j) and arr(k), where k ! = j.
#            arr(j) and arr(k) should be the smallest elements in the array.
'''Keep this in mind:
o If n<2 or empty, return –1.
o If these pairs are not found, then return to zero.
o Make sure all the values are within the integer range.
Example
Input:
Sum: 9
Arr: 5 4 2 3 9 1 7
Output:
2
'''
import numpy as np
def Productsmallpair(summ,arr):
    arr.sort()
    x=arr[0]
    y=arr[1]
    product=x*y
 
    if(x+y<summ):
        return product
        
ls=np.array([5,4,2,3,9,1,7])
summ=9
print(Productsmallpair(summ,ls))