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
        let current = stack.pop();
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
    const queue = [src];
    while (queue.length > 0) {
        const current = queue.shift();
        console.log(current);
        if (current === dst) {
            return true;
        } else {
            for (let neighbor of graph[current]) {
                queue.push(neighbor);
            }
        }
    }
    return false;
};

console.log("stack: " + dftHaspathStack(graph, "f", "k"));
console.log("recurrsion: " + dftHaspathRecurrsion(graph, "f", "k"));
console.log("queue: " + bftQueue(graph, "f", "k"));
