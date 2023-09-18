#            9. Perform the function Checkpassword (char str[], int n)
#               Execute the function which happens to be 1 if the str is a valid password or
#               it remains 0.
'''Conditions for a valid password:'''
#o The password should have at least 4 characters.
#o It should have at least 1 digit.
#o It should have one capital letter.
#o It should not have any spaces or obliques (/).
#o The first character should not be a number.
'''Assumption
The input is not empty.
Example
Input:
aA1_67
Output:
1'''
def checkPassword(str,n):
    number = "0123456789"
    capitalsymbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallsymbols = "abcdefghijklmnopqrstuvwxyz"
    schar = "_"
    if(str[0] in number):
        return '0'
#Complete            
    
