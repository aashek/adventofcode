
instruct = [x.rstrip() for x in open("in.txt").readlines()]

# stacks = [[] for i in range(10)]

# stacks = [list("ZN"), list("MCD"), list("P")]

stacks = [list("NBDTVGZJ"), list("SRMDWPF"), list("VCRSZ"), list("RTJZPHG"), list("TCJNDZQF"), list("NVPWGSFM"), list("GCVBPQ"), list("ZBPN"), list("WPJ")]

for i in instruct:
    a,b,c,d,e,f = i.split(" ")
    b = int(b)
    d = int(d) - 1
    f = int(f) - 1

    # loop b times
    # stack 1 = d
    # stack 2 = f
    s = []
    for i in range(b):
        # s.append(stacks[d].pop())
        s.append(stacks[d].pop())

    stacks[f].extend(s[::-1])
    # stacks[f].append(s[::-1])

for st in stacks:
    print(st[-1], end = "")

print()
