# n : Fjöldi nemenda

n = int(input())
nemendur = []
for x in range(n):
    nemendur.append(list(map(int, input().split())))

nr = max([i[0] for i in nemendur])

for x in range(nr):
    for nemandi in nemendur:

