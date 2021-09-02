from collections import defaultdict


def graph_has_cycle(n_nodes, edges):
    graph = defaultdict(list)
    for node_i in range(n_nodes):
        graph[node_i]
    for src, dst in edges:
        graph[src].append(dst)

    status = [0 for _ in range(n_nodes)]
    for node_i in range(n_nodes):
        if status[node_i] == 0:
            status[node_i] = 1
            has_cycle = dfs(node_i, status, graph)
            if has_cycle:
                return True
    return False


def dfs(node_i, status, graph):
    for nbr_node in graph[node_i]:
        if status[nbr_node] == 0:
            status[nbr_node] = 1
            has_cycle = dfs(nbr_node, status, graph)
            if has_cycle:
                return True

        if status[nbr_node] == 1:
            return True
    status[node_i] = 2
    return False


n_nodes = 3
edges = [[0, 1], [1, 2]]
print(graph_has_cycle(n_nodes, edges))

n_nodes = 3
edges = [[0, 1], [1, 2], [2, 1]]
print(graph_has_cycle(n_nodes, edges))

n_nodes = 3
edges = [[1, 2], [2, 1]]
print(graph_has_cycle(n_nodes, edges))
