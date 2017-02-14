#!/usr/bin/env python

import sys
#
# This program simply represents the identity function.
#
def parseLine(line):
    if line[-1]=='\n': line = line[:-1]
    tempList = line.split("\t")
    string1 = tempList[0]
    string2 = tempList[1]
    nodeID = string1[string1.index(":")+1:len(string1)]
    if "#" not in line:
        iteration = 0
    else:
        tempList2 = tempList[1].split("#")
        iteration = tempList2[1]
        string2 = tempList2[0]
    string2List = string2.split(",")
    currRank = float(string2List[0])
    neighborsList = string2List[2:len(string2List)]
    return nodeID, iteration, currRank, neighborsList

for line in sys.stdin:
    nodeID, iteration, currRank, neighborsList = parseLine(line)
    neighborsString = ",".join(neighborsList)
    for neighbor in neighborsList:
        if neighbor:
            value=0.85*currRank/len(neighborsList)
            sys.stdout.write("%s\t%s\n"%(neighbor,value))
        else:
            sys.stdout.write("%s\t%s\n"%(nodeID,0.85*currRank))
    sys.stdout.write("%s\t%s&%s#\n"%(nodeID,iteration,neighborsString))
    
# API:  10  1.0#3&2,3,4,7
#    nodeID\tab\current_rank\#iteration\&neighborslist   