function longestCommonSubsequence(text1: string, text2: string): number {
    const N = text1.length,
        M = text2.length;

    let dp = new Array(M + 1).fill(0);

    for (let i = 1; i <= N; i += 1) {
        const currDp = [ ...dp ];
        for (let j = 1; j <= M; j += 1) {
            if (text1[i-1] === text2[j-1]) {
                currDp[j] = 1 + dp[j-1];
            } else {
                currDp[j] = Math.max(dp[j], currDp[j-1]);
            }
        }

        dp = currDp;
    }


    return dp[M];
};