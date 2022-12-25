# result = True
# A = "abcdef" / B = "fedcba" : result = False
A = "aaaaaabc"
B = "aaaaaacb"

# Better Code 1
if len(A) != len(B):
    print(False)
if A == B:
    print(set(A))
    print(len(set(A)) < len(A))
diffs = [[a, b] for a, b in zip(A, B) if a != b]
print(len(diffs) == 2 and diffs[0] == diffs[1][::-1])

# Better Code 2
count, rep = 0, 0
if len(A) != len(B) or (len(A) == 1 and A != B) or sorted(A) != sorted(B):
    print(False)
EqualElements = set()

for (X,Y) in zip(A,B):
    if X == Y:
        if X in EqualElements:
            rep += 1
        else:
            EqualElements.add(X)
    else:
        count += 1

print(True if count == 2 or (count == 0 and rep) else False)

# https://ggodong.tistory.com/198
