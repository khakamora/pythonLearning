'''
Created on 5 вер. 2018 р.

@author: default-user
'''


my_list = ['gkdfgjkdf dfsjkgh jdfkh', 'rsdfer', 'hgsdkjg dsf gsdfgj hjdfk s', '1', 'gdsf dfzs']

for element in my_list:   
    if 5 < len(str(element)) < 10:
        print (element + "\n")
        
letter = 'r'

for element in my_list:   
    if letter == element[0]:
        print (element + "\n")
        