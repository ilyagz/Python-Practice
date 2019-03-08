#136. Single Number

#Given a non-empty array of integers, every element appears twice except for one. Find that single one.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = set()
        for i in nums:
            if i in new:
                new -= set([i])
            else:
                new.add(i)
        return list(new)[0]