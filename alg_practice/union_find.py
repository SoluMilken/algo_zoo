"""
A disjoint-set data structure is a data structure that
keeps track of a set of elements partitioned into a number of disjoint
(non-overlapping) subsets.
A union-find algorithm is an algorithm that performs two useful operations on such a data structure:
- Find: Determine which subset a particular element is in.
        This can be used for determining if two elements are in the same subset.
- Union: Join two subsets into a single subset.
Application:
1. to check whether a given graph contains a cycle or not.
"""


class Node:
    def __init__(self, key, rank=0, root_key=None):
        self.key = key
        self.rank = rank
        self.root_key = root_key

    def __repr__(self):
        return "key={};rank={};root_key={}".format(self.key, self.rank, self.root_key)


class DisjointSet:
    def __init__(self):
        self.key2node = {}

    def make_set(self, key: int):
        if key in self.key2node:
            raise KeyError
        else:
            node = Node(key=key)
            self.key2node[key] = node

    def find_set(self, key: int):
        if self.key2node[key].root_key is None:
            return key
        # Path Compression
        root_key = self.find_set(self.key2node[key].root_key)
        self.key2node[key].root_key = root_key
        return root_key

    def union(self, key_x: int, key_y: int):
        root_key_x = self.find_set(key_x)
        root_key_y = self.find_set(key_y)

        root_node_x = self.key2node[root_key_x]
        root_node_y = self.key2node[root_key_y]
        # Union By Rank
        if root_node_x.rank > root_node_y.rank:
            self.key2node[root_node_y.key].root_key = root_node_x.key
        else:
            self.key2node[root_node_x.key].root_key = root_node_y.key
            if root_node_x.rank == root_node_y.rank:
                root_node_y.rank += 1


ds = DisjointSet()
for key in range(10):
    ds.make_set(key)

ds.union(0, 1)
ds.union(2, 1)

ds.union(8, 9)
ds.union(7, 8)
ds.union(5, 9)

print([ds.find_set(i) for i in range(10)])
