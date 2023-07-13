***At this point: *Mon Jul 10 19:56:50 CST 2023*, I decided to concentrate on the 1. *important concept* and 2.typical functions and algorithms only for period of time of future untill I have more professional experience. Then, I will be back to tear this book into pieces!!!!!!!!!!!!!!!***

# Part I Foundations

## Introduction

-   Discribe operations and design
-   mathematical tools
-   devide-and-conquer
-   recursion
-   asymptotic notations
-   the _master method_
-   probabilistic analysis

## 1 The Role of Algorithms in Computing

What are algorithms? Why worthwhile? What is the role relative to other technologies used in computers>

### 1.1 Algorithms

-   concept of _algorithms_:
    > Informally, an algorithm is thus a sequence of conputational steps that transform the input into the output.
    > Slove the problem within finite time.
-   instance of a problem
    > consists of the input needed to compute a solution to the problem.
-   Which algorithm is best depends on many aspects of constraints.
-   correct algorithm

    > if , for every problem instance provided as input, it halts (in finite time) and outputs the correct solution to the problem instance.  
    > incorrect algorithms sometimes is useful, we can control the error rate.

-   **What kinds of problems are solved by algorithms?**
-   Data structures
-   Technique
    > _design_ and _analyze_
-   Hard Problems
    -   most of this book is about efficient algorithms.
        > however, for which we know of no algorithm that runs in a reasonable amount of time.
    -   NP-complete. What is this?
-   Alternative computing models.
    > _task-parrallel_
-   _online algorithms_
    > receive the input over time.

### 1.2 Algorithms as a technology

_infinite time_ and _correct answer_

-   Efficiency
    -   insertion sort: O(n^2)
    -   merge sort: O(n log n)
        > even a poor compiler, when the number is large, merge sort still faster than a better compiler
-   Algorithms and other technologies
    -   algorithms are important as hardware
    -   Machine Learning is a kind of algorithm itself,
        > its success is to solve the problems for which we, as human, do not really understand what the right algorithm is.
    -   Data Science, an interdisciplinary field

## 2 Getting Started

Examining the insertion sort. To use a method called devide-and-conquer to develop a sorting algorithm called merge sort.

### 2.1 Insertion sort

-   The number to be sorted is a key, and a key has satellite data.
-   pseudocode:
    ```
    INSERTION-SORT(A,n)
    for i=2 to n
    key = A[i]
    // insert A[i] into the sorted subarray A[1:i-1]
    j = i - 1
    while j > 0 and a[j] < key
        a[j+1] = A[j]
        j = j - 1
    A[j + 1] = key
    ```
-   loop ivariant:
    > three things of using a loop ivariant
      <!-- > waiting for paste from notes -->

### 2.2 Analyzing algorithms

-   concept of _Analyzing algorithms_:
    -   predicating the resources that the algorithm requires.
    -   memory, communication bandwidth, energy consumption.Most often, **computational time**.
-   _random-access machine (RAM)_

    -   concept of _RAM_:
        -   RAM assumes that each instruction takes the same amount of time as any other instruction and that each data access.
    -   Be careful not to abuse the RAM model.
        -   **_the instruction of sort do not appear in real computers! It is not one step._**
        -   commonly instructions: arithmetic (add, subtract, multiply,divide,remainder,floor,ceiling),data movement (load,store,copy), and control(conditional and unconditional branch, subroutine call and return)
        -   Shift instructions(bit operations)
    -   data types in the RAM model:
        1. integer
        2. floating point(real number)
        3. character
            > **real computer do not usually have boolean values True and False. Instead, 0 and 1**
        4. assume that each word of data has a limit on the number of bits.
    -   RAM model doesn't account for the memory hierachy in contemporary computers.
        > neither caches not virtual memory.
        > but RAM model is usually excellent performance on actual machines.
    -   You might need mathematical tools.

    #### Analysis of insertion sort

    -   first, the running time depends on the input.
    -   _input size_: depends on the problem being studied.
        > example: for sorting , the input size is the number n of items. In multiply, the input size is the number of bits.
    -   _running time_: the number of instructions and data access executed.

    #### Worst-case and average-case analysis

    -   To concentrate on on the worst-case.
        > **_Three reasons at Page 61_**
    -   average-case may the same as worst-case, and it related to _probablistic analysis_.

    #### Order of growth

    > or _rate of growth_ > `Θ`

### 2.3 Designing algorithms

-   _incremental_ method
    > Insertion Sort uses a incremental method

#### 2.3.1 The divide-and-conquer method

-   recursive in structure

---

-   recursive case performed in tree characteristic steps:
    1. divide
    2. conquer
    3. combine

---

-   merge sort:
    -   closely follows the divide-and-conquer method.
    -   the key operation: "combine" step.

#### 2.3.2 Analyzing divede-and-conquer method

-   running time described by a _recurrence equation_ or _recurrence_
-   running time:
    > D: divede; 1/b \* n: size of b problem; C: combine
    > ![running time](../pictures/recurrence%20run%20time.png)
-   two convention:
    1. simplification: ignoring floors and ceilings
    2. to omit a statement of the base cases of the recurrence.
        > because the base cases are always T(n)=Θ(1), if `n<n0` or `n>n0`
    ###### Analysis of merge sort
    -   Divide: D(n)=Θ(1).
        > just compute the middle of the subarray
    -   Conquer: 2T(n/2)
        > solving two subproblems, each of size n/2
    -   Combine: C(n)=Θ(n)
        > Merge procedure on an n-element subarray.
        > So, sum of them is `T(n)=2T(n/2)+Θ(n)`.
    -   Θ(n log n)
        -   rows(levels): divide = log n
        -   columns(elements): each touched once => n

## 3 Characterizing Running Times

Usually, an algorithm that is asymptotically more efficient is the best choice for all but very small inputs.

### 3.1 Ο-notation, Ω-notation, and Θ-notation

###### Ο-notation

-   concept of _Ο-notation_:
    > `7n^3+100n^2-20n+6`. It's highest order is 7n^3, this function's rate of growth is n^3, no faster than n^3. Thus, Ο(n^3), and also Ο(n^4) and Ο(n^5) and so on.
-   More generally, it is Ο(n^c) for any constant c>=3.

###### Ω-notation

-   concept of _Ω-notation_
    -   at least fast as.
    -   Ω(n^c), c<=3. Ω(n^3),Ω(n^2),Ω(n^1) and so on.

###### Θ-notation

-   concept of `Θ-notation`:
    -   **precisely** at a certain rate
    -   based--once again--on the highest-order term.
    -   **_if a function both Ο(n^3) and Ω(n^3),then Θ(n^3)_**

### 3.2 Asymptotic notation: formal definitions

> **_notice that this chapter 3.2 is skipped, it's not understandable for me now._**  
> **_time:Mon Jul 10 16:27:21 CST 2023_**

![Graphic example](../pictures/figure3_2.png)

###### Ο-notation

**_TOO PROFESSIONAL FOR ME TO UNDERSTAND, just skipped this chapter!_**

-   Big O is a upper bound
-   Ω is a lower bound
-   Θ is a tight bound

---

**_Theorem 3.1_**  
For any two functions `f(n)` and `g(n)`, we have `f(n) = Θ(g(n))` if and only if `f(n) = Ο(g(n))` and `f(n) = Ω(g(n))`.

---

###### Asymptotic notation and running times

-   When use _Asymptotic notation_
    > make sure as precise as possible without overstating which running time it applies to.

###### Asymptotic notation in equations and inequations

###### Proper abuses of asymptotic notation

**o-notation**
**ω-notation**

### 3.3 Standard notations and common functions

**_JUST FOR KNOW!_**

###### Monotonicity

...

###### Floors and ceilings

Obey the following properties:  
![properties](../pictures/floor_and_ceiling.png)

###### Modular arithmetic

![properties](../pictures/modular_arithmetic.png)

###### Polynomials

![properties](../pictures/polynomials.png)

###### Exponentials

###### Logarithms

###### Factorials

###### Functional iteration

![properties](../pictures/functional_iteration.png)

###### The iterated logarithm function

###### Fibonacci numbers

## Divide-and-Conquer

-   **Divede** the problem into subproblems
-   **Conquer** the subproblems by solving them recursively.
-   **Combine** the subproblem solutions to form a solution to the original problem.

> The recursion _bottoms out_ when it reaches a base case and the subproblem is small enough to solve directly without further recursing.

###### Recurrence

-   general form:
    -   an equation or inequality that describes a function over the integers or reals using the function itself.
    -   It contains two or more cases, depending on the argument.
    -   _recursive case_: involves the recursive invocation
    -   _base case_: not involve a recursive invocation.
    -   _well difined_: if there is at least one fuction that satisfies it
        > and _ill defined_ otherwise

###### Algorithmic recrrences

-   for every sufficient large threshold constant `n0>0`, the following two properties
    1. For all `n<n0`, we have T(n)=Θ(1).
    2. For all `n>=n0`, termination is in a defined base case within a finite number of recursive invocations.
-   Conventions for recurrences
    > **_Whenever a recurrence is stated without an explicit base case, we assume that the recurrence is algorithmic._**

###### Divide-and-Conquer and Recurrences

###### Solving recurrences

-   four methods:
    ![four methods](../pictures/four_methods_to%20solve_recurrence.png)

### 4.1 Multiplying square matrices

-   triple loop:
    -   1-4: row
    -   2-4: column
    -   3-4: add a polynomial
        ![triple loop](../pictures/triply_loop.png)
-   divide-and-conquer
    -   base case: `n == 1`. `c11=c11+a11*b11`
    -   divide to n/2
    -   conquer: recurrences
        ![divide-and-conquer](../pictures/divide_and_conquer_matrix.png)

### 4.2 Strassen's algorithm for matrix multiplication

### 4.3 The substitution method for solving recurrences

---

...A bunch of prove details...

---

-   two steps:
    1. Guess the form of the solution using symbolic constants.
    2. Use mathematical induction to show that the solution works, and find the constants.

###### Making a good guess

-   no general way
-   need experiences and creativity.

###### A trick of the trade: subtracting a low-order term

###### Avoid pitfalls

Avoid using asymptotic notation in the inductive hypothesis for the substitution method because it's errror prone.

### 4.4 the recursion-tree method for solving recurrences

simplify to a geometric

### 4.5 the master method for solving recurrences

-   **Three cases:**
    ![three cases:](../pictures/master_theorem.png)

## 5 Porbabilistic Analysis and Randomized Algorithms

### 5.1 The hiring problem

-   **probilistic**:
    -   each `n!` has the equal probability
-   **randomized algorithms**
    -   algorithm _randomized_: if its behavior not only determined by its input but also by values produced by a _random-number generator_.

### Indicator random variables

![indicator random variables](../pictures/indicator_random_variables.png)

###### Analysis of the hiring problem using indicator random variables

**SKIPPED!!!!!!!!!!!**

### 5.3 Randomized algorithms

concept: _uniform random permutation_

# Part II Sorting and Order Statistics

---

###### **Introduction**

This part presents several algorithms that solve the following _sorting problem_:
![sorting problem](../pictures/sorting_problem.jpg)

###### The structure of data

-   _record_
-   _key_
-   _satellite data_
    ![structure](../pictures/record_key_satellite_data.jpg)

###### Why sorting?

![why sorting](../pictures/why_sorting.jpg)

###### Soring algorithms

-   _in place_:
    -   insertion sort sorts _in place_.
    -   merge sort, the procedure does not operate in place.
-   sorting algorithms analysis table:
    ![sort table](../pictures/sort_ana_table.jpg)

###### Order statistics

###### Background

probability needs mathematical tools.

---

## Heapsort

---

-   running time: Ο(n log n)
-   sorts in place
-   a data structure: _heap_
-   ***here, the term of *heap* does not refer to the storage class, it's a data structure.***

---

### 6.1 Heaps

-   concept of a heap
    -   _(binary) heap_ data structure
    -   is an array object
    -   that we can view as a nearly complete binary tree.
    -   each node of the tree corresponds to an element of the array.
    -   PARENT,LEFT,RIGHT
        > The root of the tree is A[1], and given the index i of a node, there’s a simple way to compute the indices of its parent, left child, and right child with the one-line procedures PARENT, LEFT, and RIGHT.
        > ![heap structure](../pictures/heap_structure.jpg)
    -   find parent, left child, and right child  
         ![find parent, left child, right child](../pictures/find_plr.jpg)
    -   two kinds of heaps, satisfying a _heap-property_:
        -   max-heaps
            > in a _max-heap_, for every node other than the root: `A[PARENT(i)]>=A[i]`
        -   min-heaps
            > in a _min-heap_, for every node other than the root: `A[PARENT(i)]<=A[i]`
    -   define the _height_ of a node: `Θ(log n)`.
        > as for it's a complete binary tree.
    -   some basic procedures:
        -   The **MAX-HEAPIFY** procedure, which runs in O(lg n) time, is the key to maintaining the max-heap property.
        -   The **BUILD-MAX-HEAP** procedure, which runs in linear time, produces a max-heap from an unordered input array.
        -   The **HEAPSORT** procedure, which runs in O(n lg n) time, sorts an array in place.
        -   The procedures **MAX-HEAP-INSERT, MAX-HEAP-EXTRACT-MAX, MAX-HEAP-INCREASE-KEY, and MAX-HEAP-MAXIMUM** allow the heap data structure to implement a priority queue. They run in O(lg n) time plus the time for mapping between objects being inserted into the priority queue and indices in the heap.

### 6.2 Maintaining the heap proerty

-   _heap-size_:
-   figure MAX-HEAPIFY
    ```
        MAX-HEAPIFY(A, i)
    1       l = LEFT(i)
    2       r = RIGHT(i)
    3       if l ≤ A.heap-size and A[l] > A[i]
    4         largest = l
    5       else largest = i
    6       if r ≤ A.heap-size and A[r] > A[largest]
    7         largest = r
    8       if largest ≠ i
    9         exchange A[i] with A[largest]
    1         MAX-HEAPIFY(A, largest)
    ```
-   time complexity: `Ο(log n)`

### 6.3 Building a heap

-   the procedure:

    > by calling max-heapify in a bottom-up manner

    ```
        BUILD-MAX-HEAP(A, n)
    1       A.heap-size = n
    2       for i = ⌊n/2⌋ downto 1
    3           MAX-HEAPIFY(A, i)
    ```

-   time complexity: `Ο(n log n)`

### The heapsort algorithm

-   the procedure:

    ```
        HEAPSORT(A, n)
    1       BUILD-MAX-HEAP(A, n)
    2       for i = n downto 2
    3           exchange A[1] with A[i]
    4           A.heap-size = A.heap-size – 1
    5           MAX-HEAPIFY(A, 1)
    ```

    ![heap sort procedure](../pictures/heap_sort_procedure.jpg)

-   time complexity: `Ο(n log n)`

### 6.5 Priority queues

---

**From youtube:**  
[What is priority queue: ](https://youtu.be/wptevk0bshY)

![priority queue](../pictures/priority_queue.jpg)
When and where to use:  
![when and where to use](../pictures/when_and_where.jpg)
Complexity:  
![complexity pq 1](../pictures/complexity_pq_1.jpg)
![complexity pq 2](../pictures/complexity_pq_2.jpg)

---

-   max-priority queues and min-priority queues.
    > to implement max-priority queues in this book.
-   operations:

    -   INSERT(S, x, k) inserts the element x with key k into the set S, which is equivalent to the operation S = S ⋃ {x}.
        > `Ο(log n)`
    -   MAXIMUM(S) returns the element of S with the largest key.
        > `Ο(1)`
    -   EXTRACT-MAX(S) removes and returns the element of S with the largest key.
        > `Ο(log n)`
    -   INCREASE-KEY(S, x, k) increases the value of element x’s key to the new value k, which is assumed to be at least as large as x’s current key value.
        > `Ο(log n)`

-   uses:
    -   Among their other applications, you can use max-priority queues to schedule jobs on a computer shared among multiple users.
    -   A min-priority queue can be used in an event-driven simulator.
-   methods to add application objects to the priority queue:
    -   handles, a hidden index.
    -   hashtable
-   Algorithms,pseudocodes:
    ![operations](../pictures/priority_queue_operation1.jpg)  
    ![operations](../pictures/priority_queue_operation2.jpg)

## Quicksort

---

-   worst-case `Θ(n^2)`
-   but remarkably efficient on average: excepted running time is `Θ(n lg n)`.
-   sorting in place

---

### 7.1 Description of quicksort

-   three steps:
    -   **Divide** by partitioning (rearranging) the array A[p : r] into two (possibly empty) subarrays A[p : q – 1] (the low side) and A[q + 1 : r] (the high side) such that each element in the low side of the partition is less than or equal to the pivot A[q], which is, in turn, less than or equal to each element in the high side. Compute the index q of the pivot as part of this partitioning procedure.
    -   **Conquer** by calling quicksort recursively to sort each of the subarrays A[p : q – 1] and A[q + 1 : r].
    -   **Combine** by doing nothing: because the two subarrays are already sorted, no work is needed to combine them. All elements in A[p : q – 1] are sorted and less than or equal to A[q], and all elements in A[q + 1 : r] are sorted and greater than or equal to the pivot A[q]. The entire subarray A[p : r] cannot help but be sorted!
-   pseudocode:
    > **input**: array A[1:n], initial call QUICKSORT(A,1,n)  
    > **output**: sorted A
    > ![quicksort_pseudocode](../pictures/quick_sort_7_1.jpg)

###### Partitioning the array

-   pseudocode:
    > ![partition_pseudocode](../pictures/partition_algorithems.jpg)
-   initialization, maintenance, termination of the loop
    -   **initialization**: `i=p-1` and `j=p`.
    -   **maintenance**: if `A[j] > x`, then increment `j` but i, else if `A[j] <= x`, increment `i`, swaps `A[j]` and `A[i]`, and then increment `j`.
    -   **termination**: `j > r-1`.

### 7.2 Performance of quicksort

---

It depends on how balanced the pivot.

---

###### Worst-case partitioning

-   **occurs** when the partitioning produces one subproblem with `n-1` elements and one with 0 elements.
-   `T(n) = T(n-1) + T(0) + Θ(n) = T(n-1) + Θ(n)`.
-   `Θ(n^2)`. which case that is always sorted.

###### Best-case partitioning

-   **in the most even possible split**, **PARTITION** produces two subproblems, each of size no more than `n/2`.
-   `T(n) = 2T(n/2) + Θn`.
-   `Θ(n lg n)`

###### Balanced partitioning

-   always produces a `9-to-1` proportional split.
-   `T (n) = T (9n/10) + T (n/10) + Θ(n)`
-   `Ο(n lg n)`
    > ![balance case](../pictures/quicksort_balance_case.jpg)

###### Intuition for the average case

![quicksort intuition](../pictures/quicksort_intuition.jpg)

### 7.3 A randomized version of quicksort

![randomized quicksort](../pictures/randomized_quicksort.jpg)

### 7.4 Analysis of quicksort

**_TOO PROFESSIONAL, JUST SKIPPED!!!!!!!_**

## 8 Sorting in Linear Time

---

_comparison sorts_:  
These algorithms share an interesting property: the sorted order they determine is based only on comparisons between the input elements. We call such sorting algorithms comparison sorts. All the sorting algorithms introduced thus far are comparison sorts.

**_Any comparison sort must make `Ω(n lg n)` comparisons in the worst case to sort `n` elements._**

---

### 8.1 Lower bounds for sorting

**_ASSUME WITHOUT LOSS OF GENERALITY IN THIS SECTION THAT ALL THE INPUT ELEMENTS ARE DISTINCT._**

###### The _dicision-tree_ model

-   the concept of _dicision-tree_:
    -   is a full binary tree
        > ![decision-tree](../pictures/decision_tree.jpg)

###### A lower bound for the worst case

-   the height of its decision tree  
    > Consequently, the worst-case number of comparisons for a given comparison sort algorithm equals the height of its decision tree.
- proof:
    > ![proof Ω(n log n)](../pictures/proof_lower_bound_nlogn.jpg)
### 8.2 Counting sort
---
*Counting sort* assumes that each of the `n` input elements is an integer in the range `0` to `k`, for some integer `k`. It runs in `Θ(n + k)` time, so that when `k = O(n)`, counting sort runs in `Θ(n)` time.

***From YouTube:***
![counting sort properties](../pictures/counting_sort_properties.jpg)
![counting sort](../videos/counting_sort.mp4)
---