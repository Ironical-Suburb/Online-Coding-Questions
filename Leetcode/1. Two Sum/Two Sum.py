class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for loops to iterate through the list
        for i in range(len(nums)):
           for j in range(i+1,len(nums)):
               # if condiotion when satisfied return the index of the elements satisfying the condition.
               if nums[i] + nums[j] == target:
                   return[i,j]

'''
Time Complexity = O(n^2) because of nested for loops 
'''
