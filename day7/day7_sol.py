# Read all lines from file into list 
gamesStrs = [] 
with open('day7_puzzle.txt','r') as file:
    gamesStrs = file.read().splitlines()

# In Camel Cards, you get a list of hands, and your goal is to order them 
# based on the strength of each hand. A hand consists of five cards labeled 
# one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. The relative strength of 
# each card follows this order, where A is the highest and 2 is the lowest.

# Create dictionary comprised of the card (key) and its strength (value)
cardDict = {}
cardList = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
for x in range(len(cardList)):
    cardDict[cardList[x]] = len(cardList) - x 

# Every hand is exactly one type. From strongest to weakest, they are:
# 6    Five of a kind, where all five cards have the same label: AAAAA
# 5    Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# 4    Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# 3    Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# 2    Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# 1    One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# 0    High card, where all cards' labels are distinct: 23456

# Winnings = sum[game[0]:game[n]]( game bet * game rank )
gameDict = {}
for game in gamesStrs:
    # Split each line into usable data, the hand and its bet 
    hand, bet = game.split()

    # Tally the amount of unique cards per hand in a dict
    uniqueCards = {}
    for card in hand:
        if(card not in uniqueCards): 
            uniqueCards[card] = 1
        else:
            uniqueCards[card] = uniqueCards[card] + 1

    # Create a dict entry for each hand comprised of...
    #   - bet of the hand 
    #   - the unique cards and their count in the hand 
    #   - the hand type (default is 0)
    gameDict[hand] = [int(bet),uniqueCards,0]

orderedList = []
for games in gameDict.keys():
    # Put the uniqueCards dict into an object to use 
    uniqueCards = gameDict[games][1]

    # Begin to try and categorize the hands type given 
    # the unique cards and their counts 
    if(len(uniqueCards) == 1):
        # If the hand is five of a kind,    set type to 6
        gameDict[games][2] = 6
    elif(len(uniqueCards) == 2):
        keys = uniqueCards.keys()
        keyList = [x for x in keys]

        # If the hand is four of a kind,    set type of 5
        if(uniqueCards[keyList[0]] == 4 or uniqueCards[keyList[1]] == 4):
            gameDict[games][2] = 5
        # If the hand is a full house,      set type of 4
        else:
            gameDict[games][2] = 4
    elif(len(uniqueCards) == 3):
        keys = uniqueCards.keys()
        keyList = [x for x in keys]
        # If the hand is a three of a kind, set type of 3
        if(uniqueCards[keyList[0]] == 3 or
           uniqueCards[keyList[1]] == 3 or
           uniqueCards[keyList[2]] == 3):
            gameDict[games][2] = 3
        # If the hand is a two pair,        set type of 2
        elif((uniqueCards[keyList[0]] == 2 and uniqueCards[keyList[1]] == 2) or
             (uniqueCards[keyList[0]] == 2 and uniqueCards[keyList[2]] == 2) or
             (uniqueCards[keyList[1]] == 2 and uniqueCards[keyList[2]] == 2)):
            gameDict[games][2] = 2
    # If the hand is a one pair,            set type of 1
    elif(len(uniqueCards) == 4):
        gameDict[games][2] = 1
    # If the hand is a high card,           set type of 0
    elif(len(uniqueCards) == 5):
        gameDict[games][2] = 0

rankedList = []
for gameHand in gameDict.keys():
    gameBet         = gameDict[gameHand][0]
    gameUniqueList  = gameDict[gameHand][1]
    gameRank        = gameDict[gameHand][2] 
    if(len(rankedList) == 0):
        rankedList.append([gameHand,gameBet,gameRank])
    elif(len(rankedList) > 0):
        inserted = False
        for gamesCnt, games in enumerate(rankedList):
            rGameHand  = games[0]
            rGameBet   = games[1]
            rGameRank  = games[2]
            if(gameRank <= rGameRank):
                if(gameRank < rGameRank):
                    rankedList.insert(gamesCnt,[gameHand,gameBet,gameRank])
                    inserted = True
                    break
                else:
                    gameIsLesser = False
                    for cardInd, cards in enumerate(gameHand):
                        gCard = gameHand[cardInd]
                        gCardStrength = cardDict[gCard]
                        rCard = rGameHand[cardInd]
                        rCardStrength = cardDict[rCard]
                        if( (gCard != rCard) and (gCardStrength < rCardStrength) ):
                            if(gameRank == 0):
                                print("{} vs {}".format(gameHand,rGameHand))
                                print("{} is less than {}".format(gCard, rCard))
                                print("{} is less than {}".format(gCardStrength, rCardStrength))
                            gameIsLesser = True
                            break
                    if(gameIsLesser):
                        rankedList.insert(gamesCnt,[gameHand,gameBet,gameRank])
                        inserted = True
                        if(gameRank == 0): print(rankedList)
                        break

        if(not inserted): rankedList.append([gameHand,gameBet,gameRank])
            # print("{} {} {}".format(rGameHand,rGameBet,rGameRank))

total = 0
for gameCnt, games in enumerate(rankedList):
    print(games)
    total = total + ( (gameCnt+1) * games[1] ) 

print(total)