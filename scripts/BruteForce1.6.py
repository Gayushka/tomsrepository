import time
import string

letters = string.ascii_lowercase
Letters = string.ascii_letters
printable = string.printable

guess = ''

L0 = 0
L1 = 0
L2 = 0
L3 = 0
L4 = 0
L5 = 0

one = True
two = False
three = False
four = False
five = False
six = False

password = input('Password: ')
t0 = time.time()

while guess != password:
    if one == True:
        guess = Letters[L0]
        L0 += 1
        #print(str(guess))
        if L0 == 52 and guess != password:
            one = False
            two = True
            L0 = 0

    elif two == True:
        guess = Letters[L0] + letters[L1]
        L1 += 1
        #print(str(guess))
        if L1 == 26:
            L0 += 1
            L1 = 0
        if L0 == 52 and guess != password:
            two = False
            three = True
            L0 = 0

    elif three == True:
        guess = Letters[L0] + letters[L1] + letters[L2]
        L2 += 1
        #print(str(guess)
        if L2 == 26:
            L1 += 1
            L2 = 0
        if L1 == 26:
            L0 += 1
            L1 = 0
        if L0 == 52 and guess != password:
            three = False
            four = True
            L0 = 0
           
            
    elif four == True:
        guess = Letters[L0] + letters[L1] + letters[L2] + letters[L3]
        L3 += 1
        #print(str(guess))
        if L3 == 26:
            L2 += 1
            L3 = 0
        if L2 == 26:
            L1 += 1
            L2 = 0
        if L1 == 26:
            L0 += 1
            L1 = 0
        if L0 == 52 and guess != password:
            four = False
            five = True
            L0 = 0

    elif five == True:
        guess = Letters[L0] + letters[L1] + letters[L2] + letters[L3] + letters[L4]
        L4 += 1
        #print(str(guess))
        if L4 == 26:
            L3 += 1
            L4 = 0
        if L3 == 26:
            L2 += 1
            L3 = 0
        if L2 == 26:
            L1 += 1
            L2 = 0
        if L1 == 26:
            L0 += 1
            L1 = 0
        if L0 == 52 and guess != password:
            five = False
            six = True
            L0 = 0

    elif six == True:
        guess = letters[L0] + letters[L1] + letters[L2] + letters[L3] + letters[L4] + printable[L5]
        L5 += 1
        #print(str(guess))
        if L5 == 100:
            L4 += 1
            L5 = 0
        if L4 == 26:
            L3 += 1
            L4 = 0
        if L3 == 26:
            L2 += 1
            L3 = 0
        if L2 == 26:
            L1 += 1
            L2 = 0
        if L1 == 26:
            L0 += 1
            L1 = 0
        if L0 == 52 and guess != password:
            six = False
            seven = True
            L0 = 0

        
        
        

if guess == password:
    t1 = time.time()
    T = t1 - t0
    print('Your Password is: ' + str(guess))
    print('Brute Force Time: ' + str(T))
    
