# leetcode:two_sum
class Solution(object):
    def twoSum(self, nums, target):
        
        return_list=[]
        for integer in nums:
            for number in nums[nums.index(integer)+1: ]:
                if integer+number ==target:
                    return_list.append(nums.index(integer))
                    if integer !=number:
                        return_list.append(nums.index(number))
                    else: 
                        a=nums.index(number,nums.index(number)+1)
                        return_list.append(a)
                    return return_list
            
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
