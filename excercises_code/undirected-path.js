const edges = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"],
];

// DFS
const undirectedPath = (edges, nodeA, nodeB) => {
    const graph = buildGraph(edges);
    return hasPathDFS(graph, nodeA, nodeB, new Set());
};

const hasPathDFS = (graph, src, dst, visited) => {
    if (src === dst) return true;
    if (visited.has(src)) return false;

    visited.add(src);

    for (let neighbor of graph[src]) {
        if (hasPathDFS(graph, neighbor, dst, visited) === true) return true;
    }
    return false;
};

const buildGraph = (edges) => {
    graph = {};

    for (let edge of edges) {
        const [a, b] = edge;
        if (!(a in graph)) graph[a] = [];
        if (!(b in graph)) graph[b] = [];
        graph[a].push(b);
        graph[b].push(a);
    }

    return graph;
};
undirectedPath(edges, "r", "t")
