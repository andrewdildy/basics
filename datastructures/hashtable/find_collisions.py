from random import choice
from string import ascii_lowercase

table = [None for x in range(1000)]
for x in range(100000):
    s = ''.join(choice(ascii_lowercase) for i in range(10))
    i = hash(s) % 1000
    if table[i]:
        print(s, table[i])
    else:
        table[i] = s
