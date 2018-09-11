# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Hello, world.")

# add and assign
i = 1
i += 1
print(i)


print('a' == 'a')
print('a' == 1)
print(5 != 25/5)

#working with strings
print('A'+'B')
print('me'*3)
#print('A'+3)   error

#working with sequences
mystring = 'happy'
print(mystring[0])
print(mystring[2:4])

mylist = ['Leia','Rey','Maz']
print(mylist[-1])

mydict = {'name':'Kylo','side':'dark'}
print(mydict['name'])

#working with conditionals
name = 'Grace Hopper'

if len(name) < 20:
    print ('Yes')
else:
    print('No')

#working with loops
#for loop
i = 0
for letter in name:
    if letter in ['a','e','i','o','u']:
        i=i+1
print(name+' has '+ str(i) +' vowels.')

#while loop
i=0
vowel_count = 0
while i < len(name):
    if name[i] in ['a','e','i','o','u']:
        vowel_count = vowel_count + 1
    i = i + 1
print(name+' has '+ str(vowel_count) +' vowels.')
