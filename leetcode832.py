# Code Submitted
class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for arr in image:
            arr.reverse()

        for i in range(len(image)):
            for j in range(len(image[i])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0

        return image
      
# Better Code
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        return [[1-i for i in row[::-1]] for row in A]
