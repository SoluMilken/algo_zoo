class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    def delete(self, idx):
        self.heap[idx], self.heap[len(self.heap) - 1] = (
            self.heap[len(self.heap) - 1],
            self.heap[idx],
        )
        self.heap = self.heap[:-1]
        self.heapify_down(idx)

    def get_min(self):
        return self.heap[0]

    def extract_min(self):
        min_val = self.heap[0]
        self.delete(0)
        return min_val

    def heapify_up(self, idx):
        current_idx = idx
        while current_idx > 0:
            parent_idx = current_idx // 2
            if self.heap[parent_idx] > self.heap[current_idx]:
                self.heap[parent_idx], self.heap[current_idx] = (
                    self.heap[current_idx],
                    self.heap[parent_idx],
                )
                current_idx = parent_idx
            else:
                break

    def heapify_down(self, idx):
        current_idx = idx
        while current_idx < len(self.heap):
            left_child_idx = current_idx * 2 + 1
            right_child_idx = current_idx * 2 + 2
            # print(current_idx, left_child_idx, right_child_idx)

            if left_child_idx < len(self.heap) and right_child_idx < len(self.heap):
                if self.heap[current_idx] > min(
                    self.heap[left_child_idx], self.heap[right_child_idx]
                ):
                    if self.heap[left_child_idx] < self.heap[right_child_idx]:
                        self.heap[current_idx], self.heap[left_child_idx] = (
                            self.heap[left_child_idx],
                            self.heap[current_idx],
                        )
                        current_idx = left_child_idx
                    else:
                        self.heap[current_idx], self.heap[right_child_idx] = (
                            self.heap[right_child_idx],
                            self.heap[current_idx],
                        )
                        current_idx = right_child_idx

                else:
                    break
            elif left_child_idx < len(self.heap) or right_child_idx < len(self.heap):
                if left_child_idx < len(self.heap):
                    valid_child_idx = left_child_idx
                else:
                    valid_child_idx = right_child_idx

                if self.heap[valid_child_idx] < self.heap[current_idx]:
                    self.heap[current_idx], self.heap[valid_child_idx] = (
                        self.heap[valid_child_idx],
                        self.heap[current_idx],
                    )
                    current_idx = valid_child_idx
                else:
                    break
            else:
                break


min_heap = MinHeap()
min_heap.insert(5)
min_heap.insert(1)
print(min_heap.heap)
min_heap.insert(3)
print(min_heap.heap)
min_heap.extract_min()
print(min_heap.heap)
