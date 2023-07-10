'''
input: unsorted array A
output: sorted array A

algorithm:
1. divide: two equel part, until only unary, L and R
2. sort the two parts separatedly
3. combine the two parts.

pseudo-code:

Merge_Sort(A)
    // the break
    if A.length == 1
        return A
    // divide to two part L and R
    L, R
    // Sort L
    Merge_Sort(L)
    // Sort R
    Merge_Sort(R)
    // Merge L and R
    return Merge(L,R)

    


Merge(L, R)    
    for k=0 to A.length-1
        while  i<L.length  and j<R.length 
            if L[i] <= R[j]
                A[k]=L[i]  
                i += 1      
                k+=1 
            else
                A[k]=R[j]
                j += 1
                k+=1 
    
    // Add the remainer in L and R to A. Because L and R are both sorted, so ,just repeatedly to copy.
    while i<L.length
        A[k]=L[i]
        i += 1
        k += 1 
    while j<R.length
        A[k]=R[j]
        j += 1
        k += 1 

'''

import random


def merge_sort(A):
    if len(A) == 1:
        return A

    L = A[:len(A) // 2]
    R = A[len(A) // 2:]

    
    L = merge_sort(L)
    R = merge_sort(R)

    return merge(L, R)


def merge(L, R):
    A = []
    i = 0
    j = 0

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A.append(L[i])
            i += 1
        else:
            A.append(R[j])
            j += 1

    A += L[i:]
    A += R[j:]

    return A


if __name__ == "__main__":
    A = list()
    for i in range(11):
        A.append(random.randint(1, 100))
    print(A)
    print(merge_sort(A))
