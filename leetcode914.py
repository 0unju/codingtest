# Code Sumitted
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        
        if len(deck) < 2:
            return False

        ret = []
        for i in range(0, max(deck)+1):
            if deck.count(i) != 0:
                ret.append(deck.count(i))

        for j in range(0, len(ret)-1):
            if self.gcd(ret[j], ret[j+1]) <= 1:
                return False

        return True


    def gcd(self, a, b):
            while b != 0:
                temp = a % b
                a = b
                b = temp
            return a
          
# Better Code
from functools import reduce
from math import gcd
from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck):
        return reduce(gcd, Counter(deck).values()) != 1
