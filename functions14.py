def filter_prime(n):
    if n == 0 or n == 1:
        return False
    for j in range(2,n):
        if n%j == 0:
            return False
    return True

nums = input()
mylist = nums.split()

for i in range(len(mylist)):
    mylist[i] = int(mylist[i])

for i in range(len(mylist)):
    if filter_prime(mylist[i]) == True:
        print(mylist[i])