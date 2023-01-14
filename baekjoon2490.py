# Code Submitted
bae_list = ['E', 'A', 'B', 'C', 'D']

for i in range(3):
    case = list(map(int, input().split()))
    bae, deung = 0, 0
    for i in case:
        if int(i) == 0:
            bae += 1
        else:
            deung += 1
    print(bae_list[bae])
    
# Better Code
import sys
result = ['D','C','B','A','E']
for i in range(3):
  yut = list(map(int,sys.stdin.readline().split()))
  print(result[yut.count(1)]) 
