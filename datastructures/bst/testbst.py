import unittest
from bst import BST

from random import choice
from string import ascii_lowercase

class TestBST(unittest.TestCase):

    def test_insert_simple(self):
        tree = BST()
        tree.insert(1, 'a')
        self.assertEqual(tree.isBST(), True)

    def test_search_simple(self):
        tree = BST()
        tree.insert(1, 'a')
        self.assertEqual(tree.search(1), 'a')

    def test_delete_simple(self):
        tree = BST()
        tree.insert(1, 'a')
        tree.delete(1)
        self.assertEqual(tree.search(1), None)

    def test_insert_multiple(self):
        tree = BST()
        tree.insert(2, 'b')
        tree.insert(1, 'a')
        tree.insert(3, 'c')
        self.assertEqual(tree.isBST(), True)

    def test_search_multiple(self):
        tree = BST()
        tree.insert(2, 'b')
        self.assertEqual(tree.search(2), 'b')
        tree.insert(1, 'a')
        self.assertEqual(tree.search(1), 'a')
        tree.insert(3, 'c')
        self.assertEqual(tree.search(3), 'c')
        self.assertEqual(tree.search(1), 'a')
        self.assertEqual(tree.search(2), 'b')

    def test_delete_multiple(self):
        tree = BST()
        tree.insert(2, 'b')
        tree.insert(1, 'a')
        tree.insert(3, 'c')
        tree.delete(1)
        self.assertEqual(tree.search(1), None)
        self.assertEqual(tree.left, None)
        self.assertNotEqual(tree.right, None)
        tree.insert(1, 'a')
        self.assertEqual(tree.left.key, 1)
        self.assertEqual(tree.right.key, 3)
        tree.delete(2)
        self.assertEqual(tree.search(2), None)

    def test_insert_random(self):
        tree = BST()
        numbers = list(range(10000))
        inserted = []
        for v in range(10000):
            k = choice(numbers)
            tree.insert(k, v)
            inserted.append(k)
            numbers.remove(k)
        for v in range(10000):
            self.assertEqual(tree.search(inserted[v]), v)

    def test_delete_random(self):
        tree = BST()
        numbers = list(range(10000))
        inserted = []
        for v in range(1000):
            k = choice(numbers)
            tree.insert(k, v)
            inserted.append(k)
            numbers.remove(k)
        for v in range(999):
            k = choice(inserted)
            tree.delete(k)
            inserted.remove(k)
            self.assertEqual(tree.search(k), None)
            self.assertEqual(tree.isBST(), True)
        for k in inserted:
            self.assertNotEqual(tree.search(k), None)

if __name__ == '__main__':
    unittest.main()
