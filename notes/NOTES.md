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
- four methods:
    ![four methods](../pictures/four_methods_to%20solve_recurrence.png)
### 4.1 Multiplying square matrices
- triple loop: 
    - 1-4: row
    - 2-4: column
    - 3-4: add a polynomial
    ![triple loop](../pictures/triply_loop.png)
- divide-and-conquer
    - base case: `n == 1`. `c11=c11+a11*b11`
    - divide to n/2
    - conquer: recurrences
    ![divide-and-conquer](../pictures/divide_and_conquer_matrix.png)

