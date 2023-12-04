# Advent of Code    Day 4 
# Author            Chababster

# Open file and read all lines
allLines = []
with open('day4_puzzle.txt','r') as f:
    allLines = f.read().splitlines()

# Total points set to 0 and tallied at the end 
totalPoints = 0

# Map comprised of each cards number and the copies of it we possess
# All copies are initially set to 1
cardMap = []
for x in range(len(allLines)):
    cardMap.append([x+1,1])

# Go through all cards in a sequential fashion 
for lineCnt, line in enumerate(allLines):
    # Split the curr game into usable strings
    game, card          = line.split(": ")
    gameStr, roundNum   = game.split()
    winNum, myNum       = card.split(" | ")
    winNumList          = winNum.split()
    myNumList           = myNum.split()
    # totalCards          = 0 

    # --- PT 2 --- 
    # For each copy of the current card...
    for copy in range(cardMap[lineCnt][1]):
        # Set cardPoints to zero initially and for each number we have that is 
        # also in the winning number list, increment cardPoints by 1
        cardPoints      = 0
        for currNum in myNumList:
            if(currNum in winNumList):
                cardPoints = cardPoints + 1

        # For each cardPoint we increment the copy count of card+1 to 
        # card+1+cardPoints by 1 
        for pts in range(cardPoints):
            if( (lineCnt + (pts+1) ) <= len(allLines) ):
                cardMap[lineCnt + (pts+1)][1] = (cardMap[lineCnt + (pts+1)][1] + 1)
   
    # --- PT 1 --- 
    # # Go through all numbers in my list 
    # for currNum in myNumList:
    #     # Try and match each of my numbers to the winning numbers 
    #     if(currNum in winNumList):
    #         # If its the first match we set the points to 1
    #         if(cardPoints == 0):
    #             cardPoints = 1
    #         # If its any match after the first, multiply the pts by 2
    #         elif(cardPoints >= 1):
    #             cardPoints = (cardPoints * 2)   

    # # Update total points with the current card points 
    # totalPoints = totalPoints + cardPoints

# Tally the total amount of cards from the card map  
for cards in cardMap:
    totalPoints = totalPoints + cards[1]

# Print total points
print(totalPoints)