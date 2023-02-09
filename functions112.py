def histogram(mylist):
    for i in range(len(mylist)):
        print("*" * mylist[i])

s = input()
mylist = s.split()

for i in range(len(mylist)):
    mylist[i] = int(mylist[i])

histogram(mylist)