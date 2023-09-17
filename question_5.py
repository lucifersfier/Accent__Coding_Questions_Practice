#5. Perform the function for the given purpose.
#      For writing numbers, there is a system called N-base notation. This system uses only N-based symbols.
#      It uses symbols that are listed as the first n symbols. Decimal and n-based notations are
#      0:0, 1:1, 2:2, …, 10:A, 11:B, …, 35:Z.
'''Perform the function: Chats DectoNBase(int n, int num)
This function only uses positive integers. Use a positive integer n and num to find out the n-base that is equal to num.
Steps
o Select a decimal number and divide it by n. Consider this as an integer division.
o Denote the remainder as n-based notation.
o Again divide the quotient by n.
o Repeat the above steps until you get a 0 remainder.
o The remainders from last to first are the n-base values.'''
#Assumption
'''1 < n < = 36
Example
Input:
N: 12
Num: 718
Output:
4BA'''
def DectoNBase(n,num):
    if(n < 2 or n > 36 or num < 0):
        return "Invalid input"
    if(num==0):
        return '0'
    res=""
    sym = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    quotient = num // n
    remainder = num % n
    result = sym[remainder]
    return result
print(DectoNBase(21,5678))
    