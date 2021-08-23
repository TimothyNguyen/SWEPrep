def countPrimes(n):
    count = 0
    notPrime = [False] * n
    for i in range(2, n):
        if not notPrime(i):
            count += 1
            for j in range(2, i * j < n):
                notPrime[i * j] = True
    return count