'''
Created on 23 вер. 2018 р.

@author: F
'''
str1 = "bla5 bla 3 bla rt"
def get_digits(str1):
    c = ""

    for i in str1:
        if i.isdigit():
            c += i

    return c

digits = get_digits(str1)
print(digits)

print(''.join(c for c in str1 if c.isdigit()))
