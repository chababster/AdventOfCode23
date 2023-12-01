# Advent of Code - Day 1
# Author:   Chababster

# List of words from 'one' to 'nine'
numWordList = ["one",
                "two",
                "three",
                "four",
                "five",
                "six",
                "seven",
                "eight",
                "nine"]

# Function used to translate a numeric word to an int (i.e. "five" returns 5)
# Args      userStr is a string that should have a corresponding numeric value
# Return    Numeric value corresponding to the userStr 
def strToNum(userStr):
    for num in numWordList:
        if(userStr == num and num == "one"):
            return 1
        elif(userStr == num and num == "two"):
            return 2
        elif(userStr == num and num == "three"):
            return 3
        elif(userStr == num and num == "four"):
            return 4
        elif(userStr == num and num == "five"):
            return 5
        elif(userStr == num and num == "six"):
            return 6
        elif(userStr == num and num == "seven"):
            return 7
        elif(userStr == num and num == "eight"):
            return 8
        elif(userStr == num and num == "nine"):
            return 9

# Create file obj via opening the day 1 puzzle text file in read mode
file = open('day1_puzzle.txt', 'r')

# Read all lines from the file and store in a list
Lines = file.readlines()

# Value for storing the rolling total of values found in each line
combSum=0

# For loop for each line in the Lines list
for line in Lines:
    # Start with an empty string for each line
    combStr=""

    # While the current line length is greater than zero
    while (len(line) > 0):
        # Start with the foundNumWord flag set to False 
        foundNumWord = False

        # Go through each word in the numWordList 
        for num in numWordList:
            # If the substr of line[0:len(num)] is equal to the current num in the word list...
            if(num == line[0:len(num)]):
                # Remove the matching substr from the beginning of the word
                line = line[len(num):]
                # Add the found number to the combined string 
                combStr = combStr + str(strToNum(num))

                # Set the found flag to true and break out of the for loop 
                foundNumWord = True
                break

        # ONLY IF WE DID NOT find a word with the previous method...
        if(not foundNumWord):
            # Check if the zero'th value is a number, if so, add it to the combined string
            if(len(line) >= 1 and line[0].isnumeric()):
                combStr=combStr+line[0]

            # Pop front value 
            line = line[1:]

    # If combined string is MORE than 2 chars, take only the beginning and last
    if(len(combStr) > 2):
        combStr = (combStr[0] + combStr[len(combStr)-1])
    # If combined string is ONLY one char, duplicate the char
    elif(len(combStr) == 1):
        combStr = combStr + combStr

    # Rolling total of the values found
    combSum = (combSum + int(combStr))

# Print final value 
print(combSum)