# Graph basics

## graph = nodes + edges

-   nodes and edges
    > ![graph](../pictures/graph.jpg)
-   kinds of graphs: _directed graph_ and _undirected graph_
    > ![directed graph and undirected graph](../pictures/kinds_of_grahps.jpg)
    -   directed graph
        -   neighbor
            > ![neighbor](../pictures/neibor.jpg)
        -   adjacency list
            > ![adjacency list](../pictures/adjacency_list.jpg)
        -   depth first traversal
            > follow a direction to the deapest first.
            > **USE STACK** > [code](../excercises_code/dft_stack.js)
        -   breadth first traversal
            > find all the neighbors of a node first
            > **USE QUEUE**

# has-path problem

-   `cycle`
    > ![what is a cycle]()
-   `acyclic`
    > ![wath is acyclic]()
-   Time: `Ο(e)`, Space: `Ο(n)`
    > `n = nodes`  
    > `e = edges` > ![time and space of dft]()

# undirected problem

-   We need a guard to deal with cycle:
    > ![a cycle]()
    -   we can mark visited node as visited
-   time and space complexity: `n = nodes` and `e = edges`
    -   Time: `Ο(e)`
    -   Space: `Ο(n)`

# connected components count

![count and mark]()

-   time and space complexity: `n = nodes` and `e = edges`
    -   Time: `Ο(e)`
    -   Space: `Ο(n)`

# largest component

-   time and space complexity: `n = nodes` and `e = edges`
    -   Time: `Ο(e)`
    -   Space: `Ο(n)`

# shortest path

-   use bfs
    > bfs get the target path evenly

# island count

-   time and space complexity: `r = rows` and `c = cols`
    -   Time: `Ο(rc)`
    -   Space: `Ο(rc)`
    -   recurrsion in this problem explained
        > In the recursion function, the relationship between the inner `explore` function's return value and the outer `explore` function is crucial for the correct operation of the algorithm. The return value of the inner `explore` function affects how the outer `explore` function proceeds with its exploration and backtracking process.
        >
        > Let's analyze the relationship step by step:
        >
        > 1. When the `explore` function is called initially from the `islandCount` function, it starts exploring a particular cell in the grid.
        >
        > 2. Within the `explore` function, the first thing it does is check for base cases (out of bounds, water, or already visited). If any of these base cases are met, it immediately returns `false` to the caller (either the outer `explore` function or the `islandCount` function).
        >
        > 3. If the current cell is not a base case, it means the cell is part of an unvisited island. The `explore` function marks the current cell as visited and then proceeds to recursively explore its neighboring cells.
        >
        > 4. The recursive calls to the `explore` function are the inner calls. Each inner call explores a neighboring cell of the current cell.
        >
        > 5. The inner `explore` function returns `true` if it successfully explores an island, i.e., it finds a cell that is part of an unvisited island and recursively explores all its connected cells.
        >
        > 6. When the inner `explore` function returns `true`, it indicates to its calling `explore` function that it has found a new island and successfully explored all its connected cells.
        >
        > 7. The outer `explore` function, upon receiving the `true` return value from the inner call, also returns `true`. This propagates the information upward in the call stack, indicating that the current cell is part of an unvisited island.
        >
        > 8. The outer `explore` function then continues its exploration process, checking other neighboring cells (if any) to see if they are part of the same island. It does this by making recursive calls to the inner `explore` function for each neighboring cell.
        >
        > 9. The recursive process continues until all connected cells of the current island have been visited, and the outer `explore` function finally returns to the initial `islandCount` function call.
        >
        > 10. The `islandCount` function increments its count if the `explore` function returned `true`, indicating that it found a new island, and then proceeds to explore the next unvisited cell in the grid.
        >
        > In summary, the return value of the inner `explore` function propagates information about the presence of a new island and the successful exploration of that island. This information helps the outer `explore` function and, ultimately, the `islandCount` function to correctly count the number of islands in the grid by exploring each island and its connected cells recursively.
# minimum island

# The problems:
- path, shortest path
- count, island count
- size, minimum size