class Solution:
    def nthFibonacci(self, n: int) -> int:
        # This is your exact recursive approach nested inside
        def fib(x):
            if x == 0: return 0
            if x == 1: return 1
            return fib(x-1) + fib(x-2)
            
        return fib(n)

