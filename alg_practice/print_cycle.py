"""
Print Cycle in Graph

ex: 207. Course Schedule
"""


def dfs(node, status, stack, graph):
    print(node, status, stack)
    candidates = graph[node]
    for cand_node in candidates:
        if status[cand_node] == "visiting":
            print_cycle(stack, cand_node)

        if status[cand_node] == "not_visited":
            status[cand_node] = "visiting"
            stack.append(cand_node)
            dfs(cand_node, status, stack, graph)
            status[cand_node] = "not_visited"

    status[node] = "done"


def print_cycle(stack, node):
    output = []
    while len(stack) > 0:
        output.append(stack[-1])
        if stack[-1] == node:
            break
        stack.pop()
    print(output[::-1])


def detect_cycle_in_graph(graph, n_nodes):
    status = ["not_visited" for _ in range(n_nodes)]

    for node, _ in graph.items():
        if status[node] == "not_visited":
            stack = [node]
            status[node] = "visiting"
            dfs(node, status, stack, graph)


if __name__ == "__main__":
    graph = {
        0: [1],
        1: [2],
        2: [3],
        3: [1],
        4: [3],
    }
    detect_cycle_in_graph(graph, len(graph))
