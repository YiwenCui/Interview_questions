class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        max_product=(nums[-1]-1)*(nums[-2]-1)
        return max_product