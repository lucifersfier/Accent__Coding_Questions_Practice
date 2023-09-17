#6.   Execute the function for the given purpose.
#     When the sum of the digits exceeds a total of 9, a carry digit is added to the right-left of the 
#     digit. Execute the function: Int Numberofcarry(Integer num 1, Integer num 2)
#Assumption
'''num1, num2 > = 0
Example
Input:
num1: 451
num2: 349
Output:
2'''

def Numberofcarry(n1,n2):
    count=0
    add=0
    x=n1%10 
    y=n2%10
    while(n1>0 or n2>0):
        n1=n1//10
        n2=n2//10
        if(x+y+add>9):
            count+=1
            add=1
        x=n1%10
        y=n2%10
    return count

print(Numberofcarry(451,349))
        