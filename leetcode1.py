# Code Submitted
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []

        if len(nums) > 2:
            for i in range(0, len(nums)-1):
                for j in range(i+1, len(nums)):
                    ret = nums[i] + nums[j]
                    if(ret == target):
                        output.append(i)
                        output.append(j)
                        break
        
        else:
            output = [0, 1]

        return output
      
# Better Code
class Solution(object):
def twoSum(self, nums, target):
    dic = {}
    for i, n in enumerate(nums): 
        if n in dic:
            return [dic[n], i]
        dic[target-n] = i
