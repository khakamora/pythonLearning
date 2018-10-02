'''
Created on 29 вер. 2018 р.

@author: F
'''
import re

my_string = "Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса"

spl_list = re.split('_',my_string)

str1 = spl_list[0]
header1 = str1.replace(";","", 2)

str2 = spl_list[1]
row1 = str2.replace(";"," ")

str3 = spl_list[2]
row2 = str3.replace(";"," ")

print('{:<24}{:<14}{}'.format(header1[0:3], header1[4:11], header1[12:21]))
print('{:<24}{:<14}{}'.format(row1[0:20], row1[21:28], row1[29:44]))
print('{:<23}{:<14}{}'.format(row2[0:21], row2[21:28], row2[29:45]))

