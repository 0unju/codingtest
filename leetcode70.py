# Code Submitted -> Time Limit
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        half = n//2
        ret, new = [], []

        for i in range(n, -1, -1):
            for j in range(0, half+1):
                l = [1] * i + [2] * j
                if (sum(l) == n) :
                    ret.extend(list(permutations(l, len(l))))

        for value in ret:
            if value not in new:
                new.append(value)

        return(len(new))
      
# Better Code
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
       
        ways=[1,2];
        
        for i in range(2,n):
            ways.append(ways[i-1]+ways[i-2])
         
        return ways[n-1]

# https://novlog.tistory.com/267
