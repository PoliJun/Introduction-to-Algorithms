const minIsland = (grid) =>{
    for(let r=0; r<grid.length; r++){
        for(let c=0; c<grid[0].length; c++){
            exploreSize(grid,r,c,visited)
        }
    }
}

const grid = [
    ["W", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "L", "W"],
    ["W", "W", "L", "L", "W"],
    ["L", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "W"],
];
