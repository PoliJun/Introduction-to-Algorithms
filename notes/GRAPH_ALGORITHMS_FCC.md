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
- use bfs
    > bfs get the target path evenly
