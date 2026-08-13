class Solution:
    def equilibrium(self, arr):
        total_sum = sum(arr)
        left_sum = 0
        
        for num in arr:
            if left_sum == total_sum - left_sum - num:
                return "true"  # Return string "true" or True based on platform driver expectation
            left_sum += num
            
        return "false"