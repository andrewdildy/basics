class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __eq__(self, other):
        if type(other) == Entry:
            return self.key == other.key
        if type(other) == type(self.key):
            return self.key == other
        return False
