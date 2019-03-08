#35. Search Insert Position

#Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#You may assume no duplicates in the array.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0
        for i in range(0, len(nums)):
            if target <= nums[i]:
                return i
            elif target > nums[i]:
                index = i
            else: return 0
        return index+1