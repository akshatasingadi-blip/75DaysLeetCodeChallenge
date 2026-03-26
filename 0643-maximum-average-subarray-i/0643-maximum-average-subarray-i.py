class Solution:
    def findMaxAverage(self, nums, k):
        window_sum = 0
        
        # first window
        for i in range(k):
            window_sum += nums[i]
        
        max_sum = window_sum
        
        # slide window
        for i in range(k, len(nums)):
            window_sum = window_sum + nums[i] - nums[i-k]
            if window_sum > max_sum:
                max_sum = window_sum
        
        return max_sum*1.0 / k