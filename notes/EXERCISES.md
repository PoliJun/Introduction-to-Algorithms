# Exercises 1.1

1. Uber route to home
2. How many times to transfer the goods.
3. Linked List. pros and cons: convenient to add datat, but difficult to delete a specific data.
4. similar: find the best solution. different: the shortest path is determined, the traveling-salesperson transport is not determined.
5. traffic jam on a taxi.
6. 上课迟到点名

# Excercises 1.2

1. Shopping sites' recommendation algorithms.
2.
3. solution:

    ```py
    # if 100n^2 < 2^n,return n
    # else n+=1
    def find_n():
        n = 1
        while True:
            if 100 * n ** 2 < 2 ** n:
                return n
            else:
                n += 1


    if __name__ == "__main__":
        print(find_n())
    ```

# 2.1-3

```
for i=2 to n
key = A[i]
j = i-1
while j>0 and A[j] < key
    A[j+1]=A[j]
    j=j-1
A[j+1]=key
```

# 2.2-1

Θ(1)

# 2.2-2

-   _selection sort_
    > [code](../excercises_code/my_selection_sort.py)  
    > Remember after finding the minimum, there is a **swap** action.

# 2.2-3

---

The same: Θ(n)

---

# 2.2-4

Official Solution:

> Modify the algorithm so that it first checks the input array to see whether it is
> already sorted, taking ‚.n/ time for an n-element array. If the array is already
> sorted, then the algorithm is done. Otherwise, sort the array as usual. The best-
> case running time is generally not a good measure of an algorithm’s efficiency.

# 2.3-1
merge sort explain
# 2.3-2
...
# 2.3-3
12-18: 
- initialize: i=0,j=0,nL>0,nR>0
- maintaine: i=i+1,j=j+1
- terminate: i=nL or j=nR
# 2.3-6
Binary Search

input: sorted array: `A`, target: `k`
output: the index of value `k` in array `A`

Algorithm:
1. find the mid of array `A`
2. if `A[mid]==k`, return `mid`,end
3. if `A[mid]<k`, find the right part.
4. if `A[mid]>k`, find the left part.
5. repeat 1. 2. 3. 4. in current searching subarray.

pseudocode:

Binary_Search(A, k)
    left=1, right=A.length
    while left < right
        mid=(left+right)/2
        if A[mid] < k
            left=mid+1
        else if A[mid] > k
            right=mid-1
        else
            return mid
    return -1 

    
# 3.1-1 
Modify the lower-bound argument for insertion sort to handle input sizes that are not necessarily a multiple of 3.

***
**Answer**


***
# 3.1-2 
Using reasoning similar to what we used for insertion sort, analyze the running time of the selection sort algorithm from Exercise 2.2-2.
***
**Answer**:

Ο(n^2)
Ω(n^2)
Θ(n^2)

***
> **insertion sort analyze:**
> Ο(n^2)
> Ω(n)
> Θ(n^2)

# 3.1-3 
Suppose that α is a fraction in the range 0 < α < 1. Show how to generalize the lower-bound argument for insertion sort to consider an input in which the αn largest values start in the fi rst αn positions. What additional restriction do you need to put on α? What value of α maximizes the number of times that the αn largest values must pass through each of the middle (1 – 2α)n array positions?

