inp = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

f = open("in.txt").readlines()

l = []

csum = 0
for line in f:
    if line == '\n':
        l.append(csum)
        csum = 0
    else:
        csum += int(line[:-1])

# Task 1
# print(max(l))

# Task 2
l.sort()
print(sum(l[-3:]))