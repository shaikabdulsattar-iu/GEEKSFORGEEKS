class Solution:
    def mergeNsort(self, arr1, arr2):
        return sorted(list(set(arr1 + arr2)))
