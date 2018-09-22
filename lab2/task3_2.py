'''
Created on 23 вер. 2018 р.

@author: F
'''
import random
print("Enter N:")
user_number = int(input())

print(''.join(random.choices("R", k=user_number)))