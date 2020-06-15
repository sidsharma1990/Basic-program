#### to Calculate radius of a circle #######

print ('Enter X to close the program')

while True:
    sandy = input ('Enter the radius of a circle: ')
    if sandy == 'X':
        break
    else:
        radius = float(sandy)
        area = 3.14 * radius * radius
        print ('Area of circle is ' + str(area))
        
        

    
    
import math
radius = float(input('Radius: '))
area = math.pi*radius*radius
print('Area of requirec circle is', area)