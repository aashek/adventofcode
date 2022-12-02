
f = open("inp.txt").readlines()


csum = 0
for line in f:
    opp, me = line.split()
    
    if (opp == 'A'):
        if (me == 'X'):
            csum += 3 + 1
        elif (me == 'Y'):
            csum += 6 + 2
        elif (me == 'Z'):
            csum += 0 + 3
    if (opp == 'B'):
        if (me == 'X'):
            csum += 0 + 1
        elif (me == 'Y'):
            csum += 3 + 2
        elif (me == 'Z'):
            csum += 6 + 3
    if (opp == 'C'):
        if (me == 'X'):
            csum += 6 + 1
        elif (me == 'Y'):
            csum += 0 + 2
        elif (me == 'Z'):
            csum += 3 + 3

print(csum)