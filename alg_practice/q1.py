# class Node:

#     def __init__(self, name):
#         self.name = name
#         self.nbrs = []


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        if name not in self.nodes:
            self.nodes[name] = []

    def add_edge(self, s, t):
        if s not in self.nodes:
            raise Exception("{} does not exist!!!".format(s))
        if t not in self.nodes:
            raise Exception("{} does not exist!!!".format(t))
        self.nodes[s].append(t)

    def has_edge(self, s, t):
        if s not in self.nodes:
            raise Exception("{} does not exist!!!".format(s))
        if t not in self.nodes:
            raise Exception("{} does not exist!!!".format(t))
        if t in self.nodes[s]:
            return True
        return False


if __name__ == "__main__":
    graph = Graph()
    graph.add_node("n1")
    graph.add_node("n2")
    graph.add_edge("n1", "n2")
    print(graph.has_edge("n1", "n2"))
