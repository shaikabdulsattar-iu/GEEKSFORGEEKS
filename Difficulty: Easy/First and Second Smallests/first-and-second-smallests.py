class Solution:
    def minAnd2ndMin(self, arr):
        unique_sorted = sorted(set(arr))
        
        if len(unique_sorted) < 2:
            return [-1]
        
        return [unique_sorted[0], unique_sorted[1]]