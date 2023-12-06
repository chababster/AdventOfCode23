# Advent of Code    Day 5
# Author            Chababster

# Open file and read all lines into a list 
allLines=[]
with open('day5_puzzle.txt','r') as file:
    allLines=file.read().splitlines()

# Grab seed list, always the first line in the line list 
seedListStr = allLines[0]
_, seeds    = seedListStr.split(": ")

# Main list for all maps
mapList = {}

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

        # Add the current map to the master map dict  
        mapList[rangeMap[0]] = rangeMap[1]

print(mapList)
# --- PT 2 --- 
# From the master seed list, generate all seeds needed
seedListMaster  = seeds.split()
masterLocList   = []

sortedKeys = mapList.keys().sorted()
sortedMapList = {i: mapList[i] for i in sortedKeys}
print(sortedMapList)


# for seedsCnt, seeds in enumerate(seedListMaster):
#     # for x in range(int(seedListMaster[seedsCnt+1])):
#     #     if(int(seeds)+x not in seedList): seedList.append(int(seeds)+x)
#     if(seedsCnt % 2 == 0 or seedsCnt == 0):
#         rangeStart = int(seedListMaster[seedsCnt])
#         rangeLen = int(seedListMaster[seedsCnt+1])
#         seedList = []
#         print("RANGE START:{}\tRANGE END:{}".format(rangeStart,rangeStart+rangeLen))
#         print("RANGE LENGTH:{}".format(rangeLen))
#         for allSeeds in range(rangeLen):
#             currSeed = rangeStart+allSeeds
#             # print("PRE TRANSLATION: {}".format(currSeed))
#             for maps in mapList:
#             # # print("MAP:{}".format(maps[0]))
#             # for seedCnt, seed in enumerate(seedList):
#                 # print("ORIGINAL:{}".format(seedList[seedCnt]))
#                 for ranges in maps[1]:
#                     rangeList = ranges.split()
#                     destRange = int(rangeList[0])
#                     srcRange  = int(rangeList[1])
#                     rangeLen  = int(rangeList[2])

#                     if(currSeed >= srcRange and currSeed < (srcRange+rangeLen)):
#                         diff = currSeed-srcRange
#                         # print("SRC:{}\tSRC START:{}".format(seedList[seedCnt],srcRange))
#                         # print("DEST:{}\tDEST START:{}".format(destRange+diff,destRange))
#                         # print("DIFF:{}".format(diff))                          
#                         currSeed = destRange+diff
#             # print("POST TRANSLATION: {}".format(currSeed))
#             if(currSeed not in seedList): seedList.append(currSeed)

#         seedList.sort()
#         masterLocList.append(seedList[0])
#         # print("FINISHED: {}".format(seedList[seedCnt]))

if(len(masterLocList) > 0): print(masterLocList[0])