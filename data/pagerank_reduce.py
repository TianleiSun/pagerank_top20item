#!/usr/bin/env python

import sys

alpha = 0.85

key = None
mapSum = []

def parseLine(line):
    if line[-1] == '\n':
        line = line[:-1]
    l1 = line.split("\t")
    key = l1[0]

    if (line[-1]=='#'):
        if line[-2] == '&':
            return (key,0,l1[1][0:l1[1].index("&")],"")
        else:
            return (key,0,l1[1][0:l1[1].index("&")],line[line.index("&")+1:-1])
    else:
        return (key,float(l1[1]), None, None)

old_neighbors = None
neighbors = None
iteras = None

for line in sys.stdin:
    # ctr = mapSum
    nodeId, ctr, iterasTemp, neighborsTemp = parseLine(line)

    if iterasTemp is not None and iteras is None:
        iteras = iterasTemp
    
    if neighborsTemp is not None:
        neighbors = neighborsTemp

    if old_neighbors is None:
        old_neighbors = neighbors

    if key is None:
        key = nodeId
    elif key != nodeId:
        rank = sum(mapSum) + (1 - alpha)
        mapSum[:] = []
        sys.stdout.write("%s\t%f#%s&%s\n" % (key, rank, iteras, old_neighbors))
        key = nodeId
    old_neighbors = neighbors 

    mapSum.append(ctr)

if neighbors is not None:
    rank = sum(mapSum) + (1 - alpha)
    sys.stdout.write("%s\t%f#%s&%s\n" % (key, rank, iteras, neighbors))