'''
Created On ---
@author: Joey

About - 
Uses len to find how many chars are in inputed name. Also finds letters in name based off position (0, 1, 2, 3, etc)
'''

name = input("Enter your first name\n")
last_name = input("Enter your last name\n")
state = input(f'Hi {name} how are you?\n')
full_name = name + " " + last_name

print ("\nThe length of your name is", len(name), "characters")
print (f'additionally, the first character in your name is {name[0]} and the last is {name[-1]}\n')
print (full_name)
