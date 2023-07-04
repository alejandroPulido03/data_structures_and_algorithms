def dfs(graph, s, v):
    """
        TODO: Return path

    """
    visited = [-1 for _ in range(len(graph))]
    stack = [s]  # Top in last element
    edgeTo = [-1 for _ in range(len(graph))]
    while len(stack) > 0:
        top = stack[-1]
        if visited[top] == 0:
            stack.pop()
        else:
            visited[top] = 0
            for e in graph[top]:
                if visited[e] == -1:
                    edgeTo[e] = top
                    stack.append(e)

    return edgeTo


print(dfs([[], [6, 4], [4, 5, 6, 7], [4], [1, 2, 3], [2], [1, 2], [2], [9], [8]], 2, 6))
