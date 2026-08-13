class Solution:
    def mergeArrays(self, mat):
        # code here
        l = []
        for i in mat:
            l.extend(i)
        return sorted(l)