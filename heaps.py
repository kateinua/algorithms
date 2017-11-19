class Median:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        self.maxlen = 0
        self.minlen = 0
        self.c = 0

    def add_element(self, value):
        if self.c == 0 or value < self.maxheap[0]:
            self.maxheap.append(value)
            self.maxlen += 1
            self.max_insert()
        else:
            self.minheap.append(value)
            self.minlen += 1
            self.min_insert()

        if len(self.maxheap) - 2 == len(self.minheap):
            self.minheap.append(self.maxheap[0])
            self.maxheap[0] = self.maxheap.pop()
            self.minlen += 1
            self.maxlen -= 1
            self.min_insert()

        elif len(self.minheap) - 2 == len(self.maxheap):
            self.maxheap.append(self.minheap[0])
            self.minheap[0] = self.minheap.pop()
            self.maxlen += 1
            self.minlen -= 1
            self.max_insert()

        self.maxheap = self.get_maxheap_elements()
        self.minheap = self.get_minheap_elements()
        self.c += 1

    def get_median(self):
        if len(self.maxheap) == len(self.minheap):
            return self.maxheap[0], self.minheap[0]
        else:
            if len(self.maxheap) > len(self.minheap):
                return self.maxheap[0]
            else:
                return self.minheap[0]

    def get_maxheap_elements(self):
        if self.maxlen != 0:
            self.maxheapify(0)
        return self.maxheap

    def get_minheap_elements(self):
        if self.minlen != 0:
            self.minheapify(0)
        return self.minheap

    def maxheapify(self, i):
        p = 2 * i + 1
        q = 2 * i + 2
        if p < self.maxlen and self.maxheap[p] > self.maxheap[i]:
            largest = p
        elif p < self.maxlen:
            largest = i
        else:
            return None

        if q < self.maxlen and self.maxheap[q] > self.maxheap[largest]:
            largest = q

        if largest != i:
            self.maxheap[i], self.maxheap[largest] = self.maxheap[largest], self.maxheap[i]
            self.maxheapify(largest)

    def minheapify(self, i):
        p = 2 * i + 1
        q = 2 * i + 2
        if p < self.minlen and self.minheap[p] < self.minheap[i]:
            smallest = p
        elif p < self.minlen:
            smallest = i
        else:
            return None

        if q < self.minlen and self.minheap[q] < self.minheap[smallest]:
            smallest = q

        if smallest != i:
            self.minheap[i], self.minheap[smallest] = self.minheap[smallest], self.minheap[i]
            self.minheapify(smallest)

    def max_insert(self):
        i = self.maxlen - 1
        while i > 0 and self.maxheap[i] > self.maxheap[(i-1)//2]:
            self.maxheap[i], self.maxheap[(i-1)//2] = self.maxheap[(i-1)//2], self.maxheap[i]
            i = (i-1)//2

    def min_insert(self):
        i = self.minlen - 1
        while i > 0 and self.minheap[i] < self.minheap[(i-1)//2]:
            self.minheap[i], self.minheap[(i-1)//2] = self.minheap[(i-1)//2], self.minheap[i]
            i = (i-1)//2




median = Median()
for x in range(1, 10):
    median.add_element(x)
    print(x, ":", median.get_median())