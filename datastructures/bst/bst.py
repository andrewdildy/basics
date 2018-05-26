class BST:

    def __init__(self, key=None, value=None, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def insert(self, key, value):
        if not self.key and self.key != 0:
            self.key = key
            self.value = value
        if self.key > key:
            if self.left:
                self.left.insert(key, value)
            else:
                self.left = BST(key=key, value=value, parent=self)
        elif self.key < key:
            if self.right:
                self.right.insert(key, value)
            else:
                self.right = BST(key=key, value=value, parent=self)

    def search(self, key):
        if self.key == key:
            return self.value
        elif self.left and key < self.key:
            return self.left.search(key)
        elif self.right and key > self.key:
            return self.right.search(key)

    def delete(self, key):
        if self.left and self.key > key:
            self.left.delete(key)
            return
        if self.right and self.key < key:
            self.right.delete(key)
            return
        if self.left and self.right:
            new = self.right.find_min()
            self.key = new.key
            self.value = new.value
            new.delete(new.key)
        elif self.left:
            self.replace_parent(self.left)
        elif self.right:
            self.replace_parent(self.right)
        else:
            self.replace_parent()

    def replace_parent(self, new=None):
        if new:
            new.parent = self.parent
        if self.parent:
            if self.parent.left == self:
                self.parent.left = new
            else:
                self.parent.right = new
        elif new:
            if new.right:
                new.right.parent = self
            if new.left:
                new.left.parent = self
            self.key = new.key
            self.value = new.value
            self.left = new.left
            self.right = new.right
        else:
            self.key = None
            self.value = None

    def find_min(self):
        curr = self
        while curr.left:
            curr = curr.left
        return curr

    def isBST(self, min_key=float('-inf'), max_key=float('inf')):
        if self.key < min_key or self.key > max_key:
            return False
        if not self.left and not self.right:
            return True
        elif not self.right:
            return self.left.isBST(min_key=min_key, max_key=self.key)
        elif not self.left:
            return self.right.isBST(min_key=self.key, max_key=max_key)
        else:
            return self.left.isBST(min_key=min_key, max_key=self.key) and self.right.isBST(min_key=self.key, max_key=max_key)

    def keys(self):
        keys = []
        self.traverse(lambda node: keys.append(node.key))
        return keys

    def values(self):
        values = []
        self.traverse(lambda node: keys.append(node.values))
        return values

    def traverse(self, callback):
        if self.left:
            self.left.traverse(callback)
        callback(self)
        if self.right:
            self.right.traverse(callback)
