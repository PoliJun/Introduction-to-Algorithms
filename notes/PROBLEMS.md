# 1-1

# 2-1 Insertion sort on small arrays in merge sort

1. insertiong sort the n/k sublists, each of length k, in Θ(nk) worst-case time.
2. merge sort the sublists in Θ(n log (n/k))
3. Θ(nk + n log (n/k)) in worst-case, what is the largest value of k as the same time of merge sort?
4. How should you choose k in practice?

-   k is the value to be determined.
-   Θ(nk + n log(n/k))

# 2-2 Correctness of bubblesort
---
input: array A[1:n]  
output: sorted array A

-   pseudocode:

```
BUBBLESORT(A,n)
    for i=1 to n-1
        for j=n downto i+1
            if A[j] < A[j-1]
                swap A[j] and A[j-1]
```
---

# 2-3 correctness of Horner's rule
*running time:* `Θ(n)`.  
# 2-4 Inversion
input: array A[1:n]
output: pairs (i,j)

```
pseudocode:
Get_Inversions(A,n)
    pairs=[]
    for i=1 to n-1
        for j=i to n-1
            if i < j and A[i] > A[j]
                pairs.append((i,j))
    return pairs
```

d. Give an algorithm to determine the number of inversions on n elements in Θ(n log n) worst-case time.

My Answer:
> just add a `count` variable starting at 0 and to plus one every time the right part added to the A[i]
> **this maybe not right!!!**