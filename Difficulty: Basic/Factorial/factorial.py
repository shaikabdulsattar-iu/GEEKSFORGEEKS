class Solution:
    def factorial(self, n: int) -> int:
        product_ = 1
        for i in range(1,n+1):
            product_ *= i
        return product_    
            