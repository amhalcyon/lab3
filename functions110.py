def unique(mylist):
    x = []
    for i in mylist:
        if i not in x:
            x.append(i)
    return x

s = input()
mylist = s.split()

for i in range(len(mylist)):
    mylist[i] = int(mylist[i])

print(unique(mylist))