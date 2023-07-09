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
- merge sort:
    - closely follows the divide-and-conquer method.
    