class Solution:
    def valEqualToPos(self, arr):
        l = []
        for i,j in enumerate(arr,1):
            if i == j:
                l.append(j)
        return l        
                