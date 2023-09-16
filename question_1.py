# Question Number --1 
'''1. Execute the given function.
def differenceofSum(n.m)
The function takes two integrals m and n as arguments. You are required to obtain the total of 
all integers ranging between 1 to n (both inclusive) which are not divisible by m. You must 
also return the distinction between the sum of integers not divisible by m with the sum of 
integers divisible by m.
Assumption
o m > 0 and n > 0
o Sum lies within the integral range'''
#********************************************#
sum1=0
sum2=0
def differenceofSum(n,m):
    sum1=0
    sum2=0
    for i in range(n+1):
        if(i%m==0):
            sum1=sum1+i
        else:
            sum2=sum2+i
    return sum2-sum1
print(differenceofSum(30,6))
print(differenceofSum(10,3))


            
        