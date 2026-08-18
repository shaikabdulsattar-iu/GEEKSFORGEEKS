class Solution:
    def leaders(self, arr):
        res = []
        max_val = -1
        for x in reversed(arr):
            if x >= max_val:
                res.append(x)
                max_val = x
        return res[::-1]