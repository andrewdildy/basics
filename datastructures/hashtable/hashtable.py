from entry import Entry

class HashTable:

    def __init__(self):
        self.table = [[] for x in range(1000)]
        self.size = 0

    def put(self, key, value):
        if float(self.size) / len(self.table) > 0.75:
            self._resize()
        i = hash(key) % len(self.table)
        if key in self.table[i]:
            self.remove(key)
        self.table[i].append(Entry(key, value))
        self.size += 1

    def get(self, key):
        i = hash(key) % len(self.table)
        for e in self.table[i]:
            if e == key:
                return e.value
        return 'key not found'

    def remove(self, key):
        i = hash(key) % len(self.table)
        if key in self.table[i]:
            self.table[i].remove(key)
            self.size -= 1
        else:
            return 'key not found'

    def contains(self, key):
        i = hash(key) % len(self.table)
        if key in self.table[i]:
            return True
        return False

    def size(self):
        return self.size

    def _resize(self):
        old_table = self.table
        self.table = [[] for x in range(len(self.table) * 10)]
        self.size = 0
        for entries in old_table:
            if entries:
                for entry in entries:
                    self.put(entry.key, entry.value)
