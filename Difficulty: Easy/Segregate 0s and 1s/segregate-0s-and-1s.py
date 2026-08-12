class Solution:
    def segregate0and1(self, arr):
        zeros = arr.count(0)
        
        for i in range(len(arr)):
            if i < zeros:
                arr[i] = 0
            else:
                arr[i] = 1