# Code Submitted 
def solution(n):
    answer = []
    string_n = str(n)
    for i in range(len(string_n)-1, -1, -1):
        answer.append(int(string_n[i]))
    return answer
  
# Better Code
def digit_reverse(n):
    return [int(i) for i in str(n)][::-1]
