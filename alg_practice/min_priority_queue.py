import sys


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
        if self.is_empty():
            raise Exception("heap underflow")
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

    def get_parent(self, idx: int):
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

        if (
            right_child_idx < heap_size
            and self.heap[min_idx] > self.heap[right_child_idx]
        ):
            min_idx = right_child_idx

        if min_idx != idx:
            self.swap_node(src_idx=idx, dst_idx=min_idx)
            self.heapify(min_idx)

        # current_idx = idx
        # while current_idx < len(self.heap):
        #     left_child_idx = current_idx * 2 + 1
        #     right_child_idx = current_idx * 2 + 2
        #     # print(current_idx, left_child_idx, right_child_idx)

        #     # left child and right child exist
        #     if left_child_idx < len(self.heap) and right_child_idx < len(self.heap):
        #         if self.heap[current_idx] > min(
        #             self.heap[left_child_idx], self.heap[right_child_idx]
        #         ):
        #             if self.heap[left_child_idx] < self.heap[right_child_idx]:
        #                 self.swap_node(src_idx=current_idx, dst_idx=left_child_idx)
        #                 current_idx = left_child_idx
        #             else:
        #                 self.swap_node(src_idx=current_idx, dst_idx=right_child_idx)
        #                 current_idx = right_child_idx
        #         else:
        #             break
        #     # one of left child or right child exists
        #     elif left_child_idx < len(self.heap) or right_child_idx < len(self.heap):
        #         if left_child_idx < len(self.heap):
        #             valid_child_idx = left_child_idx
        #         else:
        #             valid_child_idx = right_child_idx

        #         if self.heap[valid_child_idx] < self.heap[current_idx]:
        #             self.swap_node(src_idx=current_idx, dst_idx=valid_child_idx)
        #             current_idx = valid_child_idx
        #         else:
        #             break
        #     # none of them exist
        #     else:
        #         break


min_heap = MinPriorityQueue()
min_heap.insert(5, 5)
min_heap.insert(1, 1)
print(min_heap.heap)
min_heap.insert(3, 3)
print(min_heap.heap)
min_heap.extract_min()
print(min_heap.heap)

"""
import sys


class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"data={self.data};priority={self.priority}"


class MinPriorityQueue:
    def __init__(self):
        self.heap = []
        self.data2idx = {}

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, data, priority):
        node = Node(data=data, priority=priority)
        self.heap.append(node)
        self.data2idx[data] = len(self.heap) - 1
        self.heapify_up(len(self.heap) - 1)

    def get_min(self):
        return self.heap[0]

    def extract_min(self):
        min_node = self.heap[0]
        self.delete(min_node.data)
        return min_node

    def decrease_key(self, data, priority):
        idx = self.data2idx[data]
        node = self.heap[idx]
        node.priority = priority
        self.heapify_up(idx)

    def get_key(self, data):
        idx = self.data2idx[data]
        node = self.heap[idx]
        return node.priority
        
    def delete(self, data):
        idx = self.data2idx[data]
        last_idx = len(self.heap) - 1
        # swap
        self.swap_node(src_idx=idx, dst_idx=last_idx)
        # delete node
        del self.data2idx[self.heap[last_idx].data]
        self.heap = self.heap[:-1]
        # heapify_down
        self.heapify_down(idx)

    def swap_node(self, src_idx: int, dst_idx: int):
        self.data2idx[self.heap[src_idx].data] = dst_idx
        self.data2idx[self.heap[dst_idx].data] = src_idx
        self.heap[src_idx], self.heap[dst_idx] = (
            self.heap[dst_idx],
            self.heap[src_idx],
        )

    def heapify_up(self, idx: int):
        current_idx = idx
        while current_idx > 0:
            parent_idx = current_idx // 2
            if self.heap[parent_idx] > self.heap[current_idx]:
                self.swap_node(src_idx=parent_idx, dst_idx=current_idx)
                current_idx = parent_idx
            else:
                break

    def heapify_down(self, idx):
        current_idx = idx
        while current_idx < len(self.heap):
            left_child_idx = current_idx * 2 + 1
            right_child_idx = current_idx * 2 + 2
            # print(current_idx, left_child_idx, right_child_idx)

            # left child and right child exist
            if left_child_idx < len(self.heap) and right_child_idx < len(self.heap):
                if self.heap[current_idx] > min(
                    self.heap[left_child_idx], self.heap[right_child_idx]
                ):
                    if self.heap[left_child_idx] < self.heap[right_child_idx]:
                        self.swap_node(src_idx=current_idx, dst_idx=left_child_idx)
                        current_idx = left_child_idx
                    else:
                        self.swap_node(src_idx=current_idx, dst_idx=right_child_idx)
                        current_idx = right_child_idx
                else:
                    break
            # one of left child or right child exists
            elif left_child_idx < len(self.heap) or right_child_idx < len(self.heap):
                if left_child_idx < len(self.heap):
                    valid_child_idx = left_child_idx
                else:
                    valid_child_idx = right_child_idx

                if self.heap[valid_child_idx] < self.heap[current_idx]:
                    self.swap_node(src_idx=current_idx, dst_idx=valid_child_idx)
                    current_idx = valid_child_idx
                else:
                    break
            # none of them exist
            else:
                break
"""
