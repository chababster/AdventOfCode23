# Open and read in lines from puzzle file
lines = []
with open('day12_puzzle.txt','r') as f:
    lines = f.read().splitlines()

for hotSpringLine in lines:
    springMap, spotMap = hotSpringLine.split()
    spotList = spotMap.split(',')
    print("MAP:{}\tSPOTS:{}".format(springMap, spotMap))
    charCount = 0
    while(charCount < len(springMap)):
        mapString = ""
        if(springMap[charCount] == '?'):
            while(charCount < len(springMap) and 
                  springMap[charCount] == '?'):
                mapString = mapString + springMap[charCount]
                charCount = charCount + 1    
        else:
            charCount = charCount + 1

        if(mapString != ""): 
            for maps in spotList:
                mapVal = int(maps)
                if(mapVal <= len(mapString)):
                    print("MAP:{}\t{}".format(mapString, mapVal))