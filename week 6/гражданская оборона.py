def sort(kort):
    return kort[1]


def makeKort(max, list):
    b = []
    for i in range(max):
        b.append((i, list[i]))
    return b


sellist2 = makeKort(int(input()), list(map(int, input().split())))
bomlist2 = makeKort(int(input()), list(map(int, input().split())))

sellist2.sort(key=sort)
bomlist2.sort(key=sort)

nearest = [None] * len(sellist2)
s = b = 0
while s < len(sellist2):
    if b == len(bomlist2) - 1:
        nearest[sellist2[s][0]] = bomlist2[b][0] + 1
        s += 1
    elif abs(sellist2[s][1] - bomlist2[b][1]) < \
            abs(sellist2[s][1] - bomlist2[b + 1][1]):
        nearest[sellist2[s][0]] = bomlist2[b][0] + 1
        s += 1
    else:
        b += 1
print(*nearest)
