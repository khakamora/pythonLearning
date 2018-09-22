'''
Created on 23 вер. 2018 р.

@author: F
'''
import random

List = [1,2,3,4,5,6]
random.shuffle(List)

print("".join(str(x) for x in List))
