'''
Created on 28 серп. 2018 р.

@author: F
'''
import math
test_list = [19, 4, 2, 3, 5, 11]



enum = []
for n in test_list:
    if n > 10:
        enum.append(n)
    else:
        print("there is no result")

print(math.fsum(enum))
 
