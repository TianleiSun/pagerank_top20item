#!/usr/bin/env python

import sys
import operator
# import re

#
# This program simply represents the identity function.
# 

MAX_ITR = 10
topRank = {}
heap = {}
itr = 0
graphList = []
flag = True

'''
expr = re.compile('\t|#|&')

def parseLine(line):
    if line[-1]=='\n': line = line[:-1]
    l = expr.split(line)
    return l[0], float(l[1]), l[3], int(l[2])
'''

for line in sys.stdin:
    flag = itr == 7
    #nodeID, score, neighbor, itr = parseLine(line)
    if line[-1] == '\n':
        line = line[:-1]
    l = line.split('\t')
    nodeID = l[0]
    rest1 = l[1].split('#')
    score = float(rest1[0])
    rest2 = rest1[1].split('&')
    itr = int(rest2[0])
    neighbor = rest2[1]
    
    if flag:
        ##### save nodes for processing when cutting
        nList = neighbor.split(',')
        graphList.append((nodeID, score, nList))


    else:
        if itr < MAX_ITR:
            sys.stdout.write('NodeId:%s\t%f,0.0,%s#%d\n' %(nodeID, score, neighbor, itr + 1))
        elif itr == MAX_ITR:
            if len(topRank) < 20:
                topRank[nodeID] = score
            else:
                (key, minval) = min(topRank.items(), key = lambda x: x[1])
                if score > minval:
                    del topRank[key]
                    topRank[nodeID] = score

#####  cutting
if flag:
    # f = open('test.txt', 'w')
    n = len(graphList)
    #select top K
    for l in graphList:
        if len(heap) < 200:
            heap[l[0]] = l[1]
        else:
            (key, minval) = min(heap.items(), key = lambda x: x[1])
            if l[1] > minval:
                del heap[key]
                heap[l[0]] = l[1]
    
    # f.write(str(len(graphList)))
    #all the node goes into next graph
    nodeSet = set()
    for key in heap.keys():
        nodeSet.add(key)
    for tup in graphList:
        #key = tup[1]
        for neigh in tup[2]: 
            if neigh in nodeSet: nodeSet.add(tup[0])
    for tup in graphList:
        #key = tup[1]
        if tup[0] in nodeSet:
            cutList = []
            for neigh in tup[2]: 
                if neigh in nodeSet: cutList.append(neigh)
            sys.stdout.write('NodeId:%s\t%f,0.0,%s#%d\n' %(tup[0], tup[1], ",".join(cutList), itr + 1))
            # f.write('NodeId:%s\t%f,0.0,%s#%d\n' %(tup[0], tup[1], ",".join(cutList), itr + 1))
    # f.write(str(len(graphList)))
    # f.close()


if topRank:
    topRank = sorted(topRank.items(), key = operator.itemgetter(1), reverse = True)
    for (id, rank) in topRank:
        sys.stdout.write('FinalRank:%f\t%s\n' %(rank, id))
