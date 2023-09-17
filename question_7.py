#                  7. The given function has a string (str) and two characters, ch1 and ch2.
#                     Execute the function in such a way that str returns to its original string,
#                     and all the events in ch1 are replaced by ch2, and vice versa.
'''Replacecharacter(Char str1, Char ch1, Int 1, Char ch2)'''
#Assumption
'''This string has only alphabets that are in lower case.
Example
Input:
str: apples
ch1: a
ch2: p
Output:
paales'''
def replacecharacter(str1,ch1,index,ch2):
    list1=[i for i in str1]
    res=[]
    for i in list1:
        if(i == ch1):
            i=ch2
            res.append(i)
        elif(i == ch2):
            i=ch1
            res.append(i)
        else:
            res.append(i)
    result=''.join(res)
    return result
print(replacecharacter('apples','a',2,'p'))

