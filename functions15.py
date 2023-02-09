def toString(mylist):
	return ''.join(mylist)

def permutation(mylist, b, l):
	if b == l:
		print(toString(mylist))
	else:
		for i in range(b, l): #0-3
			mylist[b], mylist[i] = mylist[i], mylist[b] #a = a
			permutation(mylist, b+1, l)
			mylist[b], mylist[i] = mylist[i], mylist[b] 

s = input() #abc
l = len(s) #3
mylist = list(s) #["a", "b", "c"]
permutation(mylist, 0, l)