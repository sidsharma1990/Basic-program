a = (40,60,20,50,40,40,50)
b = ('a', 'b', 'c', 'd', 'e','f', 'g')
my_list = zip(a,b)
print (dict(my_list))






def myfunc(*nums):
    return sum(nums)*.5

a=myfunc(40,60,20,50,40,40,50)
print(a)
b=myfunc(40,60,20,50,40,40)
print(b)