#challenge from r/dailyprogrammer
#challenge #364 [Easy] Create a dice-roller

#create a dice-roller: input will contain one or more lines in NdM format where
#N is the number of dice, and M is the number of sides that those dice have
# ex: 3d10 would mean 3 dice rolled, 10 sides each
# N value may be 1-100 and M value may be 2-100

#output will be the sum of all of the dice rolled on seperate lines
#ex: input: 3d10
#           4d6
#           2d8
#    output:
#           22
#           15
#           11

import re
import random




print("Welcome to the dice roll generator. How many different types of dice would you like to roll?")
numDifferentDiceTypes = int(input())
#numDifferentDiceTypes = 3 #(FOR TESTING)

#creating the 2D array where all of the inputs will be stored and accessed later
arr = []

for i in range(numDifferentDiceTypes):
    dice = input()


    yesno = bool(re.search("^[1-9]{1}-?[d]{1}-?[2-9]{1}$", dice))

    arr.append(dice)

#print(arr)

print("..........")
for i in arr:
    if yesno == True:
        # Parse N and M
        N = int(i[0])
        M = int(i[2])
        #print(N)
        #print(M)
        #print(".........")
        # generate random integer between 1-M, N times. Print sum.
        dice_rolls = []
        for i in range(N):
            roll = random.randrange(1,M)
            dice_rolls.append(roll)


        total = sum(dice_rolls)
        #print(dice_rolls)
        #print("Total:")
        print(total)
        #print('------')

    if yesno == False:
        #try again
        print("Incorrect format, try again")
