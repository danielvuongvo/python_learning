r = eval(input("radius"))
import math
circumference = 2*math.pi*r 
area = math.pi*(r**2)
print("c = ", circumference, "a = ", area)
print('c = %.2f, a = %.2f' %(circumference, area))
print('c = {:.2f}, a = {:.2f}'.format(circumference, area))