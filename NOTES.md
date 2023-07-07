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

