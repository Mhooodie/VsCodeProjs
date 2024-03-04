'''
Created On ---
@author: Joey

About - 
Goes over how to use list 

?Not sure how int operations work with char in list though?
'''

mylist = []
print (mylist)
print('-----------------------')
mylist = [10,20,'ABC']
print (mylist)
print('-----------------------')
print (f'Value at position 0 is {mylist[0]}')
print (f'Value at position 1 is {mylist[1]}')
print (f'Value at position 2 is {mylist[2]}')
print('-----------------------')
mylist.append(40)
'''Adds to list'''
print (mylist)
print('-----------------------')
mylist.pop(2)
'''Deletes from list at position'''
print (mylist)
print('-----------------------')
mylist.remove(40)
'''removes instance first time it appears'''
print (mylist)
print('-----------------------')
mylist.append(100)
print (mylist)
print('-----------------------')
print (mylist)
print(len(mylist))
print(sum(mylist))
print(min(mylist))
print(max(mylist))
mylist.append(40)
mylist.append(40)
print (mylist)
print('-----------------------')
print(f'first time 40 occurs is at position {mylist.index(40)}')
print(f'number of times 40 occurs in the list {mylist.count(40)}')
print('-----------------------')
mylist.append('hi')
print (mylist)
'''print(sum(mylist)) - How do I do this with a str'''
print('-----------------------')
