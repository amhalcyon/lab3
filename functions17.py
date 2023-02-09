def has_33(mylist):
    for i in range(len(mylist)-1):
        if mylist[i] == 3:
            if mylist[i] == mylist[i+1]:
                return True
    return False

s = input()
mylist = s.split()

for i in range(len(mylist)):
    mylist[i] = int(mylist[i])

print(has_33(mylist))