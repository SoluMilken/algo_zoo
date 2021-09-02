class Task:
    def __init__(self, idx, start_time, process_time):
        self.idx = idx
        self.start_time = start_time
        self.process_time = process_time
        self.avail_idx = (process_time, idx)

    def __repr__(self):
        return """idx={}; start_time={}; process_time={}; avail_idx={}
        """.format(
            self.idx, self.start_time, self.process_time, self.avail_idx
        )

    def __gt__(self, other_task):
        return self.avail_idx > other_task.avail_idx

    def __lt__(self, other_task):
        return not self.__gt__(other_task)


class MinHeap:
    def __init__(self):
        self.heap = []

    def __repr__(self):
        return " ".join([task.__repr__() for task in self.heap])

    def is_empty(self):
        if len(self.heap) == 0:
            return True
        return False

    def insert(self, task):
        self.heap.append(task)
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        min_task = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.heapify_down(0)
        return min_task

    def heapify_up(self, idx):
        current_idx = idx
        while current_idx > 0:
            parent_idx = (current_idx - 1) // 2
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
        while (current_idx * 2 + 1) < len(self.heap):
            child_idx = self.get_min_child_idx(current_idx)
            if self.heap[child_idx] < self.heap[current_idx]:
                self.heap[child_idx], self.heap[current_idx] = (
                    self.heap[current_idx],
                    self.heap[child_idx],
                )
                current_idx = child_idx
            else:
                break

    def get_min_child_idx(self, idx):
        if (idx * 2 + 2) > (len(self.heap) - 1):
            # one child
            return idx * 2 + 1
        left_child = self.heap[idx * 2 + 1]
        right_child = self.heap[idx * 2 + 2]
        if left_child < right_child:
            return idx * 2 + 1
        return idx * 2 + 2
