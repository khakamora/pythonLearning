'''
Created on 29 вер. 2018 р.

@author: F
'''
import re

str = "Нехай, я буду думати, що цього разу я зможу досягти мети, не знаючи всіх деталей."

spl_str2 = re.split(',|\s|\.',str)

i = ""
for i in spl_str2:
    if len(i) > 5:
        print(i)


