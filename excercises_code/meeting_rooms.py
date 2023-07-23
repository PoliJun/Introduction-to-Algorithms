class Solution:
    # @param A : list of list of integers: starting from and ending at
    # @return ans: an integer: at least number of rooms required
    def solve(self, A):
        data = []
        for s, e in A:
            data.append((s, +1))
            data.append((e, -1))

        curr = 0
        ans = 0

        for _, v in data:
            curr += v
            ans = max(ans, curr)

        return ans
