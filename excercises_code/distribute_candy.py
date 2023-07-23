
# @param A : list of integers: the score of kids
# @return sum of candies: an integer: the total number of candies
def solve(A):
    n = len(A)
    candies = [1]*n
    # we compare neighbors in an ascending order, so we create this list in ascending order
    data = sorted((x, i) for i, x in enumerate(A))

    for _, i in data:
        if i > 0 and A[i] > A[i-1]:
            candies[i] = max(candies[i], candies[i-1]+1)
        if i < n-1 and A[i] > A[i+1]:
            candies[i] = max(candies[i], candies[i+1]+1)

    print(candies)
    return sum(candies)


def main():
    my_list = [1, 2, 7, 4, 3, 3, 1]
    ans = solve(my_list)
    print(ans)


main()
