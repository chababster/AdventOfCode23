# Advent of Code    Day 3
# Author            Chababster

# Open file and read all lines
allLines = []
with open('day3_puzzle.txt') as f:
    allLines = f.read().splitlines() 

# List of numbers 0-9 in char form
numChar = ['0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9']

# Parse all chars in the schematic into a 2D array 
engineGrid = []
for line in allLines:
    rowChar = []
    for char in line:
        rowChar.append(char)
    engineGrid.append(rowChar)

# Total value that we'll update at the end of processing each square
total = 0

# Start going through the grid character by character 
for rowCount, row in enumerate(engineGrid):
    for charCount, char in enumerate(row):
        # Only need to care about symbols (e.g. not a number or ".")
        if(char not in numChar and char != "."):
            # Create 3x3 square for each symbol
            # [] [] [] 
            # [] S  []
            # [] [] []
            line0="{}{}{}".format(engineGrid[rowCount-1][charCount-1],
                                    engineGrid[rowCount-1][charCount],
                                    engineGrid[rowCount-1][charCount+1])
            line1="{}{}{}".format(engineGrid[rowCount][charCount-1],
                                    char,
                                    engineGrid[rowCount][charCount+1])
            line2="{}{}{}".format(engineGrid[rowCount+1][charCount-1],
                                    engineGrid[rowCount+1][charCount],
                                    engineGrid[rowCount+1][charCount+1])
            
            # List with values that allow us to calculate relative to the middle of the square
            relList = [-1,0,1]

            # Start blank list per square for all found values 
            numList = []

            # []    - A value that we potentially use as a starting point to 
            #         find a full surrounding value
            # S     - current symbol 

            # [] [] [] 
            # x  S  x 
            # x  x  x 
            for forCount, rel in enumerate(relList):
                number = ""
                indivChar = line0[forCount]
                if(indivChar in numChar):
                    # Set the number to the current char in the string
                    number = indivChar

                    # While loop that will continously try and find numbers to the left
                    # of the current number, until we reach the end of the string or 
                    # no more continous numbers are found
                    roll = 1
                    while(True):
                        if((charCount+rel-roll) < 0):
                            break

                        possNum = engineGrid[rowCount-1][charCount+rel-roll]
                        if(possNum in numChar):
                            number = possNum + number
                            roll = roll + 1
                        else:
                            break

                    # While loop that will continously try and find numbers to the right
                    # of the current number, until we reach the end of the string or 
                    # no more continous numbers are found
                    roll = 1
                    while(True):
                        if((charCount+rel+roll) > (len(row)-1)):
                            break

                        possNum = engineGrid[rowCount-1][charCount+rel+roll]
                        if(possNum in numChar):
                            number = number + possNum
                            roll = roll + 1
                        else:
                            break
                forCount = forCount + 1

                # Only add the found number IF it is NOT empty and IS NOT already
                # in our list of numbers for this square
                if(number != "" and number not in numList): numList.append(number)

            # x  x  x 
            # x  S  x 
            # [] [] []
            for forCount, rel in enumerate(relList):
                number = ""
                indivChar = line2[forCount]
                if(indivChar in numChar):
                    number = indivChar
                    roll = 1
                    while(True):
                        if((charCount+rel-roll) < 0):
                            break

                        possNum = engineGrid[rowCount+1][charCount+rel-roll]
                        if(possNum in numChar):
                            number = possNum + number
                            roll = roll + 1
                        else:
                            break

                    roll = 1
                    while(True):
                        if((charCount+rel+roll) > (len(row)-1)):
                            break

                        possNum = engineGrid[rowCount+1][charCount+rel+roll]
                        if(possNum in numChar):
                            number = number + possNum
                            roll = roll + 1
                        else:
                            break
                forCount = forCount + 1

                if(number != "" and number not in numList): numList.append(number)

            # x x x 
            #[] S x
            # x x x 
            if(line1[0] in numChar):
                number = line1[0]
                roll = 1
                while(True):
                    if((charCount-1-roll) < 0):
                        break

                    possNum = engineGrid[rowCount][charCount-1-roll]
                    if(possNum in numChar):
                        number = possNum + number
                        roll = roll + 1
                    else:
                        break

                if(number != "" and number not in numList): numList.append(number)

            # x x x 
            # x S []
            # x x x 
            if(line1[2] in numChar):
                number = line1[2]
                roll = 1
                while(True):
                    if((charCount+1+roll) > (len(row) - 1)):
                        break

                    possNum = engineGrid[rowCount][charCount+1+roll]
                    if(possNum in numChar):
                        number =  number + possNum
                        roll = roll + 1
                    else:
                        break

                if(number != "" and number not in numList): numList.append(number)

            # Calculate new total with found values
            if(char == "*" and len(numList) == 2):
                total = total + (int(numList[0]) * int(numList[1]))

            # for num in numList:
            #     total = total + int(num)

print(total)