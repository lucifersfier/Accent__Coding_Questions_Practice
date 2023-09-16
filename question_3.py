#      Write a function to validate if the provided two strings are 
#      anagrams or not. If the two strings are anagrams, then return ‘yes’. 
#      Otherwise, return ‘no’.
'''Input:
Input 1: 1st string
Input 2: 2nd string
Output:
(If they are anagrams, the function will return ‘yes’. Otherwise, it will return ‘no’.)
Example
Input 1: Listen
Input 2: Silent
Output:
Yes
'''

#***********************************************#
def is_anagram(str1 , str2):
    stat = False
    x=list(str1)
    y=list(str2)
    print(x)
    print(y)
    if(len(x)!=len(y)):
        return 'no'
    else:
        for i in x:
            if(i in y):
                stat = True
            else:
                stat = False
    if(stat == True):
        return('yes')
    else:
        return("no")
a='Nittyansh'
b='Srivastav'
print(is_anagram(a,b))