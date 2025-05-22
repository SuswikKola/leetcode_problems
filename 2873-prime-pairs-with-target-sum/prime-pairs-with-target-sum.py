class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        res = []
        
        primes = [1 for _ in range(n + 1)]
        primes[0] = primes[1] = 0
        p = 2
        while p ** 2 <= n:
            if primes[p]:
                for i in range(p ** 2, n + 1, p): 
                    primes[i] = 0
            p += 1
        
        for p in range(2, n // 2 + 1):
            if primes[p] and primes[n - p]:
                res.append([p, n - p])
        return res