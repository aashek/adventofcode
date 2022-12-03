inp = [x.rstrip() for x in open("in.txt").readlines()]

csum = 0
for i in range(0, len(inp), 3):
    c = list(set(inp[i]) & set(inp[i+1]) & set(inp[i+2]))[0]

    if ('A' <= c <= 'Z'):
        csum += 27 + ord(c) - ord('A')
    else:
        csum += 1 + ord(c) - ord('a')
print(csum)