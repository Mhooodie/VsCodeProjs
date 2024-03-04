'''Chap 5'''

print("---------------------------")
'''Question 1'''
print("Question 1\n")

numsquare = 1
square = 0

while numsquare < 11:
    square = numsquare * numsquare
    print (square)
    numsquare += 1

print("---------------------------")
'''Question 2'''
print("Question 2\n")

number = int(input("Enter a number: ")) 
i = 0
numlist = []
product = 1

while i < number:
    i += 1
    numlist.append(i)
for num in numlist:
    product *= num

print (product)

print("---------------------------")
'''Question 3'''
print("Question 3\n")

fib_A = 0
fib_B = 1
fibseq = 0
fibseqlist = [0, 1]

while fibseq < 89:
    fibseq = fib_A + fib_B
    fibseqlist.append(fibseq)
    if fib_A > fib_B:
        fib_B = fibseq
    elif fib_B > fib_A:
        fib_A = fibseq
    else:
        fib_A = fibseq

print (fibseqlist)

print("---------------------------")
'''Question 4'''
print("Question 4\n")

numprint = 1
numlist = [1, 2, 3, 4, 5]

while numprint < 6:
    print(*numlist[0:numprint])
    numprint += 1
    
print("---------------------------")

