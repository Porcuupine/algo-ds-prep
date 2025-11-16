import random


class RandomizedSet:
    def __init__(self):
        self.arr = []  # stores elements
        self.pos = {}  # val -> index in arr

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False

        idx = self.pos[val]  # index of element to delete
        last = self.arr[-1]  # last element

        # move last element to idx
        self.arr[idx] = last
        self.pos[last] = idx

        # remove last element
        self.arr.pop()
        del self.pos[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
