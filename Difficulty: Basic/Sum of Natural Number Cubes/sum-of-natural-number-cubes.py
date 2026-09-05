class Solution:
    def sumOfSeries(self,n):
        sum_ = 0
        for i in range(1,n+1):
            sum_ += i*i*i
        return sum_          
            
        #code here
        