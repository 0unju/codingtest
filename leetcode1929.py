# Code Submitted
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list1 = []
        length = len(nums)
        for i in range(2 * length):
            if(i >= length):
                list1.append(nums[i-length])
            else:
                list1.append(nums[i])
        return list1

# Better Code
class Solution:
    getConcatenation = lambda self, A: A * 2
    
# print(Solution.getConcatenation(nums, nums))
# lambda : https://wikidocs.net/64
