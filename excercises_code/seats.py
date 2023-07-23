# @ param A: list of strings
# @ return ans: an integer
def solve(A):
    MOD = 10000003
    # index where x exists
    crosses = [i for i, c in enumerate(A) if c == 'x']
    # moves req assuming starting at index 0
    crosses = [(cross-i) for i, cross in crosses]

    n = len(crosses)
    ans = float('inf')

    segment_start = crosses[n // 2]

    total = 0

    for cross in crosses:
        total += abs(cross-segment_start)
        total %= MOD
    ans = min(ans, total % MOD)

    return ans
