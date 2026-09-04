class Solution:
    def product(self, arr):
        mod = 1000000007
        c = 1
        for i in arr:
            c =  (c * i) % mod
        return c        
            
        # code here
        