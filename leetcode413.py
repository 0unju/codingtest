# Code Submitted
class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        cnt = 0
        ret = 0

        for i in range(len(nums)-2):
            if (nums[i+2] - nums[i+1]) == (nums[i+1] - nums[i]):
                cnt += 1
                ret += cnt
            else:
                cnt = 0

        return ret
      
# Better Code
class Solution(object):
    def numberOfArithmeticSlices(self, A):
      count = 0
      for i in range(len(A)-2):
        j = i+2
        while j < len(A):
          if A[i+1]-A[i] == A[j]-A[j-1]:
            count += 1
            j += 1
          else:
            break

      return count
