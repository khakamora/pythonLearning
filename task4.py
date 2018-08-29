'''
Created on 28 серп. 2018 р.

@author: F
'''

import statistics

test_list = [19, 4, 2, 3, 5, 11]

print ("Max value element : ", max(test_list))
 
print ("Min value element : ", min(test_list))

avg  = statistics.mean(test_list)
print("Среднее : ", avg)