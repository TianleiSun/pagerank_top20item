#!/usr/bin/env python

import sys
import operator

#
# This program simply represents the identity function.
# 

MAX_ITR = 14
topRank = {}

for line in sys.stdin:
    if line[-1] == '\n':
        line = line[:-1]
    l = line.split('\t')
    nodeID = int(l[0])
    rest1 = l[1].split('#')
    score = float(rest1[0])
    rest2 = rest1[1].split('&')
    itr = int(rest2[0])
    neighbor = str(rest2[1])
    if itr < MAX_ITR:
        sys.stdout.write('NodeId:%d\t%f,0.0,%s#%d\n' %(nodeID, score, neighbor, itr + 1))
    elif itr == MAX_ITR:
        if len(topRank) < 20:
            topRank[nodeID] = score
        else:
            (key, minval) = min(topRank.items(), key=lambda x: x[1])
            if score > minval:
                del topRank[key]
                topRank[nodeID] = score

if topRank:
    topRank = sorted(topRank.items(), key = operator.itemgetter(1), reverse = True)
    for (id, rank) in topRank:
        sys.stdout.write('FinalRank:%f\t%d\n' %(rank, id))
