def khan(graph):
    visited = [-1 for _ in range(len(graph))]
    non_visited_vertexes = {i: -1 for i in range(len(graph))}
    dfo = []

    while len(non_visited_vertexes) > 0:
        stack = [list(non_visited_vertexes.keys())[0]]
        while len(stack) > 0:

            top = stack[-1]
            if visited[top] == 0:
                if not top in dfo:
                    dfo.append(top)
                stack.pop()
            else:
                visited[top] = 0
                non_visited_vertexes.pop(top)

                for e in graph[top]:
                    if visited[e] == -1:

                        stack.append(e)

    return dfo[::-1]
