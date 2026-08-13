from collections import Counter
class Solution:
    def getSingle(self, arr):
        freq = Counter(arr)
        for key,count in freq.items():
            if count == 1:
                return key
        
        # code here 
        