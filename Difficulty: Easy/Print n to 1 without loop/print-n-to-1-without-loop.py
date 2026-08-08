class Solution:
    def printNos(self, n):
        # Base case: stop when n reaches less than 1
        if n < 1:
            return
        
        # Print current number with space
        print(n, end=" ")
        
        # Recursive call with n - 1
        self.printNos(n - 1)