def removeDuplicates(nums):
    removedDupes_list =[]
    for number in nums:
        if number not in removedDupes_list:
            removedDupes_list.append(number)
    return len(removedDupes_list), removedDupes_list

print(removeDuplicates([1,2,2,3,4,4,5]))

def removeDuplicatesInMemory(nums):
    ind=0
    while ind<len(nums):
        if nums[ind] == nums[ind-1] and len(nums)>1:
            nums.remove(nums[ind])
        else:
            ind=ind+1
    return len(nums)