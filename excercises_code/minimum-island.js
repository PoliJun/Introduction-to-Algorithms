const minIsland = (grid) => {
    let minIsland = Number.POSITIVE_INFINITY;
    const visited = new Set();
    for (let r = 0; r < grid.length; r++) {
        for (let c = 0; c < grid[0].length; c++) {
            const size = exploreSize(grid, r, c, visited);
            // When meet a "W", the size would be zero, then minIsland would be 0. 
            //We shouldn't do comparison when size is zero
            if (size != 0 && size < minIsland) minIsland = size;
        }
    }
    return minIsland;
};

const exploreSize = (grid, r, c, visited) => {
    // let size = 1;
    const rowInbounds = r >= 0 && r < grid.length;
    const colInbounds = c >= 0 && c < grid[0].length;
    if (!rowInbounds || !colInbounds) return 0;

    if (grid[r][c] === "W") return 0;
    const pos = r + "," + c;
    if (visited.has(pos)) return 0;
    visited.add(pos);

    let size = 1;
    size += exploreSize(grid, r + 1, c, visited);
    size += exploreSize(grid, r - 1, c, visited);
    size += exploreSize(grid, r, c + 1, visited);
    size += exploreSize(grid, r, c - 1, visited);
    // size += 1;

    return size;
};

const grid = [
    ["W", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "L", "W"],
    ["W", "W", "L", "L", "W"],
    ["L", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "W"],
];

console.log(minIsland(grid));
