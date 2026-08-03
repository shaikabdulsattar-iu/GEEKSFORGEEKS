class Solution:
    def countFreq(self, arr, target):
        # code here
        c = 0
        for i in arr:
            if i == target:
                c += 1
        return c        
                