def solve(numheads,numlegs):
    for i in range(numheads):
        if 4*i+2*(numheads-i) == numlegs:
            return i, numheads-i

numheads = 35
numlegs = 94
s = "{} rabbit and {} chicken"
rabbit, chicken = solve(numheads, numlegs)
print(s.format(rabbit, chicken))