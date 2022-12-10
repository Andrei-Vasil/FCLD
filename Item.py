import copy


class Item:
    def __init__(self, lhs: str, rhs: list, dotPos: int):
        self.lhs = lhs
        self.rhs = rhs
        self.dotPos = dotPos

    def deepCopy(self):
        return Item(copy.deepcopy(self.lhs), copy.deepcopy(self.rhs), copy.deepcopy(self.dotPos))