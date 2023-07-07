# Exercises 1.1

1. Uber route to home
2. How many times to transfer the goods.
3. Linked List. pros and cons: convenient to add datat, but difficult to delete a specific data.
4. similar: find the best solution. different: the shortest path is determined, the traveling-salesperson transport is not determined.
5. traffic jam on a taxi.
6. 上课迟到点名

#### Excercises 1.2

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
