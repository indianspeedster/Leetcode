
function findPaths(m: number, n: number, maxMove: number, startRow: number, startColumn: number): number {
    const dp = new Map<string,number>();
    const mod = (10**9) + 7
    const dfs = (i: number,j: number, step:number): number => {
        if (step<0){
            return 0
        }
        if (step >= 0){
            if ((i<0) || (i>=m) || (j<0) || (j>=n)){
                return 1
            }
        }
        const key = `${i},${j},${step}`
        if (dp.has(key)){
            return dp.get(key)
        } 
        dp.set(key, (dfs(i+1, j, step-1) + dfs(i-1, j, step-1) + dfs(i, j+1, step-1) + dfs(i, j-1, step-1))% mod)
        return dp.get(key)
    }

    return dfs(startRow, startColumn, maxMove)
};



