def prime(r):
    for i in range(2,r):
        if is_prime(i) == True:
            print(i)

r = int(input())
is_prime = lambda r: all(r%i != 0 for i in range(2,r))
prime(r)