# Code Submitted
class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """

        if len(s) < 3:
            return []

        elif len(s) == 3:
            if ((s[0] == s[1]) & (s[1] == s[2])):
                return [[0, 2]]

            else:
                return []

        # s의 길이가 3보다 클 때
        else:
            ret = []
            i = 0

            while(i < len(s) - 2):
                flag = 0
                flag2 = 1
        
                if ((s[i] == s[i+1]) & (s[i+1] == s[i+2])):
                    flag = 1
                    j = i+2 
                    while(flag2 == 1):
                        print("i = ", i, " / j = ", j, " / flag2 = ", flag2)
                        if j+1 <= len(s):
                            if s[i+2] == s[j]:
                                j += 1
                            else:
                                flag2 = 0
                        if j+1 > len(s):
                            flag2 = 0
                
                if flag == 1:
                    ret.append([i, j-1])
                    i = j

                else:
                    i += 1

            return ret
          
# Better Code
class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        ret = []
        j = 0

        for i in range(len(s)):
            if i == len(s) - 1 or s[i] != s[i+1]:
                if i-j+1 >= 3:
                    ret.append([j, i])
                j = i + 1

        return ret
