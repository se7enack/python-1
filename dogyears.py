#!/bin/env python3

myAge=22

afterFirstTwo=(myAge - 2)
dogYearsUnder=(myAge * 10.5)
dogYearsOver=((afterFirstTwo * 4) + (2 * 10.5))

if myAge > 2:
    print("If you are " + str(myAge) + " years old, you would be " + str(int(dogYearsOver)) + " in dog years.")
else:
    print("If you are only " + str(myAge) + " years old, you would be " + str(int(dogYearsUnder)) + " in dog years. You are just a puppy!")
if myAge > 21:
    print("Good thing you are not a dog as you would likely be dead by now.")
    
