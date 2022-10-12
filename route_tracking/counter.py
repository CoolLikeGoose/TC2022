import code
import re

DISTANTION = 163_912
codes = []          #POINT -> code
connections = {}    #POINT -> [POINT, DISTANTION]

def getCodes():
    f = open("route_tracking/area52_codes.txt", "r")

    matches = re.findall("\d\d\d.*code=\"*.", f.read())
    global codes
    for i in range(len(matches)):
        codes = matches
        codes[i] = matches[i][-1]
    f.close()

def getConnections():
    f = open("route_tracking/area52_dep.txt", "r")

    for line in f:
        data = re.search("(\d\d\d).->.(\d\d\d).*dist=(\d*)", line).groups(1)

        if (int(data[0]) not in connections):
            connections[int(data[0])] = []
        connections[int(data[0])].append([int(data[1]), int(data[2])])

    f.close()


def findConnections(point, curDist, sequence):
    possiblePoints = connections[point]

    for pp in possiblePoints:
        if (pp[0] == 0):
            if (pp[1] + curDist != DISTANTION):
                continue
            else:
                return codes[point-1]
        if (pp[0] in sequence):
            continue

        if (curDist + pp[1] < DISTANTION):
            resp = findConnections(pp[0], curDist+pp[1], sequence+[point])
            if (resp == -1):
                continue
            return codes[point-1] + resp
    
    return -1

            

getCodes()
getConnections()

print(findConnections(0, 0, []))


