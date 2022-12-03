
inp = [x.rstrip() for x in open("in.txt").readlines()]

# inp = """
# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw"""

csum = 0
for line in inp:
    # print("Here")
    # print(len(line))
    
    m = len(line) // 2

    a = line[:m]
    b = line[m:]

    print(a, b)
    c = list(set(a) & set(b))[0]

    if ('A' <= c <= 'Z'):
        csum += 27 + ord(c) - ord('A')
    else:
        csum += 1 + ord(c) - ord('a')

print(csum)