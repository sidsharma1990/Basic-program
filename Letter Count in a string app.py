##### Letter Count in a string app ###

print ('Welcome to letter count app!!')

# user input
name = input('Please enter your name: ').title().strip()
print ('Hello', name, '!')

print ('I will count a letter in your string!')
message = input('Please enter your message here: ')
letter = input ('Please enter letter you want to check here: ')

message = message.lower()
letter = letter.lower()

lettercount = message.count(letter)
print(name, 'your message has', str(lettercount), letter, '\'s in it')