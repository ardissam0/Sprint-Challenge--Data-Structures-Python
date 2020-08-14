class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.cur = 0

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        else:
            if self.cur == self.capacity:
                self.cur = 0
            self.data[self.cur] = item
        self.cur += 1

    def get(self):
        return self.data