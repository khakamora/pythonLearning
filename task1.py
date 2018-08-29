'''
Created on 26 серп. 2018 р.

@author: F
'''
import math



#case 1
# |(a2/b2 + c2*a2)/(a+b+c*(k-a/b3)) + c + (k/b -k/a)*c|

print("Enter c:")
c = int(input())

print("Enter k:")
k = int(input())
#data validation by zero
while True:
    print("Enter a:")
    a = int(input())
    if a == 0:
        print("Please enter the another number.")
    else:
        break

while True:
    print("Enter b:")
    b = int(input())
    if b == 0:
        print("Please enter the another number.")
    else:
        break

try:    
    1 / (a + b + c*(k - a / b**3))               
except:
    print("Expression (a + b + c*(k - a / b**3) returns 0!!! Repeat with the another digits.")
else:    
    print(math.fabs((a**2 / b**2 + c**2 * a**2) / (a + b + c*(k - a / b**3)) + c +(k / b - k / a)*c))

#case 2
# |((a2-b3 - c3*a2)*(b-c+c*(k-d/b3)) - (k/b -k/a)*c)2 - 20000| 
#math.fabs(((a**2-b**3 - c**3*a**2)*(b-c+c*(k-d/b**3)) - (k/b -k/a)*c)**2 - 20000)

#case3
#|1 - a*bc - a*(b2-c2) + (b-c+a)*(12+b)/(c-a)| 
#math.fabs(1 - a * b**c - a * (b**2 - c**2) + (b - c + a) * (12 + b) / (c - a))
#case4
#|a - b*c*d3+(c5-a2)/a + f3*(a-213)| 
#math.fabs(a - b * c * d**3 + (c**5 - a**2) / a + f**3 * (a - 213))
