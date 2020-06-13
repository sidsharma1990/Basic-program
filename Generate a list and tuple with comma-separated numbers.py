######Generate a list and tuple with comma-separated numbers######

data2 = input ('Enter the numbers you want to changes into list and tuples: ')
list = data2.split(",")
tuple = tuple(list)
print ('List: ', list)
print ('Tuples: ', tuple)