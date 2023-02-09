def reverse(s):
    mylist = s.split()
    mylist.reverse()
    return ' '.join(mylist)

s = str(input())
print(reverse(s))