The master theorem is a method for solving **recurrence relations** that arise from **divide and conquer algorithms**. A recurrence relation is an equation that defines a function in terms of its smaller inputs. For example, the recurrence relation for the merge sort algorithm is:

$$T(n) = 2T(n/2) + \Theta(n)$$

This means that the time complexity of sorting an array of size n is equal to the time complexity of sorting two subarrays of size n/2, plus some linear work to merge them.

The master theorem can be applied to recurrence relations of the form:

$$T(n) = aT(n/b) + f(n)$$

where a, b are positive constants, and f(n) is an asymptotically positive function. This means that the problem of size n is divided into a subproblems of size n/b, and some additional work f(n) is done to combine them.

The master theorem gives three cases for the asymptotic behavior of T(n), depending on how f(n) compares to n^{\log_b a}:

-   Case 1: If f(n) = O(n^{\log_b a - \epsilon}) for some constant \epsilon > 0, then T(n) = \Theta(n^{\log_b a}). This means that f(n) grows slower than n^{\log_b a}, so the dominant term is the recursive work done by the subproblems.
-   Case 2: If f(n) = \Theta(n^{\log_b a}), then T(n) = \Theta(n^{\log_b a} \log n). This means that f(n) grows at the same rate as n^{\log_b a}, so the dominant term is the product of the recursive work and the number of levels in the recursion tree.
-   Case 3: If f(n) = \Omega(n^{\log_b a + \epsilon}) for some constant \epsilon > 0, and if af(n/b) \leq cf(n) for some constant c < 1 and all sufficiently large n, then T(n) = \Theta(f(n)). This means that f(n) grows faster than n^{\log_b a}, and satisfies the regularity condition, so the dominant term is the non-recursive work done at each level.

For example, applying the master theorem to the merge sort recurrence, we have:

-   a = 2, b = 2, f(n) = \Theta(n)
-   n^{\log_b a} = n^{\log_2 2} = n
-   f(n) = \Theta(n^{\log_b a})
-   Therefore, we are in case 2, and T(n) = \Theta(n^{\log_2 2} \log n) = \Theta (n \log n).

For more information and examples on the master theorem, you can refer to these sources:

-   [Master theorem (analysis of algorithms) - Wikipedia](https://en.wikipedia.org/wiki/Master_theorem_%28analysis_of_algorithms%29)¹
-   [Master Theorem (With Examples) - Programiz](https://www.programiz.com/dsa/master-theorem)²
-   [Master’s Theorem in Data Structures | Master’s Algorithm - Scaler](https://www.scaler.com/topics/data-structures/masters-theorem/)³
-   [Master theorem - cse.unt.edu](http://www.cse.unt.edu/~tarau/teaching/cf1/Master%20theorem.pdf)⁴

Source: Conversation with Bing, 7/11/2023
(1) Master theorem (analysis of algorithms) - Wikipedia. https://en.wikipedia.org/wiki/Master_theorem_%28analysis_of_algorithms%29.
(2) Master Theorem (With Examples) - Programiz. https://www.programiz.com/dsa/master-theorem.
(3) Master’s Theorem in Data Structures | Master’s Algorithm - Scaler. https://www.scaler.com/topics/data-structures/masters-theorem/.
(4) Master theorem - cse.unt.edu. http://www.cse.unt.edu/~tarau/teaching/cf1/Master%20theorem.pdf.
