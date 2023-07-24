'''
 @param A: list of integers
 @return an integer
 length of the list A is N, returns frequency > N / 2 element.
'''
from collections import Counter


# This solution: time complexity Ο(N) and space Ο(N). This is not the optimal solution
def naive_solve(A):
    return Counter(A).most_common(1)[0][0]


# Sneaky solution
'''
[0,1,1]

num=0,b=0
ones+=1
ones=1
ans=0

num=1,b=1
10 & 1 = 11
ones=2
ans = (1<<1) = 10
'''
def sneaky_solve(A):
    n = len(A)
    ans = 0
    for b in range(32):
        ones = 0
        for num in A:
            if (1 << b) & num:
                ones += 1
        print(ones)
        if ones > n//2:
            ans += (1 << b) # or ans |= (1 << b)
        
    return ans

print(sneaky_solve([0]))



'''


'''