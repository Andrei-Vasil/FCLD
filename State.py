from enum import Enum

class StateType(Enum):
    ACCEPT = 1
    REDUCE = 2
    SHIFT = 3
    REDUCE_REDUCE_CONFLICT = 4
    SHIFT_REDUCE_CONFLICT = 5

def testCond(items: dict[Item], condition) -> bool:
    result = True
    for it in items.keys():
        result = result and condition(it)
    return result

class State:
    def __init__(self, items: dict[Item]):
        self.items = items
        firstItem = list(items.keys())[0]
        self.stateType = StateType.SHIFT_REDUCE_CONFLICT
        if len(items) == 1 and len(firstItem.rhs) == firstItem.dotPosition and firstItem.lhs == Grammar.enrichedGrammarStartingSymbol:
            self.stateType = StateType.ACCEPT
        elif len(items) == 1 and len(firstItem.rhs) == firstItem.dotPosition:
            self.stateType = StateType.REDUCE
        elif len(items) > 0 and testCond(items, lambda it: len(it.rhs) > it.dotPosition):
            self.stateType = StateType.SHIFT
        elif len(items) > 1 and testCond(items, lambda it: len(it.rhs) == it.dotPosition): 
            self.stateType = StateType.REDUCE_REDUCE_CONFLICT

    def getSymbolsSucceedingTheDot(self) -> list[str]:
        symbols = []
        for it in self.items:
            if 0 <= it.dotPosition < len(it.rhs):
                symbols.append(it.rhs[it.dotPosition])
        return symbols

    def __str__(self):
        return f'{self.stateType} items: {str(self.items)}'
