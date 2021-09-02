# class Node:

#     def __init__(
#         self,
#         key: int,
#         pred_key: int = None,
#         dest: int = None,
#     ):
#         self.key = key
#         self.pred_key = pred_key
#         self.dest = dest

# class MinPriorityQueue:

#     def __init__(self):
#         self.queue = []
#         self.key2idx = {}

#     def get_size(self):
#         return len(self.queue)

#     def insert(self, node: Node):
#         self.queue.append(node)
#         self.key2idx = {node.key: len(self.queue) - 1}
#         self.heapify_up(len(self.queue) - 1)

#     def get_min(self):
#         return self.queue[0]

#     def extract_min(self):
#         min_node = self.queue[0]
#         self.queue[0], self.queue[len(self.queue) - 1] = (
#             self.queue[len(self.queue) - 1], self.queue[0]
#         )
#         self.queue.pop()
#         del self.key2idx[min_node.key]
#         self.key2idx[self.queue[0].key] = 0
#         self.heapify_down(0)

#     def heapify_up(self, target_idx: int):
#         current_idx = target_idx
#         while (current_idx >= 0):
#             parent_idx = current_idx // 2
#             parent_node = self.queue[parent_idx]
#             current_node = self.queue[current_idx]
#             if (parent_node.dest is None and current_node.dest is None) or (
#                 parent_node.dest is not None and current_node.dest is None
#             ):
#                 break
#             else:
#                 self.queue[parent_idx], self.queue[current_idx] = (
#                     self.queue[current_idx], self.queue[parent_idx]
#                 )
#                 self.key2idx[self.queue[parent_idx].key] = parent_idx
#                 self.key2idx[self.queue[current_idx].key] = current_idx
#                 current_idx = parent_idx

#     def heapify_down(self, target_idx: int):
#         current_idx = target_idx
#         while (current_idx < len(self.queue)):
#             left_child_idx = current_idx * 2 + 1
#             right_child_idx = current_idx * 2 + 2

#             if (
#                 self.queue[current_idx].dest is None and
#                 self.queue[left_child_idx].dest is None and
#                 self.queue[right_child_idx].dest
#             ) or (
#                 self.queue[current_idx].dest is not None and
#                 parent_node.dest is not None and current_node.dest is None
#             ):
#             if self.queue[current_idx].dest <= min(
#                 self.queue[left_child_idx].dest,
#                 self.queue[right_child_idx].dest
#             ):
#                 break

#             if self.queue[left_child_idx].dest <= min(
#                 self.queue[current_idx].dest,
#                 self.queue[right_child_idx].dest
#             ):
#                 self.queue[left_child_idx], self.queue[current_idx] = (
#                     self.queue[current_idx], self.queue[left_child_idx]
#                 )
#                 self.key2idx[self.queue[left_child_idx].key] = left_child_idx
#                 self.key2idx[self.queue[current_idx].key] = current_idx
#                 current_idx = left_child_idx
#             else:
#                 self.queue[right_child_idx], self.queue[current_idx] = (
#                     self.queue[current_idx], self.queue[right_child_idx]
#                 )
#                 self.key2idx[self.queue[right_child_idx].key] = right_child_idx
#                 self.key2idx[self.queue[current_idx].key] = current_idx
#                 current_idx = right_child_idx


# def dijkstra(n, edge_weight_pairs, src):
#     graph = {}
#     for e_src, e_dst, w in edge_weight_pairs:
#         if e_src not in graph:
#             graph[e_src] = {e_dst: w}
#         else:
#             graph[e_src][e_dst] = w

#     pq = MinPriorityQueue()
#     for i in range(n):
#         if i == src:
#             pq.insert(Node(key=i, dest=0))
#         else:
#             pq.insert(Node(key=i))

#     result = []
#     while (pq.get_size() > 0):
#         min_node = pq.extract_min()
#         result.append(min_node)
#         if min_node.key not in graph:
#             continue
#         for dst_key in graph[min_node.key].keys():
#             # relax
#             dst_node = pq.key2idx[dst_key]
#             if dst_node.dest is None:
#                 dst_node.dest = min_node.dest + graph[min_node.key][dst_node.key]
#                 dst_node.pred = min_node.key
#             elif dst_node.dest > min_node.dest + graph[min_node.key][dst_node.key]:
#                 dst_node.dest = min_node.dest + graph[min_node.key][dst_node.key]
#                 dst_node.pred = min_node.key
#     return result
# # graph = {0: [1, 2], 1: [2], 2: []}
# # weight = {(0, 1): 100, (1, 2): 100, (0, 2): 500}
# # src = 0

# n = 3
# edge_weight_pairs = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0
# dijkstra(n, edge_weight_pairs, src)
