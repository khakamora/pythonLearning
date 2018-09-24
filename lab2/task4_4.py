'''
Created on 24 вер. 2018 р.

@author: F
'''
str1 = "bla5 bla 3 bla rt"
def get_digits(str1):
    c = ""
    st = ""
    for i in str1:
        if i.isdigit():
            c += i
        else:
            st += i
    print(c)
    print(st)        

get_digits(str1)
