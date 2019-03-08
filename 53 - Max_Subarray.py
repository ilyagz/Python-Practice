# 53. Maximum Subarray

#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = float("-inf")
        maxSum = float("-inf")
        for i in range(len(nums)):
            sum += nums[i]
            if (sum < nums[i]):
                sum = nums[i]
            maxSum = max(sum, maxSum)
        return maxSum