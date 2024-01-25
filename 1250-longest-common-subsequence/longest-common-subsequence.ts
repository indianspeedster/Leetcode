function longestCommonSubsequence(text1: string, text2: string): number {
    const n1 = text1.length;
    const n2 = text2.length;
    const dp = new Map<string, number>(); // Change the key type to string

    const dfs = (x: number, y: number): number => {
        if (x === n1 || y === n2) {
            return 0;
        }
        const key = `${x},${y}`; // Create a unique string key
        if (dp.has(key)) {
            return dp.get(key)!; // Use the key to get the value from the map
        }
        
        if (text1[x] === text2[y]) {
            dp.set(key, 1 + dfs(x + 1, y + 1));
            return dp.get(key)!;
        }
        
        const result1 = dfs(x + 1, y);
        const result2 = dfs(x, y + 1);

        if (result1 > result2) {
            dp.set(key, result1);
        } else {
            dp.set(key, result2);
        }
        
        return dp.get(key)!;
    }

    return dfs(0, 0);
}
