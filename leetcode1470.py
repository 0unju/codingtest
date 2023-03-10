# Code Submitted
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ret = []
        for i in range(0, n):
            ret.append(nums[i])
            ret.append(nums[n+i])

        return ret
      
# Better Code
class Solution(object):
    def shuffle(self, nums, n):
      return [j for i in zip(nums[:n], nums[n:]) for j in i]
