class Solution:
    def getSubArrays(self, arr):
        res = []
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n + 1):
                res.append(arr[i:j])
                
        return res