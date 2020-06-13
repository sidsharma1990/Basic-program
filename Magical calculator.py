print ('Our Magical calculator')
print ('Type exit to exit from function')

previous = 0
run = True
# due to 'run = True', loop will keep running

def performMath():
    global run
    global previous
    equation = input ('Enter equation: ')
    if equation == 'exit':
        run = False
    else:
        equation = eval(equation)
        print ('Your input is', equation)

while run:
    performMath()
    
# Output --> Your input is 70

####### Manual work for calculator ############
print ('Our Magical calculator')
print ('Type exit to exit from function')

previous = 0
run = True
# due to 'run = True', loop will keep running

import re

print ('Our Magical calculator')
print ('Type exit to exit from function')

previous = 0
run = True
def performMath():
    global run
    global previous
    equation = ''
    if previous == 0:
        equation = input ('Enter equation: ')
    else:
        equation = input(str(previous))

    if equation == 'exit':
        print ('Good Bye')
        run = False
    else:
        equation = re.sub('[A-Za-z&%$().,;:?]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous)+ equation)
#        print ('Your input is', equation)

while run:
    performMath()
    
# Output --> Your input is 70
    
    
    
    
    
    
    
    
    