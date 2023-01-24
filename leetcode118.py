# Code Submitted
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        push_list = []
        if numRows == 1:
            return [[1]]
        
        else:
            ret.append([1])
            ret.append([1,1])
            if numRows == 2:
                return ret

            list_a = [1,1]
            for j in range(numRows-2):
                list_b = [1]
                for i in range(len(list_a)-1):
                    list_b.append(list_a[i] + list_a[i+1])
                list_b.append(1)
                ret.append(list_b)
                list_a = list_b

            return ret
          
# Better Code 1
def generate(numRows):
    pascal = [[1]*(i+1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1,i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal
  
  
# Better Code 2
class Solution:
    def generate(self, num_rows):
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle
