def remove_vowels (newstr, string):
    vowels = ('a', 'e','i','o', 'u', 'A', 'E', 'I', 'O', 'U')
    for c in string.lower and string.upper():
        if c in vowels:
            newstr=newstr.replace(c,"")
    return newstr 
    
print ("Enter x for exit")
string = input("Enter string to remove vowels from it: ")
if string == "x":
    exit()
else:
    newstr = string
    print("Replacing vowels from the given string...")
    newstr= remove_vowels(newstr, string)
    print("The new string after remvoing vowels "+ (newstr))
    
##################
print ('Enter x to exit')
string = input("Enter string to remove vowels from it: ")
if string == "x":
    exit()
else:
    newstr = string
    vowels = ('a', 'e','i','o', 'u', 'A', 'E', 'I', 'O', 'U')
    for c in string.lower and string.upper():
        if c in vowels:
            newstr=newstr.replace(c,"")
    print('New string after removing vowel is: ', newstr)