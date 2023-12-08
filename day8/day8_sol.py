# Read files lines and store in list 
lines = []
with open('day8_puzzle.txt','r') as f:
    lines = f.read().splitlines()

directions = lines[0]
locDict = {}

for line in lines[2:]:
    nodeInit, nodeDest = line.split('=')
    nodeDestList = nodeDest[2:(len(nodeDest)-1)].split(', ')
    # print("INSERTING: {} - {}".format(nodeInit,nodeDestList))
    locDict[nodeInit[:-1]] = nodeDestList
    # print(nodeStr,nodeDestList)

keyList = list(locDict.keys())
key = keyList[0]

finalFound = False
stepCount = 1
loopCount = 0 
while(not finalFound):
    stepCount = 1 
    for dirSteps, dirs in enumerate(directions):
        # Set the L / R index to 0 (L) by default and 
        # only set to 1 if the dir is R
        ind = 0
        if('R' == dirs): 
            ind = 1 

        # Grab the L or R destination from the current key
        keyInDict = locDict[str(key)]
        newKey = keyInDict[ind]

        # print("{} --> {}".format(key, newKey))
        # Break early if our dest is 'ZZZ'
        if(newKey in 'ZZZ'):
            finalFound = True
            stepCount = dirSteps + 1
            break
        # If the new dest isn't 'ZZZ', set the key to newKey
        # and increment stepCount by 1 
        else:
            key = newKey

    if(not finalFound): loopCount = loopCount + 1 

print("STEPS:{}".format(loopCount*len(directions)+stepCount))