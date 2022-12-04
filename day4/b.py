
def overlap(x1, x2, y1, y2):
    return (not (y1 <= y2 < x1 <= x2)) and (not (x1 <= x2 < y1 <= y2))


lines = [x.rstrip() for x in open("in.txt").readlines()]

csum = 0
for l in lines:
    int1, int2 = l.split(',')
    x1, x2 = [int(x) for x in int1.split('-')]
    y1, y2 = [int(x) for x in int2.split('-')]
    if overlap(x1, x2, y1, y2):
        csum += 1


print(csum)