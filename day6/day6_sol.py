# AdventOfCode  Day 6
# Author        Chababster
# --- PT 1 ---

# Open file and read
lines = []
with open('day6_puzzle.txt','r') as file:
    lines = file.read().splitlines()

# Split the time and distance strings into usable lists 
times = lines[0][5:].split()
dists = lines[1][10:].split()

# List of how many ways we can win per game 
waysToWinList = []

# Each sec the button is held, the boat gains +1mm/ms of speed
for index, _ in enumerate(times):
    # Put the current time and dist values into vars
    currTime = int(times[index])
    currMaxDist = int(dists[index])

    # Obj for ways to win count
    waysToWin = 0

    # For loop from 0 to currTime, calculate if we can win the race 
    # at that speed and time
    for timeHeld in range(currTime):
        # If the current timeHeld ends up in a greater max distance 
        # we increment our waysToWin counter
        if ( ( (timeHeld) * (currTime - timeHeld) ) > currMaxDist ):
            waysToWin = waysToWin + 1

    # If we found more than 0 ways to win, append the counter to the main list
    if(waysToWin > 0): waysToWinList.append(waysToWin)

# Obj for total
total = 0

# For all the win counts in the list, multiply them 
# all together for a final number
for wins in waysToWinList:
    if(total == 0):
        total = wins
    elif(total > 0):
        total = (total * wins)

print(total)