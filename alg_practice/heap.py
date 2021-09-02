class MinHeap:
    def __init__(self):
        self.data = None
        self.n = None

    def get_parent_index(self, index):
        output_index = int((index - 1) / 2)
        if (0 <= index < self.n) and (output_index >= 0):
            return output_index
        return

    def get_left_child_index(self, index):
        output_index = (index * 2) + 1
        if (0 <= index < self.n) and (output_index < self.n):
            return output_index
        return

    def get_right_child_index(self, index):
        output_index = (index * 2) + 2
        if (0 <= index < self.n) and (output_index < self.n):
            return output_index
        return

    def build(self, data):
        self.data = data
        n = len(self.data)
        self.n = n
        for i in range(1, n):
            self.reverse_heapify(i)

    def reverse_heapify(self, index):
        parent_index = self.get_parent_index(index)
        if parent_index is not None:
            if self.data[parent_index] > self.data[index]:
                self.data[parent_index], self.data[index] = (
                    self.data[index],
                    self.data[parent_index],
                )
                self.reverse_heapify(parent_index)
        return

    def heapify(self, index):
        left_index = self.get_left_child_index(index)
        right_index = self.get_right_child_index(index)
        min_value = self.data[index]
        min_index = index

        if left_index is not None:
            if min_value > self.data[left_index]:
                min_value = self.data[left_index]
                min_index = left_index

        if right_index is not None:
            if min_value > self.data[right_index]:
                min_value = self.data[right_index]
                min_index = right_index

        if min_index != index:
            self.data[index], self.data[min_index] = (
                self.data[min_index],
                self.data[index],
            )
            self.heapify(min_index)
        return

    def extract_min(self):
        if self.n == 0:
            return
        min_value = self.data[0]
        self.data[0], self.data[self.n - 1] = self.data[self.n - 1], self.data[0]
        self.n -= 1
        self.heapify(0)
        return min_value


if __name__ == "__main__":
    heap = MinHeap()
    heap.build([9, 2, 5, 3, 7, 1, 2])
    while heap.n > 0:
        print(heap.extract_min())
