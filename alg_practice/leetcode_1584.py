import sys
from typing import List


class Node:
    def __init__(self, data, key):
        self.data = data
        self.key = key

    def __lt__(self, other):
        return self.key < other.key

    def __repr__(self):
        return f"data={self.data};key={self.key}"


class MinPriorityQueue:
    def __init__(self):
        self.heap = []
        self.data2idx = {}

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, data, key):
        node = Node(data=data, key=sys.maxsize)
        self.heap.append(node)
        self.data2idx[data] = len(self.heap) - 1
        self.decrease_key(data, key)

    def decrease_key(self, data, key):
        idx = self.data2idx[data]
        if key > self.heap[idx].key:
            raise Exception
        self.heap[idx].key = key

        # up
        current_idx = idx
        while (current_idx > 0) and (
            self.heap[self.get_parent(current_idx)] > self.heap[current_idx]
        ):
            self.swap_node(src_idx=self.get_parent(current_idx), dst_idx=current_idx)
            current_idx = self.get_parent(current_idx)

    def get_min(self) -> Node:
        return self.heap[0]

    def extract_min(self) -> Node:
        min_node = self.heap[0]
        self.delete(min_node.data)
        return min_node

    def delete(self, data):
        idx = self.data2idx[data]
        last_idx = len(self.heap) - 1
        # swap
        self.swap_node(src_idx=idx, dst_idx=last_idx)
        # delete node
        del self.data2idx[self.heap[last_idx].data]
        self.heap = self.heap[:-1]
        # heapify_down
        self.heapify(idx)

    def swap_node(self, src_idx: int, dst_idx: int):
        self.data2idx[self.heap[src_idx].data] = dst_idx
        self.data2idx[self.heap[dst_idx].data] = src_idx
        self.heap[src_idx], self.heap[dst_idx] = (
            self.heap[dst_idx],
            self.heap[src_idx],
        )

    def get_parent(self, idx: int) -> int:
        return idx // 2

    def get_left_child(self, idx: int) -> int:
        return idx * 2 + 1

    def get_right_child(self, idx: int) -> int:
        return idx * 2 + 2

    def get_heap_size(self) -> int:
        return len(self.heap)

    def heapify(self, idx: int):
        left_child_idx = self.get_left_child(idx)
        right_child_idx = self.get_right_child(idx)
        heap_size = self.get_heap_size()

        min_idx = idx
        if left_child_idx < heap_size and self.heap[idx] > self.heap[left_child_idx]:
            min_idx = left_child_idx

        if (right_child_idx < heap_size) and (
            self.heap[min_idx] > self.heap[right_child_idx]
        ):
            min_idx = right_child_idx

        if min_idx != idx:
            self.swap_node(src_idx=idx, dst_idx=min_idx)
            self.heapify(min_idx)


pq = MinPriorityQueue()
pq.heap = [Node(data=3, key=3), Node(data=1, key=1), Node(data=2, key=2)]
pq.data2idx = {3: 0, 1: 1, 2: 2}
pq.heapify(0)
print(pq.heap)
print(pq.data2idx)

pq = MinPriorityQueue()
pq.heap = [Node(data=3, key=3), Node(data=2, key=2), Node(data=1, key=1)]
pq.data2idx = {3: 0, 2: 1, 1: 2}
pq.heapify(0)
print(pq.heap)
print(pq.data2idx)

pq = MinPriorityQueue()
pq.heap = [Node(data=3, key=3), Node(data=2, key=2), Node(data=1, key=1)]
pq.data2idx = {3: 0, 2: 1, 1: 2}
pq.heapify(0)
print(pq.heap)
print(pq.data2idx)

pq = MinPriorityQueue()
pq.heap = [Node(data=2, key=2), Node(data=1, key=1)]
pq.data2idx = {2: 0, 1: 1}
pq.heapify(0)
print(pq.heap)
print(pq.data2idx)

# pq = MinPriorityQueue()
# pq.heap = [Node(data=2, key=2), None, Node(data=1, key=1)]
# pq.data2idx = {Node(data=2, key=2): 0, Node(data=1, key=1): 2}
# pq.heapify(0)
# print(pq.heap)
# print(pq.data2idx)


# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         return self.prim(points)

#     def get_weight(self, point_a: List[int], point_b: List[int]) -> int:
#         return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])

#     def prim(self, points: List[List[int]]):
#         pq = MinPriorityQueue()
#         for x, y in points:
#             pq.insert(data=(x, y), key=self.get_weight(points[0], (x, y)))

#         assert len(pq.heap) == len(points)
#         # # print(pq.heap)
#         # # print(pq.data2idx)
#         # first_x, first_y = points[0]
#         # pq.decrease_key(data=(first_x, first_y), key=0)

#         cost = 0
#         while not pq.is_empty():
#             current_node = pq.extract_min()
#             cost += current_node.key
#             current_x, current_y = current_node.data
#             print(current_node)
#             for node in pq.heap:
#                 x, y = node.data
#                 weight = self.get_weight([current_x, current_y], [x, y])
#                 if weight < node.key:
#                     pq.decrease_key(data=(x, y), key=weight)
#         return cost


# sol = Solution()
# points = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0]]
# print(points)
# print(sol.minCostConnectPoints(points))
