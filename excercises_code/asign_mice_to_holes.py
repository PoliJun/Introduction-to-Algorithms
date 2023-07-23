# @param A: list of integers which is for mice
# @param B: list of integers which is for holes

def solve(A, B):
    A.sort()
    B.sort()

    ans = 0
    for a, b in zip(A, B):
        ans = max(ans, abs(a-b))

    return ans
