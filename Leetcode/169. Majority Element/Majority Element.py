class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = nums.sort()
        return nums[len(nums)//2]
''' 
The given solution works in nlogn time complexity . The idea behind the solution because the number is present in majority that is more than n/2 it will always appear on the middle index of the list. For example if the lists has 10 elements , the 5th element will be the majority one 
'''
