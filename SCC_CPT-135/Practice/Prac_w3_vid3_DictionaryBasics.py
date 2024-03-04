'''
Created On ---
@author: Joey

About - 
Goes over general use of dictionaries
'''

print('\n---------------------------------')
print('Dictionary Basics')
print('---------------------------------\n')

calories = {}
print (calories)
calories = {'coke': 200, 'sprite': 210, 'mountain_dew': 250}
print (calories)
print('---------------------------------')
print (f'Coke has {calories['coke']} calories')
print (f'Sprite has {calories['sprite']} calories')
print (f'Mountain Dew has {calories['mountain_dew']} calories')
print('---------------------------------')
calories['fanta'] = 300
print (calories)
print('---------------------------------')
del calories['fanta']
print (calories)
print('---------------------------------')

print('\n---------------------------------')
print('String Formatting')
print('---------------------------------\n')

name = 'Deepika'
test1 = 100
test2 = 80.5
avg = (test1+test2)/2
print(avg)
grade = 'A'

print(f'{name}, your test score, final average, and grade are below')
print('%s, your test score, final average, and grade are below' %name)
'''String %s'''
print(f'In test 1, you scored a %d' %test1)
'''Digit %d'''
print(f'In test 2, you scored a %.2f' %test2)
'''Floating point %f'''
print(f'Your average is %.2f' %avg)
'''.2f formats it to 2 decimal places instead of 90.25000000'''
print(f'%s, your final grade for the course is %s and you got a %d on test 1 and a %f on test 2' %(name, grade, test1, test2))





