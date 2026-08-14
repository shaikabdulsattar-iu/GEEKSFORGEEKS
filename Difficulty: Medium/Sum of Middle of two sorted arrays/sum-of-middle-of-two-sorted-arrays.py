class Solution:
    def findMidSum(self, arr1, arr2):
        m = sorted(arr1+arr2)
        n = len(m)
        return m[n//2-1] + m[n//2]
        