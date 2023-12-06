# Advent of Code    Day 5
# Author            Chababster
# NOTE: This file only solves pt 1 of the Day 5 puzzle

# Open file and read all lines into a list 
allLines=[]
with open('day5_puzzle.txt','r') as file:
    allLines=file.read().splitlines()

# Grab seed list, always the first line in the line list 
seedListStr = allLines[0]
_, seeds    = seedListStr.split(": ")

# From the seeds string, split based off " " to create list of all seeds 
seedList    = seeds.split()

# Main list for all maps
mapList = []

# For loop through every line AFTER the first since we already processed seed
# values into a list 
for lineCnt, line in enumerate(allLines[1:]):
    # List for all of the range lines 
    rangeList = []

    # Map for all range-mapping info
    rangeMap  = []

    # If the line contains 'map' start processing all ranges for that map
    if("map" in allLines[lineCnt]):
        # Strip " map: " from the end of the line and add it to the range map
        rangeMap.append(allLines[lineCnt][:-5])

        # Add all ranges to the list until we find a blank line 
        while(lineCnt+1 < len(allLines) and
                allLines[lineCnt+1] != ""):
            rangeList.append(allLines[lineCnt+1])
            lineCnt = lineCnt+1

        # Add the current range list to the current map 
        rangeMap.append(rangeList)

        # Add the current map to the master map list 
        mapList.append(rangeMap)

# Go through ALL the maps 
for maps in mapList:
    # At each map we try and translate the current seed-value, if 
    # no translation is found for this map, the seed-value remains 
    # unchanged 
    for seedCnt, seed in enumerate(seedList):
        for ranges in maps[1]:
            # Split and turn all necessary values into ints 
            rangeList = ranges.split()
            destRange = int(rangeList[0])
            srcRange  = int(rangeList[1])
            rangeLen  = int(rangeList[2])

            # If the current seed value is within the current 
            # src range for this map, calculate the destination 
            # and reset the seed-value, then break to start on 
            # next seed 
            if(int(seedList[seedCnt]) >= srcRange and 
               int(seedList[seedCnt]) < (srcRange+rangeLen)):
                diff = int(seedList[seedCnt])-srcRange              
                seedList[seedCnt] = destRange+diff
                break

# Sort the seed list after all map translations 
seedList.sort()

# Print the first value from the final list, which is the first loc
print("FIRST SEED LOC:{}".format(seedList[0]))