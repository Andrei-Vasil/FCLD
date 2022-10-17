# lab2
# Statement: Implement the Symbol Table (ST) as the specified data structure, with the corresponding operations
# Deliverables: class ST (source code) + documentation.
# UPLOAD documentation, on the first line link to git for source code

from dataclasses import dataclass


class HashTableST():
    """
        
    """
    p = 31

    def __init__(self):
        self._size = 0
        self.cap = 10
        self.hashtable = [[] for _ in range(self.cap)]

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value: int) -> None:
        self._size = value
        if self.size >= self.cap // 2:
            self.scaleup()
    
    def hashfnc(self, k: any) -> int:
        k = str(k)
        hashval = 0
        for i, c in enumerate(k):
            hashval += (ord(c) - ord('a') + 1) * (HashTableST.p ** i)
            hashval %= self.cap
        return hashval

    def scaleup(self) -> None:
        self.cap *= 2
        new_hashtable = [[] for _ in range(self.cap)]
        self.reassign(new_hashtable)

    def reassign(self, new_hashtable: list) -> None:
        for vals in self.hashtable:
            for val in vals:
                new_hashtable[self.hashfnc(val)].append(val)
        self.hashtable = new_hashtable

    def add(self, k: any) -> None:
        self.size += 1
        self.hashtable[self.hashfnc(k)].append(k)

    def remove(self, k: any) -> None:
        self.size -= 1
        vals = self.hashtable[self.hashfnc(k)]
        for i, val in enumerate(vals):
            if val == k:
                vals[i] = vals[-1]
                vals.pop()
                break
    
    def exists(self, k: any) -> bool:
        for val in self.hashtable[self.hashfnc(k)]:
            if val == k:
                return True
        return False
