# Code Submitted
class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        count = 0

        for word in words:
            flag = 0
            if word[0] == s[0]:
                for w in word:
                    if w not in s:
                        flag = -1
                    else:
                        if flag != -1:
                            flag = 1
            
            if flag == 1:
                count += 1

        return count
      
# Better Code
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count=0
        for i in words:
            if (s[:len(i)]==i):
                count+=1
        return count
