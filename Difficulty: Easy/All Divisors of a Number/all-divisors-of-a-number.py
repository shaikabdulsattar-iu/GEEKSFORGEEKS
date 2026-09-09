import math

class Solution:
    def getDivisors(self, n):
        divisors = []
        for i in range(1, int(math.isqrt(n)) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)

        divisors.sort()
        return divisors
        