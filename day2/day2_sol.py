# AdventOfCode  Day 2 
# Author:       Chababster

# Open file and read all lines with this method as it removes newline chars
allLines = []
with open('day2_chall.txt') as f:
    allLines = f.read().splitlines() 

# Create obj to store total 
rollingTotal = 0

# Go through all games 
for line in allLines:
    # Set goodGame to true initially
    # goodGame = True

    # Split line into game number and rounds using ": " as the separator
    game, rounds = line.split(": ")

    # Split the 'game' string via " ", only the round # is needed
    _, roundNum = game.split(" ")

    # Default minimum value of 0 for each color per round
    redMin      = 0
    greenMin    = 0
    blueMin     = 0

    # Split rounds into each round using "; " as the separator
    roundList = rounds.split("; ")
    for rounds in roundList:
        # Split the round info into individual count/color strings
        colors = rounds.split(", ")

        # Go through all the colors for this round
        for currColor in colors:
            # Split the string with " " to obtain the color and its count
            count, color = currColor.split(" ")

            # Update the minimum count of the colors needed per round IF 
            # the current minimum is LESS THAN the current count per color
            if(color == "red"):
                if(redMin < int(count)):
                    redMin = int(count)
                # if(int(count) > 12):
                #     goodGame = False
            elif(color == "green"):
                if(greenMin < int(count)):
                    greenMin = int(count)
                # if(int(count) > 13):
                #     goodGame = False
            elif(color == "blue"):
                if(blueMin < int(count)):
                    blueMin = int(count)
                # if(int(count) > 14):
                #     goodGame = False
            
    # Update the rolling with new values total given the formula
    # gameTotal = minRed * minGreen * minBlue
    rollingTotal = rollingTotal + (redMin * greenMin * blueMin)

    # Calculate the new rolling total if the game is possible with the 
    # configuration given (12r, 13g, 14b)
    # if goodGame:
    #     rollingTotal = rollingTotal + int(roundNum)

print(rollingTotal)
