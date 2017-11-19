class HashTable:
    def __init__(self, hash_type, values):
        self.type = hash_type
        self.size = len(values)*3 - 1
        self.table = [None]*self.size
        self.values = values
        self.collisions = 0
        self.link = False

        if hash_type == 1:
            for i in range(len(values)):
                index = self.chain_div(self.values[i])
                if self.table[index]:
                    self.link = True
                    self.collisions += 1
                self.add_hash(index, i)
                self.link = False
        elif hash_type == 2:
            for i in range(len(values)):
                index = self.chain_mult(self.values[i])
                if self.table[index]:
                    self.link = True
                    self.collisions += 1
                self.add_hash(index, i)
                self.link = False
        elif hash_type == 3:
            for i in range(len(values)):
                j = 0
                index = self.open_linear(self.values[i], j)
                while self.table[index]:
                    j += 1
                    index = self.open_linear(self.values[i], j)
                    self.collisions += 1
                self.add_hash(index, i)
        elif hash_type == 4:
            for i in range(len(values)):
                j = 0
                index = self.open_square(self.values[i], j)
                while self.table[index]:
                    j += 1
                    index = self.open_square(self.values[i], j)
                    self.collisions += 1
                self.add_hash(index, i)
        else:
            for i in range(len(values)):
                j = 0
                index = self.open_double(self.values[i], j)
                while self.table[index]:
                    j += 1
                    index = self.open_double(self.values[i], j)
                    self.collisions += 1
                self.add_hash(index, i)

    def add_hash(self, index, i):
        if self.type == 1 or self.type == 2:
            if self.link:
                self.table[index].append(self.values[i])
            else:
                self.table[index] = [self.values[i]]
        else:
            self.table[index] = self.values[i]

    def get_collisions_amount(self):
        return self.collisions

    def chain_div(self, i):
        return i % self.size

    def chain_mult(self, i):
        return int(((i * 0.6180339887) % 1) * self.size)

    def open_linear(self, i, j):
        return (i + j) % self.size

    def open_square(self, i, j):
        return (i + j**2) % self.size

    def open_double(self, i, j):
        index_h = i % self.size/2
        index = i % self.size
        return int((index + index_h*j) % self.size)

    def find_sum(self, s):
        for x in self.values:
            y = s - x
            if self.type == 1:
                index = self.chain_div(y)
                if self.table[index]:
                    for i in range(len(self.table[index])):
                        if self.table[index][i] == y:
                            return x, y
            elif self.type == 2:
                index = self.chain_mult(y)
                if self.table[index]:
                    for i in range(len(self.table[index])):
                        if self.table[index][i] == y:
                            return x, y
            elif self.type == 3:
                j = 0
                index = self.open_linear(y, j)
                if self.table[index]:
                    while self.table[index]:
                        if self.table[index] == y:
                            return x, y
                        j += 1
                        index = self.open_linear(y, j)
            elif self.type == 4:
                j = 0
                index = self.open_square(y, j)
                if self.table[index]:
                    while self.table[index]:
                        if self.table[index] == y:
                            return x, y
                        j += 1
                        index = self.open_square(y, j)
            else:
                j = 0
                index = self.open_double(y, j)
                if self.table[index]:
                    while self.table[index]:
                        if self.table[index] == y:
                            return x, y
                        j += 1
                        index = self.open_double(y, j)
        return None
