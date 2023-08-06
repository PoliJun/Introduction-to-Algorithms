const graph = {
    f: ["g", "i"],
    g: ["h"],
    h: [],
    i: ["g", "k"],
    j: ["i"],
    k: [],
};
//dft stack
const dftHaspathStack = (graph, src, dst) => {
    let stack = [src];
    while (graph[src].length > 0) {
        let current = stack.shift();
        console.log(current);
        if (current == dst) return true;
        for (let neighbor of graph[current]) {
            stack.push(neighbor);
        }
    }
    return false;
};
// dft recurrsion
const dftHaspathRecurrsion = (graph, src, dst) => {
    if (src === dst) return true;

    for (let neighbor of graph[src]) {
        if (dftHaspathRecurrsion(graph, neighbor, dst) === true) {
            return true;
        }
    }
    return false;
};

// bft queue
const bftQueue = (graph, src, dst) => {
    let queue = []
}

console.log("stack: " + dftHaspathStack(graph, "f", "k"));
console.log("recurrsion: " + dftHaspathRecurrsion(graph, "f", "k"));
