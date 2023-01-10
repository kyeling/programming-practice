# Google Foobar level 4a

from itertools import permutations

def solution(times, times_limit):
    n = len(times)
    dp = [[times[i][j] for j in range(n)] for i in range(n)]
    
    # floyd-warshall algorithm to get minimal path weight between every pair
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

                # if negative cycle detected, early return a list of all bunnies
                if i == j and dp[i][j] != 0:
                    return list(range(n-2))

    # brute force: check all possible paths 
    res = []
    for l in range(1, n-1):
        paths = list(permutations(range(1, n-1), l))
        for path in paths:
            total_wt = 0
            u, v = 0, 0
            for node in path:
                v = node 
                total_wt += dp[u][v]
                u = v
            total_wt += dp[v][n-1]

            if total_wt <= times_limit:
                path = sorted(path)
                if len(path) > len(res) or (len(path) == len(res) and path < res):
                    res = path
                
    return list(map(lambda x : x - 1, res))


if __name__ == "__main__":
    times, times_limit = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1
    soln = solution(times, times_limit)
    print(soln)

