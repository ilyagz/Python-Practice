# 169. Majority Element

# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > total_count:
                return num
