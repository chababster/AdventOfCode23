# AdventOfCode  Day 9
# Author        Chababster

# Read all lines from file into list 
lines = []
with open('day9_puzzle.txt','r') as f:
    lines = f.read().splitlines()

# Obj for calculating the overall total
mainTotal = 0

# For all the lines we found in the file 
for line in lines:
    # Split the line into numbers via " "
    numList = line.split()

    # Reverse the list for pt 2, comment out for pt 1 answer
    numList.reverse()

    # Grab the last number from the list so we can eventually 
    # add the extrapolated difference to find the next value
    lastNum = int(numList[-1])

    # Empty list to store all the end caps of the diff lists, this will 
    # be used to find the extrapolated difference value
    listOfEndCaps = []

    # While loop that continues running until we find a diff
    # list that is comprised of ONLY zeroes
    while(True):
        # List for differences found 
        listofDiffs = []

        # Obj to keep track of zeros find in the curr diff list
        zerosFound = 0 

        # Go through numList and find the difference between 
        # each values and its previous. Start at the second index 
        # of the list so we'll always find a PREVIOUS value
        for numCnt, num in enumerate(numList[1:]):
            curr = int(numList[numCnt+1])
            prev = int(numList[numCnt])
            diff = curr - prev

            # Append the diff found to the our diff list 
            listofDiffs.append(diff)

            # If the diff is 0, uptick the zeroFound counter
            if(diff == 0):
                zerosFound = zerosFound + 1

        # If we have not found a diff list of all zeros, append 
        # the last value in our diff list to our endcap list then 
        # set the numList to the listOfDiffs 
        if(len(listofDiffs) != zerosFound):
            listOfEndCaps.append(listofDiffs[-1])
            numList = listofDiffs
        # Break if we did find a diff-list of all zeros 
        else:
            break

    # Calculate the difference by adding up all our end caps 
    extrapolatedDiff = 0
    for x in reversed(listOfEndCaps):
        extrapolatedDiff = extrapolatedDiff + x

    # Update the overall sum with the newly found value, which 
    # we find using the last num from the line and the extrapolated diff
    mainTotal = (mainTotal + (extrapolatedDiff + lastNum))

# Print total of all extrapolated values
print(mainTotal)