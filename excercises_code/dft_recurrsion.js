// use recurrsion

const depthFirstPrint = (graph, source) => {
    // We don't need to add an `if` hear, because e: and f: are dead ends.
    // the for loop is the same performance.
    console.log(source);
    for (let neighbor of graph[source]) {
        depthFirstPrint(graph, neighbor);
    }
};
const graph = {
    a: ["c", "b"],
    b: ["d"],
    c: ["e"],
    d: ["f"],
    e: [],
    f: [],
};

depthFirstPrint(graph,'a');
