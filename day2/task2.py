
f = open("inp.txt").readlines()


csum = 0
for line in f:
    opp, me = line.split()
    
    if (opp == 'A'):
        if (me == 'X'):
            csum += 3 + 0
        elif (me == 'Y'):
            csum += 1 + 3
        elif (me == 'Z'):
            csum += 2 + 6
    if (opp == 'B'):
        if (me == 'X'):
            csum += 1 + 0
        elif (me == 'Y'):
            csum += 2 + 3
        elif (me == 'Z'):
            csum += 3 + 6
    if (opp == 'C'):
        if (me == 'X'):
            csum += 2 + 0
        elif (me == 'Y'):
            csum += 3 + 3
        elif (me == 'Z'):
            csum += 1 + 6

print(csum)