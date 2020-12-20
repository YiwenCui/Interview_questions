class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=0
        for ele in nums:
            if len(str(ele))%2==0:
                n=n+1
        return n