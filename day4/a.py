
def inside(x1, x2, y1, y2):
    return (x1 <= y1 and x2 >= y2) or (y1 <= x1 and y2 >= x2)



lines = [x.rstrip() for x in open("inp.txt").readlines()]

csum = 0
for l in lines:
    int1, int2 = l.split(',')
    x1, x2 = [int(x) for x in int1.split('-')]
    y1, y2 = [int(x) for x in int2.split('-')]
    if inside(x1, x2, y1, y2):
        csum += 1


print(csum)

