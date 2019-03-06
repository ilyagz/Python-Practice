# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        if not strs: return prefix
        shortest = min(strs, key = len)
        for i in range(len(shortest)):
            if all([x.startswith(shortest[:i+1]) for x in strs]):
                prefix = shortest[:i+1]
            else:
                break
        return prefix