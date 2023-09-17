'''You are tasked with a complex matrix operation. You will need to input the size of the matrix 
and then provide the elements of the matrix.
The main matrix must then be divided into two sub matrices one for even indexed and one for
the odd indexed elements.
Following this you are required to sort both the even and odd matrices in ascending order.
Finally you must calculate and print the sum of the second largest numbers from both the
matrices.'''
import numpy as np 
def Sumoflargest(array):
    if(len(array)>4):
        even=[]
        odd=[]
        for i in range(len(array)):
            if(i%2==0):
                even.append(array[i])
            else:
                odd.append(array[i])
        even.sort()
        odd.sort()
        return even[-2]+odd[-2]
    else:
        return "Invalid Array"
ls=np.array([1,2,3])
print(Sumoflargest(ls))
