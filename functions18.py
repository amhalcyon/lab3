def spy_game(mylist):
    for i in range(len(mylist)-1):
        if mylist[i] == 0:
            if mylist[i+1] == 0:
                if mylist[i+2] == 7:
                    return True
    return False

s = input()
mylist = s.split()

for i in range(len(mylist)):
    mylist[i] = int(mylist[i])

print(spy_game(mylist))