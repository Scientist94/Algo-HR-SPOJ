from math import sqrt
primes = set([2])

for i in range(3,32000,2):
    isprime = True

    cap = sqrt(i)+1

    for j in primes:
        if (j >= cap):
            break
        if (i % j == 0):
            isprime = False
            break
    if (isprime):
        primes.add(i)

#print primes
T = int(raw_input())
m, n = raw_input().split(" ")
m = int(m)
n = int(n)      

# for t in range(T):
#     M, N = raw_input().split(' ')
#     M = int(M)
#     N = int(N)
#     max = sqrt(N) + 1

    # if M % 2 != 0:
    #     i = M
    #     while i in range(M+1, N, 2):
    #         if i in primes:
    #             print i

    # else:
    #     i = M
    #     while i in range(M, N)

    # while i in range(M, N):
    #     if i in primes:
    #         print i