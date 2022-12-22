# Code Submitted -> Runtime Error
A, B, C = list(map(int, input().split()))

if(B > C):
    x = -1

else:
    while((TC-TR) >= 0):
        x += 1
        TC = A + (B * x)
        TR = C * x

print(x)

# Better Code (https://ooyoung.tistory.com/80)
A, B, C = list(map(int, input().split()))
if B >= C:
    print(-1)
else:
    print(A//(C-B)+1)
