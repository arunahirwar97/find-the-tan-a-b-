print ("Find the vlaue of tan(a-b)")
from math import tan
a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))
c = (tan(a)-tan(b))/(tan(a)*tan(b)+1)
print ("THe value of tan(a+b) is = ",c)