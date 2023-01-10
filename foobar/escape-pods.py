## Google Foobar 4b

## Dinic's algorithm for O(EV^2) time, iterative dfs TODO

# def bfs(src, sink, path):
#     n = len(path)
#     visited = [False] * n
#     q = [src]
#     levels = [-1] * n
#     levels[src] = 0
#     level = 0

#     while q:
#         u = q.pop(0)
#         level += 1
#         for v in range(n):
#             if not visited[v] and path[u][v]:
#                 levels[v] = level
#                 if v == sink: 
#                     return (True, path, levels)
#                 visited[v] = True
#                 q.append(v)
#     return False

# def dfs(src, sink, path, levels, total_flow):
#     n = len(path)
#     q = [src]
#     u = src
#     iteration_flow = 0
#     min_flow = float('inf')
#     flow = 0

#     while q:
#         # print(q)
#         u = q.pop()
#         for v in range(n):
#             if v == sink:
#                 pass
#             remaining_flow = max(path[u][v] - flow, 0) 
#             if levels[u] + 1 == levels[v] and remaining_flow:
#                 q.append(v)
#                 min_flow = min(min_flow, remaining_flow)

#         # not correct: need path, not every edge from node
#         if min_flow:
#             for v in range(n):
#                 if path[u][v]:
#                     path[u][v] -= min_flow
#                     path[v][u] += min_flow

#         iteration_flow += min_flow
#         total_flow += min_flow    

#     return (iteration_flow, path, total_flow)


## submitted solution:

# iterative bfs on residual graph
# keep track of path with parent index array
def bfs(src, sink, path, parent):
    n = len(path)
    visited = [False] * n
    q = [src]
    
    while q:
        u = q.pop(0)
        for v in range(n):
            if not visited[v] and path[u][v]:
                parent[v] = u
                if v == sink: 
                    return True
                visited[v] = True
                q.append(v)
    return False
            
def solution(entrances, exits, path):
    n = len(path)

    # combine all entrances into single source node and all exits into single sink node
    src = entrances[0]
    sink = exits[0]
    
    # consolidate entrance and exit rows first
    src_row = [sum(elems) for elems in zip(*[path[i] for i in entrances])]
    sink_row = [sum(elems) for elems in zip(*[path[i] for i in exits])]

    path[src] = src_row
    path[sink] = sink_row
    for i in entrances[1:] + exits[1:]:
        path[i] = [0]*n  

    # consolidate entrance and exit columns
    src_col  = [sum(elems) for elems in [[row[j] for j in entrances] for row in path]]
    sink_col = [sum(elems) for elems in [[row[j] for j in exits] for row in path]]

    for i in range(n):
        for j in entrances + exits:
            if j == src:
                path[i][j] = src_col[i]
            elif j == sink:
                path[i][j] = sink_col[i]
            elif j in entrances[1:] + exits[1:]:
                path[i][j] = 0

    # run Edmonds-Karp algorithm to get maximum flow in O(VE^2) time
    total_flow = 0
    parent = [-1 for _ in range(n)]
    
    while bfs(src, sink, path, parent):
        # iterate through bfs path to find minimum flow
        min_flow = float('inf')
        v = sink
        while v != src:
            u = parent[v]
            min_flow = min(min_flow, path[u][v])
            v = u
    
        # iterate through bfs path again to update edge weights
        total_flow += min_flow
        v = sink
        while v != src:
            u = parent[v]
            path[u][v] -= min_flow
            path[v][u] += min_flow
            v = u

    return total_flow
    
# Sources used: https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
    
    # bfsPaths, path, levels = bfs(src, sink, path)
    # while bfsPaths:
    #     print('bfs')
    #     dfsPaths, path, total_flow = dfs(src, path, levels, total_flow)
    #     while dfsPaths:
    #         dfsPaths, path, total_flow = dfs(src, path, levels, total_flow)
    #     bfsPaths, path, levels = bfs(src, sink, path)
    # return total_flow

    
        

if __name__ == "__main__":
    entrances, exits, path = [0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]
    # entrances, exits, path = [0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    
    res = solution(entrances, exits, path)
    print(res)
