# n : Fjöldi staða
# m : Fjöldi vega
# a : Frá
# b : Til
# c : 0 ef að er einbreið brú
pos = 1

def viableRoads(pos, roads):
    viable = []
    for road in roads:
        if road[0] == pos or road[1] == pos:
            viable.append(road)
    return viable

def roadFinder(pos, vegir):
    next = viableRoads(pos, vegir)
    if len(next) == 0 or pos == 3:
        for road in next:
            roadFinder(road[1], vegir)


vegir = []
n, m = map(int, input().split(' '))
for x in range(m):
    vegir.append(list(map(int, input().split())))

start = viableRoads(1, vegir)


print(start)

for x in start:
    roadFinder(x[1], vegir)