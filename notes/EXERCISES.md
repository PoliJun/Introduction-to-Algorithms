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
