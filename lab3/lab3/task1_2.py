'''
Created on 29 вер. 2018 р.

@author: F
'''

import re

str = "Нехай Лишень, я буду думати Липневого вечора, що цього разу Лише я зможу досягти мети, не знаючи всіх  деталей."

spl_str2 = re.split(',|\s|\.',str)

str2 = "Ли"

j = ""
for i in spl_str2:
    j = ''.join(i) #convert from list to str

    if str2 == j[0:2]:
        print(j)




