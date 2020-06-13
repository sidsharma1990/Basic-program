def addition (number1, number2):
    result = (number1+number2)
    print ('The result is: ', result)
    
def substract (number1, number2):
    result = (number1-number2)
    print ('The result is: ', result)

def multiply (number1, number2):
    result = (number1*number2)
    print ('The result is: ', result)

def devide (number1, number2):
    result = (number1/number2)
    print ('The result is: ', result)

print ('Selection operator')
print ('1. Addition')
print ('2. Substraction')
print ('3. Multiplication')
print ('4. Devision')
print ('5. Exit')

while True:
    choice = int(input('Please enter oprator choice: '))
    if (choice >= 1 and choice <=4):
        num1 = int(input('Enter your first number: '))
        num2 = int(input('Enter your second number: '))
        if choice == 1:
            addition (num1, num2)
        elif choice == 2:
            substract (num1, num2)
        elif choice == 3:
            multiply (num1, num2)
        elif choice == 4:
            devide (num1, num2)
    elif choice ==5:
        break
else:
    print ('Please give a correct input!!')