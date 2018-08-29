'''
Created on 26 серп. 2018 р.

@author: F
'''

test_list = [4, 's', 'p', 'isok', 2, 3, 'test 5', 5]

new_list = []
for value in test_list:
    try:
        new_list.append(int(value))
    except ValueError:
        continue

def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print("\n".join(map(str, is_even_num(new_list))))