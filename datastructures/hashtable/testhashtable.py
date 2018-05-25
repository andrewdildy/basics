import unittest
from hashtable import HashTable

from random import choice
from string import ascii_lowercase

class TestHashTable(unittest.TestCase):

    def test_put_simple(self):
        t = HashTable()
        t.put('a', 1)

    def test_get_simple(self):
        t = HashTable()
        t.put('a', 1)
        self.assertEqual(t.get('a'), 1)
        self.assertEqual(t.get('b'), 'key not found')
        t.put('a', 2)
        self.assertEqual(t.get('a'), 2)

    def test_contains_simple(self):
        t = HashTable()
        t.put('a', 1)
        self.assertEqual(t.contains('a'), True)
        self.assertEqual(t.contains('b'), False)
        t.put('b', 1)
        self.assertEqual(t.contains('b'), True)

    def test_remove_simple(self):
        t = HashTable()
        t.put('a', 1)
        self.assertEqual(t.contains('a'), True)
        t.remove('a')
        self.assertEqual(t.contains('a'), False)
        self.assertEqual(t.remove('b'), 'key not found')

    def test_collisions(self):
        t = HashTable()
        t.put('rwlqyilqlt', 1)
        t.put('eulvcjibif', 2)
        self.assertEqual(t.contains('rwlqyilqlt'), True)
        self.assertEqual(t.contains('eulvcjibif'), True)
        self.assertEqual(t.get('rwlqyilqlt'), 1)
        self.assertEqual(t.get('eulvcjibif'), 2)
        t.remove('rwlqyilqlt')
        self.assertEqual(t.contains('rwlqyilqlt'), False)
        self.assertEqual(t.contains('eulvcjibif'), True)
        t.remove('eulvcjibif')
        self.assertEqual(t.contains('eulvcjibif'), False)

    def test_resize(self):
        added = []
        t = HashTable()
        for i in range(775):
            s = ''.join(choice(ascii_lowercase) for i in range(10))
            added.append(s)
            t.put(s, i)
        for i in range(775):
             self.assertEqual(t.get(added[i]), i)

if __name__ == '__main__':
    unittest.main()
