######## Reading or Writing into a file #####

file = open('Pythonfile.txt')
file.close()
# WARX --> W - Over-Writing, A - Appending, X creating and R - Reading
fn = open('Pythonfile.txt', 'r')
fn.read()
fn.read(5)
fn.readline()
#Output: 'Hello World'
fn.close()

fn = open('Pythonfile.txt', 'w')
fn.write('This is different')
fn.close()

fn = open('Pythonfile.txt', 'a')
fn.write('More data to add')
fn.close()


#### w+ and x can be used to create and write something in a file####
fn = open('Pythonfilenewupdate.txt', 'w+')
fn.write('This is differentuie')
fn.close()

fn = open('Pythonfile233.txt', 'x')
fn.write('More data to add')
fn.close()

#############for more lines######

fn = open('Pythonfile.txt', 'r')
for line in fn.readlines():
    print(line)
    
for line in fn.readlines():
    line = line.strip('\n')
    print(line)
    
file = open('C:\Users\sshar127\Desktop\Python\Sandeep.txt', 'r')

######### Reading and Writing 2#######

import os
directory = input('Enter path where you need to save your file: ')
directory = directory.strip('\n')

os.chdir(directory)
file_name = input('Please enter the name of file: ')
content_in_file = 'My name is Sandeep\nI am a Business analyst\nWorking with UHG'

fn = open(file_name, 'a')
fn.write(content_in_file)
fn.close()

##### Removing a file########

import os
os.remove('Pythonfilenewupdate.txt')