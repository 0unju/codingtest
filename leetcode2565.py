# Code Submitted -> Visual Studio Code O, Leetcode X
class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 2:
            return 1

        ret = []

        length = len(nums) // 2

        for i in range(0, length):
            max_i, min_i, max_ret, min_ret = 0, 0, 0, 0

            for j in range(0, len(nums)):
                if nums[max_i] < nums[j]:
                    max_i = j

                if nums[min_i] > nums[j]:
                    min_i = j

            min_ret = nums[min_i]
            max_ret = nums[max_i]

            if min_i > max_i:
                nums.remove(nums[min_i])
                nums.remove(nums[max_i])
                
            else:
                nums.remove(nums[max_i])
                nums.remove(nums[min_i])
                
            ret.append( (max_ret + min_ret) / 2 )

        result = []
        for r in ret:
            if r not in result:
                result.append(r)

        return len(result)
      
# Better Code
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        av=[]
        nums.sort()
        while nums:
            av.append((nums[-1]+nums[0])/2)
            nums.pop(-1)
            nums.pop(0)
        return len(set(av))
